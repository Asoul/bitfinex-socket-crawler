import sys
from invoke import task

@task
def lint(ctx, k=None):
    pylint_args = '--output-format=colorized --reports=no'
    options = '--disable=all --enable={}'.format(k) if k else ''
    extra_args = ""
    if not sys.stdout.isatty():
        extra_args = "--output-format=text"
    ctx.run('pylint {} {} {} *.py tools/*.py'.format(pylint_args, options, extra_args))
