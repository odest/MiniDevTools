import hashlib



class HashTool:

    @classmethod
    def __processData(cls, data):
        if isinstance(data, str):
            return data.encode()
        elif isinstance(data, bytes):
            return data
        elif isinstance(data, (list, tuple)):
            return b"".join([str(item).encode() for item in data])
        elif isinstance(data, dict):
            return b"".join([str(key).encode() + str(value).encode() for key, value in data.items()])
        elif isinstance(data, int):
            return str(data).encode()
        elif isinstance(data, float):
            return str(data).encode()
        elif isinstance(data, set):
            return b"".join([str(item).encode() for item in sorted(data)])
        elif isinstance(data, bool):
            return str(data).encode()
        else:
            return False


    @classmethod
    def MD5(cls, text=None, file=None):
        """
        This function hashes data provided either as text or from a file using MD5.

        Args:
            text: String data to be hashed. (Optional)
            file: Path to the file containing data to be hashed. (Optional)

        Returns:
            Hashed data in hexadecimal format (str) on success, None otherwise.

        Raises:
            ValueError: If both text and file are provided or neither are provided!
            ValueError: Invalid Data!
        """

        if (text is None and file is None) or (text is not None and file is not None):
            raise ValueError("Provide either text or file, not both or neither.")

        if text:
            textData = cls.__processData(text)
            if textData:
                textHash = hashlib.md5(textData)
                return textHash.hexdigest()
            else:
                raise ValueError("Invalid Data!")
        else:
            try:
                with open(file, 'rb') as f:
                    fileData = f.read()
                fileHash = hashlib.md5(fileData)
                return fileHash.hexdigest()
            except FileNotFoundError as error:
                print(f'{type(error).__name__}: {str(error)}')
                return None


    @classmethod
    def SHA1(cls, text=None, file=None):
        """
        This function hashes data provided either as text or from a file using SHA1.

        Args:
            text: String data to be hashed. (Optional)
            file: Path to the file containing data to be hashed. (Optional)

        Returns:
            Hashed data in hexadecimal format (str) on success, None otherwise.

        Raises:
            ValueError: If both text and file are provided or neither are provided!
            ValueError: Invalid Data!
        """

        if (text is None and file is None) or (text is not None and file is not None):
            raise ValueError("Provide either text or file, not both or neither.")

        if text:
            textData = cls.__processData(text)
            if textData:
                textHash = hashlib.sha1(textData)
                return textHash.hexdigest()
            else:
                raise ValueError("Invalid Data!")
        else:
            try:
                with open(file, 'rb') as f:
                    fileData = f.read()
                fileHash = hashlib.sha1(fileData)
                return fileHash.hexdigest()
            except FileNotFoundError as error:
                print(f'{type(error).__name__}: {str(error)}')
                return None


    @classmethod
    def SHA256(cls, text=None, file=None):
        """
        This function hashes data provided either as text or from a file using SHA256.

        Args:
            text: String data to be hashed. (Optional)
            file: Path to the file containing data to be hashed. (Optional)

        Returns:
            Hashed data in hexadecimal format (str) on success, None otherwise.

        Raises:
            ValueError: If both text and file are provided or neither are provided!
            ValueError: Invalid Data!
        """

        if (text is None and file is None) or (text is not None and file is not None):
            raise ValueError("Provide either text or file, not both or neither.")

        if text:
            textData = cls.__processData(text)
            if textData:
                textHash = hashlib.sha256(textData)
                return textHash.hexdigest()
            else:
                raise ValueError("Invalid Data!")
        else:
            try:
                with open(file, 'rb') as f:
                    fileData = f.read()
                fileHash = hashlib.sha256(fileData)
                return fileHash.hexdigest()
            except FileNotFoundError as error:
                print(f'{type(error).__name__}: {str(error)}')
                return None


    @classmethod
    def SHA512(cls, text=None, file=None):
        """
        This function hashes data provided either as text or from a file using SHA512.

        Args:
            text: String data to be hashed. (Optional)
            file: Path to the file containing data to be hashed. (Optional)

        Returns:
            Hashed data in hexadecimal format (str) on success, None otherwise.

        Raises:
            ValueError: If both text and file are provided or neither are provided!
            ValueError: Invalid Data!
        """

        if (text is None and file is None) or (text is not None and file is not None):
            raise ValueError("Provide either text or file, not both or neither.")

        if text:
            textData = cls.__processData(text)
            if textData:
                textHash = hashlib.sha512(textData)
                return textHash.hexdigest()
            else:
                raise ValueError("Invalid Data!")
        else:
            try:
                with open(file, 'rb') as f:
                    fileData = f.read()
                fileHash = hashlib.sha512(fileData)
                return fileHash.hexdigest()
            except FileNotFoundError as error:
                print(f'{type(error).__name__}: {str(error)}')
                return None
