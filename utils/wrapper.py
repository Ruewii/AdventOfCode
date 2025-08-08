import os
import sys
import inspect
from typing import Callable, Any
from pathlib import Path


class Context:
    def __init__(self):
        self.name = ""
        self.content = ""

    def _load(self):
        if not self.name:
            raise RuntimeError("Module name is empty.")

        input_path = f"inputs/{self.name}.txt"
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found. ({input_path})")

        with open(input_path) as f:
            self.content = f.read()
            if not self.content:
                raise RuntimeError("Input content is empty.")


def Solution(func: Callable[[Context], Any]) -> Callable[[], Any]:

    def main():
        ctx = Context()
        f = Path(inspect.stack()[1].filename)
        ctx.name = f.stem
        print(f"Day {f.parent.stem}:", ctx.name.replace("_", " ").capitalize())
        ctx._load()
        return func(ctx)

    return main
