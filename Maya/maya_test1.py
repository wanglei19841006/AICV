from numpy import *
import numpy as np
from numpy import pi, sin, cos, mgrid
import mayavi
from mayavi import mlab

x=[[-1,1,1,-1,-1], [-1,1,1,-1,-1]]
y=[[-1,-1,-1,-1,-1], [1,1,1,1,1]]
z=[[1,1,-1,-1,1], [1,1,-1,-1,1]]
s = mlab.mesh(x,y,z)
mlab.show()

#--------------------------------mesh------------------------------
dphi, dtheta = pi/250.0, pi/250.0
[phi, theta] = mgrid[0:pi+dphi*1.5:dphi, 0:2*pi+dtheta*1.5:dtheta]
m0=3; m1=2; m2=2; m3=3; m4=8; m5=3; m6=3; m7=3;
r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
x = r*sin(phi)*cos(theta)
y = r*cos(phi)
z = r*sin(phi)*sin(theta)
#sc = mlab.gcf()
#source = sc.children[0]
#manager = source.children[0]
#colors = manager.children[0]
#colors.scalar_lut_manager.lut_mode = 'Blues'
#color.scalar_lut_manager.show_legend = True

s = mlab.mesh(x, y, z)
mlab.show()

#-----------------------------points3d------------------------------
t = np.linspace(0, 4*pi, 20)
x = np.sin(2*t)
y = np.cos(t)
z = np.cos(2*t)
s = 2 + sin(2*t)
points = mlab.points3d(x,y,z,s,colormap="Reds", scale_factor=0.25)
mlab.show()

#-------------------------plot3d-------------------------------------
n_mer, n_long = 6, 11
dphi = pi/1000.0
phi = arange(0.0, 2*pi + 0.5*dphi, dphi)
mu = phi * n_mer
x = np.cos(mu)*(1 + cos(n_long * mu / n_mer) * 0.5)
y = np.sin(mu)*(1 + cos(n_long * mu / n_mer) * 0.5)
z = np.sin(n_long * mu / n_mer) * 0.5
l = mlab.plot3d(x,y,z,0.5*np.sin(mu), tube_radius = 0.025, colormap='Spectral')
mlab.show()