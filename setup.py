import sys
from setuptools import setup
__version__ = list(map(str, [0, 0, 1]))

if sys.version_info < (3, 0):
    raise Exception("You require Python3.0 or above to run Camembert")

setup(
    name= "camembert",
    version= ".".join(__version__)
    description= "Falcon middlewares made easy.",
    url= "https://github.com/Jithinqw/Camembert",
    author="Jithin Zacharia",
    author_email="zachariajithin@gmail.com",
    license="MIT",
    packages=["camembert"],
    install_packages=["falcon"],
    keywords= ["falcon", "middlewares"]
)
