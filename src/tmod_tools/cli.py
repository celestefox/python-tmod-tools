"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mtmod_tools` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``tmod_tools.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``tmod_tools.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click
import click_log
import logging
logger = logging.getLogger('tmod_tools') # We want to configure the base logger
click_log.basic_config(logger)


@click.group()
@click.pass_context
@click_log.simple_verbosity_option(logger)
@click.version_option()
def main(ctx):
    if ctx.obj is None:
        ctx.obj = {}
    logger.debug("Main done.")

@click.command()
@click.pass_context
@click.option('-o', '--output', default=None, type=click.Path(file_okay=False), help="The directory to write the contents to.")
@click.argument('file', type=click.File(mode='rb'))
def extract(ctx, output, file):
    pass

main.add_command(extract)
