import sys
from setuptools import setup
__version__ = list(map(str, [0, 4, 0]))

if sys.version_info < (3, 0):
    raise Exception("You require Python3.0 or above to run Camembert")

with open("README.md") as f:
    long_description = f.read()
    
setup(
    name= "camembert",
    version= ".".join(__version__),
    description= "Falcon middlewares made easy.",
    url= "https://github.com/Jithinqw/Camembert",
    author="Jithin Zacharia",
    author_email="zachariajithin@gmail.com",
    license="MIT",
    packages=["camembert"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/Jithinqw/Camembert/archive/0.4.0.tar.gz",
    install_packages=["falcon"],
    install_requires=[
          "falcon"],
    keywords= ["falcon", "middlewares"]
)
