from typing import Callable, Any


class Context:
    def __init__(self):
        self.content = ""

    def read(self, filename):
        with open(filename) as f:
            self.content = f.read()


def Solution(func: Callable[[Context], Any]) -> Callable[[], Any]:
    def wrapper():
        ctx = Context()
        return func(ctx)

    return wrapper
