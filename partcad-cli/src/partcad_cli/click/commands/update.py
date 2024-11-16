import rich_click as click  # import click
from partcad import Context
from partcad.user_config import user_config


@click.command(help="* Update all imported packages")
@click.pass_obj
def cli(ctx: Context):
    user_config.force_update = True
    ctx.get_all_packages()
