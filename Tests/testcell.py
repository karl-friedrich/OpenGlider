#!/bin/python2

__author__ = 'simon'
from openglider.Profile import Profile2D
from openglider.Cells import BasicCell
from openglider.Ribs import Rib
import os
import math
#import numpy
import openglider.Graphics as Graph
from openglider.Utils.Ballooning import BallooningBezier


a = Profile2D()
a.importdat(os.path.dirname(os.path.abspath(__file__))+"/test.dat")
#a.Numpoints = 400


ballooning = BallooningBezier()
balloon = [ballooning(i) for i in a.XValues]


r1 = Rib(a, ballooning, [0.12, 0, 0], 1., 20*math.pi/180, 2*math.pi/180, 0, 7)
r3 = Rib(a, ballooning, [0.3, 0.2, -0.1], 0.8, 30*math.pi/180, 5*math.pi/180, 0, 7)
r2 = r1.copy()
r2.mirror()
for i in [r1, r2, r3]:
    i.recalc()


cell = BasicCell(r2.profile_3d, r1.profile_3d, balloon)
cell2 = BasicCell(r1.profile_3d, r3.profile_3d, balloon)



num = 20
ribs = [cell.midrib(x*1./num) for x in range(num+1)]
ribs += [cell2.midrib(x*1./num) for x in range(num+1)]
#G.Graphics3D([G.Line(r1.profile_3d.data),G.Line(r2.profile_3d.data),G.Line([[0.,0.,0.],[1.,0.,0.]]),G.Line([[0.,0.,0.],[0.,0.5,0.]])])
Graph.Graphics3D([Graph.Line(x.data) for x in ribs])
