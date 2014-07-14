#!/usr/bin/env python2
from makeimage import makeimage

stuff = [
    ("Network cables can be purchased at the canteen", 60),
    ("Stupid Questions May Incur A Fee", 90),
    (
        "Zero tolerance on illegal downloads "
        "See the Intranet for more information",
        80
    ),
    ("HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?", 100),
    ("RFLAN 49", 150),
    ("TECH SUPPORT", 150),
    ("THIS IS NOT THE GAMES ADMIN DESK", 100),
]

for text, point in stuff:
    makeimage(text, point)

    print('Done {} at {}pt'.format(text, point))
