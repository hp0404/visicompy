# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

from visicom import __version__


def get_long_description() -> str:
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as readme_path:
        return readme_path.read()



setup(
    name="visicom",
    version=__version__,
    url="https://github.com/hp0404/visicompy.git",
    author="hp0404",
    long_description=get_long_description(),
    packages=find_packages(),
    install_requires=["httpx==0.22.0"],
)
