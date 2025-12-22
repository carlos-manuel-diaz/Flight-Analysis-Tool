from setuptools import setup, find_packages

DISTNAME = "orion-analysis"
VERSION = "1.0"
PYTHON_REQUIRES = ">=3.6"
DESCRIPTION = "Pyside6 tool for analyzing post-launch rocketry sensor data, developed for Orbihub"
LONG_DESCRIPTION = open("README.md").read()
AUTHOR = "Carlos M Diaz"
MAINTAINER_EMAIL = "cmdiaz2012.1@hotmail.com"
LICENSE = "MIT License"
URL = "https://github.com/carlos-manuel-diaz/Flight-Analysis-Tool"

setup(
    name=DISTNAME,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    python_requires=PYTHON_REQUIRES,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    maintainer_email=MAINTAINER_EMAIL,
    license=LICENSE,
    url=URL,
    install_requires=[
        "PySide6>=6.5.2",
        "PySide6-Addons>=6.5.2",
        "PySide6-Essentials>=6.5.2",
        "shiboken6>=6.5.2",
    ],
    package_data={
        "": [
            "assets/**/*",
            "ui/*.ui",
            "*.txt",
            "*.rst",
            "*.json",
            "*.jpg",
            "*.qss",
            "*.sh",
            "*.svg",
            "*.png",
            "*.kv",
            "*.bat",
            "*.csv",
            "*.md",
            "*.yml",
            "*.dll",
            "*.idf",
            "*.doctree",
            ".*info",
            "*.html",
            "*.js",
            "*.inv",
            "*.gif",
            "*.css",
            "*.eps",
            "*.pickle",
            "*.xlsx",
            "*.ttf",
            "*.pdf",
            "**/license*",
            "*.yml",
            "*.ui",
            "*.eot",
            "*.woff",
            "*.woff2",
            "LICENSE",
            "*.mplstyle",
            "*.ini",
        ],
    },
    entry_points={"console_scripts": ["orion = orion.__main__:main"]},
)