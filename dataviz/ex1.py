# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 14:58:44 2017

@author: Jonas Lindemann
"""

import numpy as np
import pyvtk as vtk

print("Reading from uvw.dat...")
xyzuvw = np.loadtxt('uvw.dat', skiprows=2)

print("Converting to points and vectors")
points = xyzuvw[:, 0:3].tolist()
vectors = xyzuvw[:, 3:].tolist()

pointdata = vtk.PointData(vtk.Vectors(vectors))
data = vtk.VtkData(vtk.StructuredPoints([96, 65, 48]), pointdata)
data.tofile('example1','ascii')
data.tofile('example1b','binary')

