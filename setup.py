"""
Setup script for Island Survival.

This script allows the project to be installed as a package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="island-survival",
    version="1.0.0",
    author="Jake Tantorski",
    author_email="jake.tantorski1@marist.edu",
    description="A text-based adventure game where players must survive on an island",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jaketantorski/CMPT120-Project",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["main"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "island-survival=main:main",
        ],
    },
    keywords="game, adventure, text-based, survival",
    project_urls={
        "Bug Reports": "https://github.com/jaketantorski/CMPT120-Project/issues",
        "Source": "https://github.com/jaketantorski/CMPT120-Project",
    },
)
