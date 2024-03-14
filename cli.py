from typing_extensions import Annotated
from typing import Optional
from enum import Enum

from minidevtools import HashTool, VERSION, PROJECT_URL, INFO_URL, check_update
from src import showBanner

import pyperclip
import typer



class HashAlgorithm(str, Enum):
    MD5 = "md5"
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA512 = "sha512"


app = typer.Typer(
    help=f"> A new version is available at {PROJECT_URL}/releases.\n" if check_update(VERSION, INFO_URL) else "",
    epilog=f"> Check out the docs at {PROJECT_URL} for more details.",
    rich_markup_mode="markdown",
    context_settings={"help_option_names": ["-h", "--help"]},
    add_completion=False)


@app.command(help="Hash texts or files with MD5, SHA1, SHA256, SHA512")
def hash(
    text: Annotated[str, typer.Option("--text", "-t", help="Text to be hashed.")] = None,
    file: Annotated[str, typer.Option("--file", "-f", help="File to be hashed.")] = None,
    algorithm: Annotated[HashAlgorithm, typer.Option("--algoritm", "-a", help="Hashing algorithm to be used.", case_sensitive=False)] = HashAlgorithm.SHA256,
    copy: Annotated[bool, typer.Option("--copy", "-c", help="Copy to text.")] = False
):
    if (text is None and file is None) or (text is not None and file is not None):
        typer.secho("Provide either --text or --file, not both or neither.", fg='red')
        return

    if text:
        data = text
    elif file:
        data = file

    if algorithm == 'md5':
        hashed = HashTool.MD5(text=text, file=file)
    elif algorithm == 'sha1':
        hashed = HashTool.SHA1(text=text, file=file)
    elif algorithm == 'sha256':
        hashed = HashTool.SHA256(text=text, file=file)
    elif algorithm == 'sha512':
        hashed = HashTool.SHA512(text=text, file=file)
    else:
        typer.secho("Unsupported hashing algorithm. Please provide one of these ('md5', 'sha1', 'sha256', 'sha512').", fg='yellow')
        return

    if hashed:
        typer.secho(f"Hashed Data with {algorithm.upper()}: {hashed}", bold=True, fg='green')

    if copy:
        pyperclip.copy(hashed)
        typer.secho("Hashed Data copied to clipboard.", bold=True, fg='green')


def version_callback(value: bool):
    if value:
        print(f"MiniDevTools: v{VERSION}")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def callback(
    ctx: typer.Context,
    version: Annotated[
        Optional[bool],
        typer.Option("--version", "-v", help="Show the version and exit.", callback=version_callback, is_eager=True),
    ] = None):
    if ctx.invoked_subcommand is None:
        showBanner()
        typer.echo(ctx.get_help())


if __name__ == "__main__":
    app()
