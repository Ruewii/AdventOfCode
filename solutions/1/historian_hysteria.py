from utils.wrapper import Context, Solution


def unpack(string: str):
    l, _, r = string.partition(" ")
    return map(int, [l.strip(), r.strip()])


@Solution
def main(ctx: Context):
    ctx.read("inputs/historian_hysteria.txt")
    lines = [line for line in ctx.content.split("\n") if line]

    ls, lr = zip(*map(unpack, lines))
    ls, lr = sorted(ls), sorted(lr)

    result = [abs(l - r) for l, r in zip(ls, lr)]
    distance = sum(result)

    print("Total Distance:", distance)


if __name__ == "__main__":
    main()
