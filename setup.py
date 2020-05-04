from setuptools import setup, find_packages

requirements = [
    "click==7.1.2"
]

setup(
    name="comps",
    version="0.3",
    packages=find_packages(),
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=requirements,
    # metadata to display on PyPI
    author="Gauthier the bearded",
    author_email="gauhtier.feuillen@gmail.com",
    description="Make yourself shine",
    entry_points={
        "console_scripts": [
            "compl = comps.cli:comp",
        ],
    },
    python_requires='>=3.7',
)
