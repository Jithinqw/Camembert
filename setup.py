import sys
from setuptools import setup

VERSION = list(map(str, [0, 10, 0]))
DESCRIPTION = "Falcon Utils library for Falcon."

if sys.version_info < (3, 0):
    raise Exception("You require Python3.0 or above to run Camembert")
try:
    with open("README.md") as f:
        LONG_DESCRIPTION = f.read()
except FileNotFoundError:
        LONG_DESCRIPTION = DESCRIPTION

setup(
    name="camembert",
    version=".".join(VERSION),
    description="Falcon middlewares made easy.",
    url="https://github.com/Jithinqw/Camembert",
    author="Jithin Zacharia",
    author_email="zachariajithin@gmail.com",
    license="MIT",
    classifiers=[
        # Trove classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy"
    ],
    packages=["camembert"],
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    download_url="https://github.com/Jithinqw/Camembert/archive/0.10.0.tar.gz",
    install_packages=["falcon"],
    install_requires=["falcon", "pytest","secure"],
    keywords=["falcon", "middlewares"],
)
