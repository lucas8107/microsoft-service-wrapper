from enum import Enum
from dataclasses import dataclass

SCOPES = ["https://analysis.windows.net/powerbi/api/.default"]


class DatasetUserAccessRightEntry(str, Enum):
    READ = "Read"  # Grants Read access to the content in the dataset
    READ_EXPLORE = (
        "ReadExplore"  # Grants Read and Explore access to the content in the dataset
    )
    READ_RESHARE = (
        "ReadReshare"  # Grants Read and Reshare access to the content in the dataset
    )
    READ_RESHARE_EXPLORE = "ReadReshareExplore"  # Grants Read, Reshare, and Explore access to the content in the dataset


class DatasetUserAccessRight(str, Enum):
    NONE = "None"  # Removes permission to the content in the dataset
    READ = "Read"  # Grants Read access to the content in the dataset
    READ_EXPLORE = (
        "ReadExplore"  # Grants Read and Explore access to the content in the dataset
    )
    READ_RESHARE = (
        "ReadReshare"  # Grants Read and Reshare access to the content in the dataset
    )
    READ_RESHARE_EXPLORE = "ReadReshareExplore"  # Grants Read, Reshare, and Explore access to the content in the dataset
    READ_WRITE = (
        "ReadWrite"  # Grants Read and Write access to the content in the dataset
    )
    READ_WRITE_EXPLORE = "ReadWriteExplore"  # Grants Read, Write, and Explore access to the content in the dataset
    READ_WRITE_RESHARE = "ReadWriteReshare"  # Grants Read, Write, and Reshare access to the content in the dataset
    READ_WRITE_RESHARE_EXPLORE = "ReadWriteReshareExplore"  # Grants Read, Write, Reshare, and Explore access to the content in the dataset


class PrincipalType(str, Enum):
    APP = "App"  # Service principal type
    GROUP = "Group"  # Group principal type
    NONE = "None"  # No principal type. Use for whole organization level access.
    USER = "User"  # User principal type


class GroupUserAccessRight(str, Enum):
    ADMIN = "Admin"  # Administrator rights to workspace content
    CONTRIBUTOR = (
        "Contributor"  # Read and explore (ReadExplore) access to workspace content
    )
    MEMBER = "Member"  # Read, reshare and explore (ReadReshareExplore) access rights to workspace content
    NONE = "None"  # No access to workspace content
    VIEWER = "Viewer"  # Read-only (Read) access to workspace conten


@dataclass
class ServicePrincipalProfile:
    displayName: str
    id: str
