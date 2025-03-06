from setuptools import setup, find_packages
from configparser import ConfigParser

VERSION = '0.0.2' 
DESCRIPTION = 'Helper for plotting 3d vectors and coordinate systems.'
LONG_DESCRIPTION = open("README.md", encoding="utf-8").read()
setup(
    name="trasnformplot3d", 
    version=VERSION,
    author="jan Sani",
    author_email="<santipt50@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['transformations','numpy'],

    keywords=['python', 'matrix', 'matrix transformation', 'transformations','plot', '3d plot', 'quiver'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
