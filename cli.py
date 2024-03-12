from typing_extensions import Annotated
from typing import Optional

import typer


VERSION = '0.0.1'
PROJECT_URL = 'https://github.com/odest/MiniDevTools'


app = typer.Typer(
    epilog=f"Check out the docs at {PROJECT_URL} for more details.",
    rich_markup_mode="markdown",
    context_settings={"help_option_names": ["-h", "--help"]},
    add_completion=False)


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
        typer.echo(ctx.get_help())


if __name__ == "__main__":
    app()
