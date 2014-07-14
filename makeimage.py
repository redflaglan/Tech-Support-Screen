#!/usr/bin/env python3
import os
import sys
import textwrap

COMMAND = (
    'convert -size 1920x1080 canvas:"rgb(149, 1, 1)" '
    '-font Dejavu-Sans-Bold -pointsize {} -gravity center -stroke none '
    '-fill white -annotate 0 "{}" -size 1920x1080 "{}.png"'
)


def makeimage(text, point_size=100, width=30):
    tw = textwrap.TextWrapper(width=width)
    text = "\n".join(
        a.replace("\\n", "\n") for a in tw.wrap(text)
    )

    filename = "".join(
        c
        for c in text.replace(" ", "-")
        if c.isalpha() or c.isdigit() or c in ["-", "_"]
    )

    os.system(COMMAND.format(point_size, text, filename))


def main():
    text = None
    if len(sys.argv) > 1:
        pt = int(sys.argv[1])
        width = int(-0.3 * float(sys.argv[1]) + 60)

        if width < 10:
            print("Too large.")
            sys.exit(2)

        if len(sys.argv) > 2:
            text = " ".join(sys.argv[2:])
    else:
        pt = 100
        width = 30

    if not text:
        text = input("Text: ")

    makeimage(text, pt, width)

if __name__ == '__main__':
    main()
