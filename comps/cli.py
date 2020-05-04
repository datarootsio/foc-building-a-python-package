import sys
from urllib.request import urlopen

import click

from .main import *


@click.command()
def comp():
    comp_stream = urlopen(
        'https://raw.githubusercontent.com/datarootsio/foc-building-a-python-package/master/compliments.json')
    comps = load_comp(comp_stream)
    if comps is None:
        print("Couldn't read compliments from file")
        sys.exit(-1)
    comp = select_comp(comps)
    if comp is None:
        print("Couldn't select a compliment in the list")
        sys.exit(-1)
    print(comp)


if __name__ == '__main__':
    comp()
