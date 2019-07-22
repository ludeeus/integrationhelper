"""Setup configuration."""
import setuptools
from integrationhelper.version import Version

with open("README.md", "r") as fh:
    LONG = fh.read()

with open("requirements.txt", "r") as fh:
    REQURIE = fh.read()

setuptools.setup(
    name="integrationhelper",
    version=Version().version,
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="A set of helpers for integrations.",
    long_description=LONG,
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/integrationhelper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)