"""CLI"""

from enum import Enum
from typing import Optional, Annotated

import typer

from .hash_tool import HashTool
from .utils import VERSION, PROJECT_URL, INFO_URL
from .utils import show_banner, check_update


class HashAlgorithm(str, Enum):
    """An enumeration representing common cryptographic hash algorithms.

    This class provides named constants for well-known hash algorithms,
    making it easier to work with them in your code.

    Attributes:
        MD5 (str): The MD5 hash algorithm.
        SHA1 (str): The SHA-1 hash algorithm.
        SHA256 (str): The SHA-256 hash algorithm.
        SHA512 (str): The SHA-512 hash algorithm.
    """

    MD5 = "md5"
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA512 = "sha512"


app = typer.Typer(
    help="A Swiss Army Knife for Developers",
    epilog=f"""
    > For help with a specific command, see: `mdt <command> --help`.
    \n
    \n
    > Check out the docs at {PROJECT_URL} for more details.
    """,
    rich_markup_mode="markdown",
    context_settings={"help_option_names": ["-h", "--help"]},
    add_completion=False,
)


@app.command(help="Hash texts or files with MD5, SHA1, SHA256, SHA512")
def hash(
    text: Annotated[
        str, typer.Option("--text", "-t", help="Text to be hashed.")
    ] = None,
    file: Annotated[
        str, typer.Option("--file", "-f", help="File to be hashed.")
    ] = None,
    algorithm: Annotated[
        HashAlgorithm,
        typer.Option(
            "--algoritm",
            "-a",
            help="Hashing algorithm to be used.",
            case_sensitive=False,
        ),
    ] = HashAlgorithm.SHA256,
) -> str | None:
    """Hashes a text or file with a chosen algorithm.

    This function allows you to hash either text you provide directly or the
    contents of a file. You can choose between MD5, SHA1, SHA256, or SHA512
    hashing algorithms. The hashed data can be optionally copied to your
    clipboard.

    Args:
        text (str, optional): The text to hash. Defaults to None.
        file (str, optional): The path to the file to hash. Defaults to None.
        algorithm (HashAlgorithm, optional): The hashing algorithm to use.
            Defaults to SHA256.
    """
    if (text is None and file is None) or (
        text is not None and file is not None
    ):
        typer.secho(
            "Provide either --text or --file, not both or neither.", fg="red"
        )
        return

    if algorithm == "md5":
        hashed = HashTool.MD5(text=text, file=file)
    elif algorithm == "sha1":
        hashed = HashTool.SHA1(text=text, file=file)
    elif algorithm == "sha256":
        hashed = HashTool.SHA256(text=text, file=file)
    elif algorithm == "sha512":
        hashed = HashTool.SHA512(text=text, file=file)
    else:
        typer.secho(
            "Unsupported hashing algorithm. Please provide one of these \
            ('md5', 'sha1', 'sha256', 'sha512').",
            fg="yellow",
        )
        return

    if hashed:
        typer.secho(
            f"Hashed Data with {algorithm.upper()}: {hashed}",
            bold=True,
            fg="green",
        )


def version_callback(value: bool):
    """Prints the version of MiniDevTools and exits the program.

    Args:
        value (bool): This argument is ignored. The function always prints
                    the version and exits.
    """
    if value:
        typer.echo(f"MiniDevTools: v{VERSION}")

        latest_version = check_update(VERSION, INFO_URL)
        if latest_version is not None:
            typer.secho(
                f"A new release of mdt is available: v{VERSION} -> v{latest_version}\nTo upgrade, run: pip install minidevtools --upgrade",
                fg="green",
            )

        raise typer.Exit()


@app.callback(invoke_without_command=True)
def callback(
    ctx: typer.Context,
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            help="Show the version and exit.",
            callback=version_callback,
            is_eager=True,
        ),
    ] = None,
):
    """This callback function serves two main purposes:

    1. Displays the application banner and help message if no subcommand is
        invoked.
    2. Handles the `--version` or `-v` flag for showing the version and
        exiting.


    Args:
        ctx (typer.Context): The Typer context object providing information
            about the current execution.
        version (Annotated[ Optional[bool], typer.Option, optional):
            - If `True` (inferred from the `--version` or `-v` flag), displays
                the application version and exits.
            - If `None` (default), no version handling is performed.
    """
    __version = version
    if ctx.invoked_subcommand is None:
        show_banner()
        typer.echo(ctx.get_help())

        latest_version = check_update(VERSION, INFO_URL)
        if latest_version is not None:
            typer.secho(
                f"A new release of mdt is available: v{VERSION} -> v{latest_version}\nTo upgrade, run: pip install minidevtools --upgrade",
                fg="green",
            )


if __name__ == "__main__":
    app()
