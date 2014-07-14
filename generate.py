#!/usr/bin/env python2
import os
stuff = {"Network cables can be purchased at the canteen": 60,
         "Stupid Questions May Incur A Fee": 90,
         "Zero tolerance on illegal downloads See the Intranet for more information": 80,
         "HAVE YOU TRIED TURNING IT OFF AND ON AGAIN?": 100,
         "RFLAN 49": 150,
         "TECH SUPPORT": 150,
         "THIS IS NOT THE GAMES ADMIN DESK": 100}
for k,v in stuff.items():
    os.system("./makeimage.py {} {}".format(v, k))
    print "Done {} at {}pt".format(k, v)
