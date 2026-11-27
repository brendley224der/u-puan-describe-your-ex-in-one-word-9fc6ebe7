#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word to /output/entry.txt: the one-word verdict on an ex.
Pure standard library, deterministic: the same word on every run.
"""

import os

WORD = "unsubscribed"


def validate(word):
    """Gate mirror: 1-111 chars, not only whitespace, exactly one word."""
    if not (1 <= len(word) <= 111):
        raise ValueError("word must be 1-111 characters")
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
