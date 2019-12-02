import sys
from setuptools import setup

VERSION = list(map(str, [0, 10, 0]))

if sys.version_info < (3, 0):
    raise Exception("You require Python3.0 or above to run Camembert")

with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="camembert",
    version=".".join(VERSION),
    description="Falcon middlewares made easy.",
    url="https://github.com/Jithinqw/Camembert",
    author="Jithin Zacharia",
    author_email="zachariajithin@gmail.com",
    license="MIT",
    packages=["camembert"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    download_url="https://github.com/Jithinqw/Camembert/archive/0.10.0.tar.gz",
    install_packages=["falcon"],
    install_requires=["falcon", "pytest"],
    keywords=["falcon", "middlewares"],
)
