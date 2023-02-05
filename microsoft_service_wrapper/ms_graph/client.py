import msal
from typing import List, Dict
import json
import logging

from ..generic.client import BaseClient

MAX_USERS_PER_REQUEST = 20


logger = logging.getLogger(__name__)

class MsGraphClient(BaseClient):

    scopes = ["https://graph.microsoft.com/.default"]

    def __init__(self, app: msal.ClientApplication) -> None:
        super().__init__(app)
        self.group_map = self.get_pbi_groups()

    def get_pbi_groups(self) -> Dict[str, str]:
        groups = self.api_call(
            url="https://graph.microsoft.com/v1.0/groups?$filter=startsWith(displayname, 'pbi')&$select=displayName,id",
            extra_headers={"ConsistencyLevel": "eventual"},
        )

        return {
            group["displayName"]: group["id"] for group in groups
        }

    def get_group_members(self, group_id):
        return self.api_call(
            url=f"https://graph.microsoft.com/v1.0/groups/{group_id}/members?$select=userPrincipalName,id",
        )

    def add_users_to_group(self, group_name: str, user_email_list: List[str]) -> None:
        if not user_email_list:
            return

        group_id = self.group_map[group_name]

        for i in range(0, len(user_email_list), MAX_USERS_PER_REQUEST):

            data = {
                "members@odata.bind": [
                    f"https://graph.microsoft.com/v1.0/users/{email}"
                    for email in user_email_list[i : i + MAX_USERS_PER_REQUEST]
                ]
            }

            self.api_call(
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

        user_id_list = [user["id"] for user in group_members if user["userPrincipalName"] in user_email_list]

        for user_id in user_id_list:
            try:
                self.api_call(
                    url=f"https://graph.microsoft.com/v1.0/groups/{group_id}/members/{user_id}/$ref",
                    method="delete",
                )
            except Exception:
                logger.exception()
