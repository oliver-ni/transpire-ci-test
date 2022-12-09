from typing import Generator

from transpire.types import Image

name = "transpire-ci-test"


def objects():
    return []


def images() -> list[Image]:
    return [
        Image("hello", "/hello"),
    ]
