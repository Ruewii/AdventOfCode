from utils.wrapper import Context, Solution


def is_stable(pairs):
    return all(a < b for a, b in pairs) or all(a > b for a, b in pairs)


def is_safe(numbers):
    pairs = list(zip(numbers, numbers[1:]))
    return (
        is_stable(pairs)
        and all(abs(a - b) <= 3 for a, b in pairs)
        and (numbers[0] != numbers[-1])
    )


@Solution
def main(ctx: Context):
    # ctx.name = "test"
    # ctx.load()

    reports = [list(map(int, line.split())) for line in ctx.lines]
    safe_reports = [levels for levels in reports if is_safe(levels)]
    # print("\n".join(map(str, safe_reports)))
    print("Safe Reports:", len(safe_reports))


if __name__ == "__main__":
    main()
