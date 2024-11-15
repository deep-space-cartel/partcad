import logging
import rich_click as click
import os

plugin_folder = os.path.join(os.path.dirname(__file__), "commands")


class MyCLI(click.RichGroup):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py") and filename != "__init__.py":
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + ".py")
        # logging.debug(f"Loading {fn}")
        with open(fn) as f:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)
        return ns["cli"]


@click.command(cls=MyCLI, help="PartCAD command line tool")
@click.option("-v", is_flag=True, help="Increase the level of verbosity")
@click.option("-q", is_flag=True, help="Decrease the level of verbosity")
@click.option(
    "--no-ansi",
    is_flag=True,
    help="Plain logging output. Do not use colors or animations.",
)
@click.option(
    "-p",
    type=click.Path(exists=True),
    help="Package path (a YAML file or a directory with 'partcad.yaml')",
)
def cli(v, q, no_ansi, p):
    pass


# cli = MyCLI(
#     help="This tool's subcommands are loaded from a "
#     "plugin folder dynamically."
# )
#
# if __name__ == "__main__":
#     cli()
