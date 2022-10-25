import httpx

__version__ = "0.1.0"


def foo() -> bool:
    resp = httpx.get("https://loremipsum.io/ultimate-list-of-lorem-ipsum-generators/")
    return True
