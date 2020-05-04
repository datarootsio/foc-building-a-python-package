import setuptools


setuptools.setup(
    name='complimentme',
    version='0.1.0',
    author='Pablito',
    author_email='pablo@dataroots.io',
    description='Boost your ego with compliments',
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ["complimentme = complimentme.compliments:main"]
    }
)