import logging
import partcad as pc
import partcad_cli as pcc
import rich_click as click  # import click


@click.command(
    help="* Print PartCAD & PartCAD CLI versions and exit"
)  # @cli, not @click!
def cli():
    logging.info("PartCAD version: %s" % pc.__version__)
    logging.info("PartCAD CLI version: %s" % pcc.__version__)
