#!/usr/bin/env python3
"""One-word Wi-Fi entry: the network is named after the appliance that kills it.

A microwave oven leaks 2.4 GHz noise and murders Wi-Fi every time it runs,
so naming the network after it is both the funniest and the most accurate word.
"""
import os

WORD = "Microwave"  # one word, no spaces, no punctuation

# Entry rule: exactly one word. Nothing else is written to entry.txt.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; entry.txt lives inside it.
    if out_dir.endswith("entry.txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
