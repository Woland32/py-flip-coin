import random


def flip_coin(cases: int = 100_000, flips: int = 10) -> dict:
    counts = {heads: 0 for heads in range(flips + 1)}

    for _ in range(cases):
        heads = sum(random.random() < 0.5 for _ in range(flips))
        counts[heads] += 1
    return {
        heads: round(count / cases * 100, 2)
        for heads, count in counts.items()
    }


print(flip_coin())
