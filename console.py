#!/usr/bin/python2

import sys
import os
import Graphics as G
from Profile import Profile2D
from Utils.Bezier import BezierCurve
import numpy as np

#clear the terminal
os.system('clear')

#custom prompt
sys.ps1 = ">"
sys.ps2 = '>>'
os.environ['PYTHONINSPECT'] = 'True'
print(
"                     xxxxxxxxxxxxxxx                                  \n"
"                xxxxxxxxxxxxxxxxxxxxxxx                               \n"
"            xxxxxxxxxxx       x        x                              \n"
"        xxxxxxxxxxx  x       xx       xx                              \n"
"      xxxxxxxxx     xx        x       x                               \n"
"    xxxxxxxx          xx      x       x    xxxxxxxxx       xxxxxxxxxxx\n"
"  xxxxxxxx  x           x      x      x   xxx     xxxx    xxx         \n"
" xxxxxxx    xx           x      x     x  xx         xx   xxx          \n"
"xxxxxx                    xx    x     x  xx         xxx  xx     xxxxxx\n"
"xxxxxx           xx         x    x    x  xx         xx   xx        xxx\n"
"xxxx  xx           xx        xx  xx   x  xxx       xxx   xxx       xxx\n"
"xxxx    xxx          xx        x  x   x   xxx     xxx     xxxx     xxx\n"
" xx          xx         x       x  x xx     xxxxxxx         xxxxxxxx  \n"
"  xx                             xxxxx                                \n"
"                           x       xxx                                \n"
"                    xx xxx  xxxxx   xx                                \n"
"                             xxxxxx                                   "
)
try:
	import readline
except ImportError:
	print("Module readline not available.")
else:
	import rlcompleter
readline.parse_and_bind("tab: complete")

print('imported: numpy:np, Graphics:G, Profile:Profile2D ProfilIndt:b Utils:BezierCurve')

