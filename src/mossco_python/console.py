import click
from . import __version__

@click.command()
@click.version_option(version=__version__)

def main():
    """Python tools for MOSSCO"""
    click.echo("Hello, world!")
