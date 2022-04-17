from enum import Enum


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
