import click
from github_contributions import get_contributions


@click.command()
@click.argument('usernames')
def get_contributions_cli(usernames):
    """Print out users' public contributions"""
    click.echo(get_contributions(usernames.split(',')))

if __name__ == '__main__':
    get_contributions_cli()
