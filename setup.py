import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sudoku2svg",
    version = "0.0.1",
    author = "Roi Rodriguez Mendez",
    author_email = "roi.rodriguez.mendez@gmail.com",
    description = ("Produces a svg from a sudoku grid, with corner / center marks and coloring support."),
    license = "MIT",
    keywords = "sudoku",
    url = "https://github.com/roirodriguez/sudoku2svg",
    # adding packages
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data = {
        'sudoku2svg': ['templates/*']
    },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)