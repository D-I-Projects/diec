import click
from .encoder import encode
from .decoder import decode

@click.group()
def cli():
    """Diec, CLI Library."""
    pass

@cli.command()
@click.argument('text')
def encode_cli(text):
    """Encodes the provided text."""
    encode(text)
    
@cli.command()
def decode_cli():
    """Decodes the provided text."""
    decode()

cli.add_command(encode_cli)
cli.add_command(decode_cli)
