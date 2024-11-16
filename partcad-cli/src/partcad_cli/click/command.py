import logging
import rich_click as click
import os
import partcad as pc
import coloredlogs, logging

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


@click.command(cls=MyCLI)  # , help=""
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
@click.pass_context
def cli(ctx, v, q, no_ansi, p):
    """
    \b
    ██████╗  █████╗ ██████╗ ████████╗ ██████╗ █████╗ ██████╗
    ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
    ██████╔╝███████║██████╔╝   ██║   ██║     ███████║██║  ██║
    ██╔═══╝ ██╔══██║██╔══██╗   ██║   ██║     ██╔══██║██║  ██║
    ██║     ██║  ██║██║  ██║   ██║   ╚██████╗██║  ██║██████╔╝
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚═════╝

    """
    if no_ansi:
        logging.basicConfig()
    else:
        # Create a logger object.
        logger = logging.getLogger(__name__)

        # By default the install() function installs a handler on the root logger,
        # this means that log messages from your code and log messages from the
        # libraries that you use will all show up on the terminal.
        coloredlogs.install(level="DEBUG")

        # If you don't want to see log messages from libraries, you can pass a
        # specific logger object to the install() function. In this case only log
        # messages originating from that logger will show up on the terminal.
        coloredlogs.install(
            level="DEBUG",  # env.COLOREDLOGS_LOG_LEVEL
            logger=logger,
            # .venv/lib/python3.11/site-packages/coloredlogs/__init__.py:DEFAULT_LOG_FORMAT
            fmt="%(asctime)s.%(msecs)03d %(levelname)s %(message)s",  # env.COLOREDLOGS_LOG_FORMAT
            datefmt="%H:%M:%S",
            # fmt="%(pathname)s:%(lineno)d - %(message)s",
        )

        pc.logging_ansi_terminal_init()

    if q:
        pc.logging.setLevel(logging.CRITICAL + 1)
    else:
        if v:
            pc.logging.setLevel(logging.DEBUG)
        else:
            pc.logging.setLevel(logging.INFO)

    if p is None:
        ctx.obj = pc.init()
    else:
        ctx.obj = pc.init(p)


if __name__ == "__main__":
    cli()
