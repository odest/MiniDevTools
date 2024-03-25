"""Hash texts or files with MD5, SHA1, SHA256, SHA512"""

import hashlib
from typing import Union
from typing import Optional


class HashTool:
    """Hash texts or files with MD5, SHA1, SHA256, SHA512

    Returns:
        str: The .hexdigest() method of a hash object returns a string of
        hexadecimal digits that represents the hash value of the data passed
        to the object.
    """

    @classmethod
    def MD5(
        cls,
        text: Optional[Union[str, bytes, int, float, bool]] = None,
        file: Optional[str] = None,
    ) -> str | None:
        """
        This function hashes data provided either as text or from a file using
        MD5.

        Args:
            text: String data to be hashed. (Optional)
            file: Path to the file containing data to be hashed. (Optional)

        Returns:
            Hashed data in hexadecimal format (str) on success, None otherwise.

        Raises:
            ValueError: If both text and file are provided or neither are
                provided!
            ValueError: Invalid Data!
        """

        if (text is None and file is None) or (
            text is not None and file is not None
        ):
            raise ValueError(
                "Provide either text or file, not both or neither."
            )

        if text:
            text_data = None
            if isinstance(text, bytes):
                text_data = text
            elif isinstance(text, (str, int, float, bool)):
                text_data = str(text).encode()

            if text_data:
                text_hash = hashlib.md5(text_data)
                return text_hash.hexdigest()
            raise ValueError("Invalid Data!")

        if file:
            try:
                with open(file, "rb") as f:
                    file_data = f.read()
                file_hash = hashlib.md5(file_data)
                return file_hash.hexdigest()
            except FileNotFoundError as error:
                print(f"{type(error).__name__}: {str(error)}")
                return None

    @classmethod
    def SHA1(
        cls,
        text: Optional[Union[str, bytes, int, float, bool]] = None,
        file: Optional[str] = None,
    ) -> str | None:
        """
        This function hashes data provided either as text or from a file using
        SHA1.

        Args:
            text: String data to be hashed. (Optional)
            file: Path to the file containing data to be hashed. (Optional)

        Returns:
            Hashed data in hexadecimal format (str) on success, None otherwise.

        Raises:
            ValueError: If both text and file are provided or neither are
                provided!
            ValueError: Invalid Data!
        """

        if (text is None and file is None) or (
            text is not None and file is not None
        ):
            raise ValueError(
                "Provide either text or file, not both or neither."
            )

        if text:
            text_data = None
            if isinstance(text, bytes):
                text_data = text
            elif isinstance(text, (str, int, float, bool)):
                text_data = str(text).encode()

            if text_data:
                text_hash = hashlib.sha1(text_data)
                return text_hash.hexdigest()
            raise ValueError("Invalid Data!")

        if file:
            try:
                with open(file, "rb") as f:
                    file_data = f.read()
                file_hash = hashlib.sha1(file_data)
                return file_hash.hexdigest()
            except FileNotFoundError as error:
                print(f"{type(error).__name__}: {str(error)}")
                return None

    @classmethod
    def SHA256(
        cls,
        text: Optional[Union[str, bytes, int, float, bool]] = None,
        file: Optional[str] = None,
    ) -> str | None:
        """
        This function hashes data provided either as text or from a file using
        SHA256.

        Args:
            text: String data to be hashed. (Optional)
            file: Path to the file containing data to be hashed. (Optional)

        Returns:
            Hashed data in hexadecimal format (str) on success, None otherwise.

        Raises:
            ValueError: If both text and file are provided or neither are
                provided!
            ValueError: Invalid Data!
        """

        if (text is None and file is None) or (
            text is not None and file is not None
        ):
            raise ValueError(
                "Provide either text or file, not both or neither."
            )

        if text:
            text_data = None
            if isinstance(text, bytes):
                text_data = text
            elif isinstance(text, (str, int, float, bool)):
                text_data = str(text).encode()

            if text_data:
                text_hash = hashlib.sha256(text_data)
                return text_hash.hexdigest()
            raise ValueError("Invalid Data!")

        if file:
            try:
                with open(file, "rb") as f:
                    file_data = f.read()
                file_hash = hashlib.sha256(file_data)
                return file_hash.hexdigest()
            except FileNotFoundError as error:
                print(f"{type(error).__name__}: {str(error)}")
                return None

    @classmethod
    def SHA512(
        cls,
        text: Optional[Union[str, bytes, int, float, bool]] = None,
        file: Optional[str] = None,
    ) -> str | None:
        """
        This function hashes data provided either as text or from a file using
        SHA512.

        Args:
            text: String data to be hashed. (Optional)
            file: Path to the file containing data to be hashed. (Optional)

        Returns:
            Hashed data in hexadecimal format (str) on success, None otherwise.

        Raises:
            ValueError: If both text and file are provided or neither are
                provided!
            ValueError: Invalid Data!
        """

        if (text is None and file is None) or (
            text is not None and file is not None
        ):
            raise ValueError(
                "Provide either text or file, not both or neither."
            )

        if text:
            text_data = None
            if isinstance(text, bytes):
                text_data = text
            elif isinstance(text, (str, int, float, bool)):
                text_data = str(text).encode()

            if text_data:
                text_hash = hashlib.sha512(text_data)
                return text_hash.hexdigest()
            raise ValueError("Invalid Data!")

        if file:
            try:
                with open(file, "rb") as f:
                    file_data = f.read()
                file_hash = hashlib.sha512(file_data)
                return file_hash.hexdigest()
            except FileNotFoundError as error:
                print(f"{type(error).__name__}: {str(error)}")
                return None
