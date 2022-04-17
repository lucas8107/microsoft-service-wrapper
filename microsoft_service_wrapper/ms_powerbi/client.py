import json

from ..generic.client import BaseClient
from .constants import (
    DatasetUserAccessRightEntry,
    DatasetUserAccessRight,
    PrincipalType,
)


class MsPowerBiClient(BaseClient):

    scopes = ["https://analysis.windows.net/powerbi/api/.default"]

    def get_workspaces(self, *args, **kwargs):
        workspaces = self.api_call(url="https://api.powerbi.com/v1.0/myorg/groups")

        return workspaces

    def grant_workspace_dataset_permission_to_user(
        self,
        workspace_id: str,
        dataset_id: str,
        user_principal_name: str,
        access_right: DatasetUserAccessRightEntry,
    ) -> None:
        if not any([workspace_id, dataset_id, user_principal_name, access_right]):
            return

        data = {
            "datasetUserAccessRight": access_right,
            "identifier": user_principal_name,
            "principalType": PrincipalType.USER,
        }

        return self.api_call(
            url=f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets/{dataset_id}/users",
            body=json.dumps(data),
            extra_headers={"Content-Type": "application/json"},
            method="post",
        )

    def update_workspace_dataset_permission_to_user(
        self,
        workspace_id: str,
        dataset_id: str,
        user_principal_name: str,
        access_right: DatasetUserAccessRight,
    ) -> None:
        if not any([workspace_id, dataset_id, user_principal_name, access_right]):
            return

        data = {
            "datasetUserAccessRight": access_right,
            "identifier": user_principal_name,
            "principalType": PrincipalType.USER,
        }

        return self.api_call(
            url=f"https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets/{dataset_id}/users",
            body=json.dumps(data),
            extra_headers={"Content-Type": "application/json"},
            method="put",
        )

    def revoke_workspace_dataset_permission_to_user(
        self, workspace_id: str, dataset_id: str, user_principal_name: str
    ) -> None:
        self.update_workspace_dataset_permission_to_user(
            workspace_id,
            dataset_id,
            user_principal_name,
            access_right=DatasetUserAccessRight.NONE,
        )
