from typing import Generator

from transpire.types import Image

name = "transpire-ci-test"


def objects():
    return
    yield


def images():
    yield Image(name="hello", path="/hello")
