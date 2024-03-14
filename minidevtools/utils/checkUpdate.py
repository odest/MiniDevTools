from packaging import version
import requests
import re



def is_internet_connected():
    """Checks internet connectivity using GitHub status as a reliable endpoint.

    Returns:
        bool: True if internet connection is available, False otherwise.
    """

    try:
        # Use a context manager for cleaner resource management
        with requests.get("https://www.githubstatus.com/", timeout=5) as response:
            response.raise_for_status()  # Raise exception for non-2xx status codes
        return True

    except requests.exceptions.RequestException as e:
        # Log the exception for debugging or monitoring purposes
        return False


def get_latest_version(url):
    """Fetches the latest version from the given URL.

    Args:
        url (str): The URL to fetch the version information from.

    Returns:
        str: The extracted version string, or None if not found.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-2xx status codes

        match = re.search(r"VERSION\s*=\s*['\"]([^'\"]+)['\"]", response.text)
        if match:
            return match.group(1)
        else:
            return None

    except requests.exceptions.RequestException:
        return None


def check_update(current_version, update_url):
    """Checks for a newer version of software available at the provided URL.

    Args:
        current_version (str): The currently installed version of the software.
        update_url (str): The URL where the latest version information is located.

    Returns:
        bool: True if a newer version is available, False otherwise.

    """

    if is_internet_connected():
        return version.parse(current_version) < version.parse(get_latest_version(update_url))
