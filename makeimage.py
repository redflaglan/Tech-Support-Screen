#!/usr/bin/env python2
import os, textwrap, sys
text = None
if len(sys.argv) > 1:
    pt = int(sys.argv[1])
    width = int(-0.3 * float(sys.argv[1]) + 60)
    if width < 10:
        print "Too large."
        sys.exit(2)
    if len(sys.argv) > 2:
        text = " ".join(sys.argv[2:])
else:
    pt = 100
    width = 30

if not text:
    text = raw_input("Text: ")
tw = textwrap.TextWrapper(width=width)
newtext = u"\n".join([a.replace("\\n", "\n") for a in tw.wrap(text)])

os.system("convert -size 1920x1080 canvas:\"rgb(149, 1, 1)\" \
-font Dejavu-Sans-Bold -pointsize {} -gravity center -stroke none \
-fill white -annotate 0 \"{}\" -size 1920x1080 \"{}.png\"".format(pt, newtext,
  "".join([c for c in text.replace(" ", "-") if c.isalpha() or c.isdigit() or c in ["-", "_"]])))

