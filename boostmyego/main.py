import click

import boostmyego.compliment as bc


def cli():
    cs = bc.fetch_compliments()
    print("🍕 {}".format(bc.give_compliment(cs)))


if __name__ == "__main__":
    cli()
