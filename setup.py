from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Helper for plotting 3d vectors and coordinate systems.'
LONG_DESCRIPTION = 'Helper for plotting 3d vectors and coordinate systems using `matplotlib` and matrices from `transformations`.'

setup(
    name="trasnformplot3d", 
    version=VERSION,
    author="jan Sani",
    author_email="<santipt50@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
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