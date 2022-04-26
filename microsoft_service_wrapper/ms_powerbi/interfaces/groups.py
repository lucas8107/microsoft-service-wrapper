from abc import ABC
from dataclasses import dataclass
from typing import List
from microsoft_service_wrapper.generic.client import api_call_factory

from microsoft_service_wrapper.ms_powerbi.constants import GroupUserAccessRight, PrincipalType, ServicePrincipalProfile, SCOPES


api_call = api_call_factory(scopes=SCOPES, self.app, self.session)


@dataclass
class Group:
    capacityId: str
    dataflowStorageId: str
    id: str
    isOnDedicatedCapacity: bool
    isReadOnly: bool
    name: str


@dataclass
class GroupUser:
    displayName: str
    emailAddress: str
    graphId: str
    groupUserAccessRight: GroupUserAccessRight
    identifier: str
    principalType: PrincipalType
    profile: ServicePrincipalProfile


class GroupsApi(ABC):
    """https://docs.microsoft.com/en-us/rest/api/power-bi/groups"""

    def add_group_user(self):
        """https://docs.microsoft.com/en-us/rest/api/power-bi/groups/add-group-user"""
        ...
        def add_group_user(
        self,
        group_id: str,
        group_user_access_right: GroupUserAccessRight,
        identifier: str,
        principal_type: PrincipalType,
        display_name: str = None,
        email_address: str = None,
        graph_id: str = None,
        profile: ServicePrincipalProfile = None,
    ) -> None:

        self.api_call(
            url=f"https://api.powerbi.com/v1.0/myorg/groups/{group_id}/users",
            method="post",
        )

    def create_group(self):
        """https://docs.microsoft.com/en-us/rest/api/power-bi/groups/create-group"""
        ...

    def delete_group(self):
        """https://docs.microsoft.com/en-us/rest/api/power-bi/groups/delete-group"""
        ...

    def delete_user_in_group(self):
        """https://docs.microsoft.com/en-us/rest/api/power-bi/groups/delete-user-in-group"""
        ...

    def get_groups(self, filter: str = None, skip: int = None, top: int = None) -> List[Group]:
        """https://docs.microsoft.com/en-us/rest/api/power-bi/groups/get-groups"""
        result = self.api_call(url=f"https://api.powerbi.com/v1.0/myorg/groups")

        groups = []

        for group in result:
            groups.append(Group(**group))

        return groups

    def get_group_users(self, group_id: str, skip: int, top: int) -> List[GroupUser]:
        """https://docs.microsoft.com/en-us/rest/api/power-bi/groups/get-group-users"""
        ...

    def update_group_user(self):
        """https://docs.microsoft.com/en-us/rest/api/power-bi/groups/update-group-user"""
        ...
