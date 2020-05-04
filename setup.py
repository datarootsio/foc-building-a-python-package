from setuptools import setup, find_packages

setup(
    name="BoostMyEgo",
    version="1.3.3.7",
    author="Bart",
    description="Boosts my own personal ego!",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": ["boostmyego = boostmyego.compliment:print_compliment",],
    },
)
