from setuptools import setup, find_packages

setup(
    name="orion",
    version="0.4",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.0",
    ],
    package_data={
        "orion": ["ui/*.ui"],
    },
    include_package_data=True,
)