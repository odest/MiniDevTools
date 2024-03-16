"""This module provides functions to check internet connectivity,
retrieve software versions, and perform update checks."""

import re
import requests
from packaging import version


def is_internet_connected() -> bool | None:
    """Checks internet connectivity by attempting to
    access a reliable online resource.

    Returns:
        bool | None: True if internet connection is detected, False otherwise.
    """

    try:
        with requests.get(
            "https://www.githubstatus.com/", timeout=3
        ) as response:
            response.raise_for_status()
        return True

    except requests.exceptions.RequestException:
        return False


def get_latest_version(url: str) -> str | None:
    """Fetches the latest version from the given URL.

    Args:
        url (str): The URL to fetch the version information from.

    Returns:
        str: The extracted version string, or None if not found.
    """

    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()

        match = re.search(r"VERSION\s*=\s*['\"]([^'\"]+)['\"]", response.text)
        if match:
            return match.group(1)

        return None

    except requests.exceptions.RequestException:
        return None


def check_update(current_version: str, update_url: str) -> bool | None:
    """Checks for a newer version of software available at the provided URL.

    Args:
        current_version (str): The currently installed version of the software.
        update_url (str): The URL where the latest version
            information is located.

    Returns:
        bool: True if a newer version is available, False otherwise.
    """

    if is_internet_connected():
        latest_version = get_latest_version(update_url)
        if latest_version is not None:
            return version.parse(current_version) < version.parse(
                latest_version
            )
    return None
