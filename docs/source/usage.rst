Usage
=====
The usage of MiniDevTools is versatile and offers multiple options to suit various workflows.
Whether integrating it as a package into your codebase, utilizing its Command Line Interface (CLI) for quick tasks,
or experiencing its features through the forthcoming Graphical User Interface (GUI), MiniDevTools provides flexibility and efficiency.
Each option caters to different preferences, ensuring seamless integration into your development process.

MiniDevTools offers three options for usage:

As a Package
------------

Integrate MiniDevTools into your own code or project as a package. Simply import it as follows:

.. code-block:: python

    from minidevtools import HashTool

    # Hashing text
    hash_text = HashTool.SHA256(text="Hello, world!")
    print("Hashed text with SHA256:", hash_text)

    # Hashing file
    hash_file = HashTool.SHA256(file="image.png")
    print("Hashed file with SHA256:", hash_file)

You can then use the functionalities provided by MiniDevTools within your codebase.

Command Line Interface (CLI)
-----------------------------

Utilize MiniDevTools via the Command Line Interface (CLI) for quick and efficient tasks. Execute the CLI script as follows:

.. code-block:: bash

    mdt --help

.. code-block:: bash

    Usage: mdt [OPTIONS] COMMAND [ARGS]...

    ╭─ Options ────────────────────────────────────────────────────────────────────────╮
    │ --version  -v        Show the version and exit.                                  │
    │ --help     -h        Show this message and exit.                                 │
    ╰──────────────────────────────────────────────────────────────────────────────────╯

    ╭─ Commands ───────────────────────────────────────────────────────────────────────╮
    │ hash  Hash texts or files with MD5, SHA1, SHA256, SHA512                         │
    ╰──────────────────────────────────────────────────────────────────────────────────╯

    ▌ For help with a specific command, see: mdt <command> --help.
    ▌ Check out the docs at https://github.com/odest/MiniDevTools for more details.

.. code-block:: bash

    Usage: mdt hash [OPTIONS]

    Hash texts or files with MD5, SHA1, SHA256, SHA512

    ╭─ Options ───────────────────────────────────────────────────────────────────────╮
    │ --text      -t      TEXT                      Text to be hashed.                │
    │                                               [default: None]                   │
    │ --file      -f      TEXT                      File to be hashed.                │
    │                                               [default: None]                   │
    │ --algoritm  -a      [md5|sha1|sha256|sha512]  Hashing algorithm to be used.     │
    │                                               [default: HashAlgorithm.SHA256]   │
    │ --help      -h                                Show this message and exit.       │
    ╰─────────────────────────────────────────────────────────────────────────────────╯

This allows you to access MiniDevTools' features directly from the command line.

Graphical User Interface (GUI)
-------------------------------

Experience MiniDevTools' capabilities through the Graphical User Interface (GUI) for a user-friendly interaction. Launch the GUI to access its functionalities effortlessly.

.. admonition:: Note
	
    The GUI option is currently under development and will be available soon.


Choose the option that best suits your workflow and preferences to make the most out of MiniDevTools.
