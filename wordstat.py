
import re
from collections import Counter
from pathlib import Path
import argparse


def count_words(text):
    words = re.findall(r"\b\w+\b", text.casefold())
    return Counter(words)


def get_top_words(text, n):
    if n < 1:
        raise ValueError("n must be at least 1")

    counts = count_words(text)

    return sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )[:n]


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Count words in a text file."
    )

    parser.add_argument(
        "file",
        type=Path,
        help="Input text file"
    )

    parser.add_argument(
        "-n",
        "--top",
        type=int,
        default=10,
        help="Number of top words to display"
    )

    args = parser.parse_args(argv)

    if args.top < 1:
        parser.error("--top must be at least 1")

    try:
        text = args.file.read_text(encoding="utf-8")
    except FileNotFoundError:
        parser.error(f"file not found: {args.file}")

    results = get_top_words(text, args.top)

    if not results:
        print("No words found.")
        return

    for word, count in results:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
