import msal
from typing import List, Dict
import json

import pandas as pd

from ..generic.client import BaseClient


class MsGraphClient(BaseClient):

    scopes = ["https://graph.microsoft.com/.default"]

    def __init__(self, app: msal.ClientApplication) -> None:
        super().__init__(app)
        self.group_map = self.get_pbi_groups()

    def get_pbi_groups(self) -> Dict[str, str]:
        groups = self.api_call(
            url="https://graph.microsoft.com/v1.0/groups?$filter=startsWith(displayname, 'pbi_')&$select=displayName,id",
            extra_headers={"ConsistencyLevel": "eventual"},
        )

        df = pd.DataFrame(data=groups)
        return dict(zip(list(df["displayName"]), list(df["id"])))

    def get_group_members(self, group_id):
        return self.api_call(
            url=f"https://graph.microsoft.com/v1.0/groups/{group_id}/members?$select=userPrincipalName,id",
        )

    def add_users_to_group(self, group_name: str, user_email_list: List[str]) -> None:
        if not user_email_list:
            return

        group_id = self.group_map[group_name]

        data = {
            "members@odata.bind": [
                f"https://graph.microsoft.com/v1.0/users/{email}"
                for email in user_email_list
            ]
        }

        return self.api_call(
            url=f"https://graph.microsoft.com/v1.0/groups/{group_id}",
            body=json.dumps(data),
            extra_headers={"Content-Type": "application/json"},
            method="patch",
        )

    def remove_users_from_group(
        self, group_name: str, user_email_list: List[str]
    ) -> None:
        if not user_email_list:
            return

        group_id = self.group_map[group_name]

        group_members = self.get_group_members(group_id)

        if not group_members:
            return

        df = pd.DataFrame(data=group_members)
        user_id_list = list(df[df["userPrincipalName"].isin(user_email_list)]["id"])

        for user_id in user_id_list:
            try:
                self.api_call(
                    url=f"https://graph.microsoft.com/v1.0/groups/{group_id}/members/{user_id}/$ref",
                    method="delete",
                )
            except Exception as e:
                print(e)
