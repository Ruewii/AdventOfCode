from aoc.utils.wrapper import Context, Solution


def is_stable(pairs):
    return all(a < b for a, b in pairs) or all(a > b for a, b in pairs)


def is_safe(numbers):
    pairs = list(zip(numbers, numbers[1:]))
    return (
        is_stable(pairs)
        and all(abs(a - b) <= 3 for a, b in pairs)
        and (numbers[0] != numbers[-1])
    )


def damper(numbers):
    for i in range(len(numbers)):
        if is_safe(numbers[:i] + numbers[i + 1 :]):
            return True
    return False


@Solution
def main(ctx: Context):
    # ctx.name = "test"
    # ctx.load()

    reports = [list(map(int, line.split())) for line in ctx.lines]

    safe_reports = [levels for levels in reports if is_safe(levels)]
    print("[#1 Attempt] Safe Reports:", len(safe_reports))

    safe_reports = [levels for levels in reports if damper(levels)]
    print("[#2 Attempt] Safe Reports:", len(safe_reports))


if __name__ == "__main__":
    main()
