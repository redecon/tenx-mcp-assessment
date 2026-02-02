from src.reverse_string import reverse_string


def run():
    cases = [
        ("", ""),
        ("a", "a"),
        ("racecar", "racecar"),
        ("hello", "olleh"),
        ("こんにちは", "はちにんこ"),
    ]
    for inp, expected in cases:
        out = reverse_string(inp)
        assert out == expected, f"{inp!r} -> {out!r} != {expected!r}"
    print("All tests passed")


if __name__ == "__main__":
    run()
