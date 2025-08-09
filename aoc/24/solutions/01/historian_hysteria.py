from aoc.utils.wrapper import Context, Solution
from collections import Counter


@Solution
def main(ctx: Context):
    lines = [line for line in ctx.content.split("\n") if line]

    def unpack(string: str):
        return map(int, string.strip().split())

    ls, lr = zip(*map(unpack, lines))
    ls, lr = sorted(ls), sorted(lr)

    occurance = [k * v for k, v in Counter(lr).items() if k in ls]
    result = [(l, abs(l - r), r) for l, r in zip(ls, lr)]
    distance = sum(d for _, d, _ in result)

    print("Total Distance:", distance)
    print("Similarity Score:", sum(occurance))


if __name__ == "__main__":
    main()
