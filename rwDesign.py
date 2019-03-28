from numpy import *

class Satellite:
    def __init__(self):
    	'''
    	F_eci = Earth-Centered Inertial Frame:
    	origin - center of earth
    	z - Earth axis of rotation to celestial North Pol
    	x - Center of Sun to center of Earth during vernal equinox
    	y - completed axis for right-hand orthonormal frame

		F_o = Spacecraft Orbit Reference Frame:
		origin - center of mass of spacecraft
		er - axis coincide with vector r, center of earth to spacecraft
		eh - axis parallel to orbital angular momentum vector, pointing in the orbital normal direction
		et - theta axis, completed axis for right-hand orthonormal frame

		F_b = Spacecraft body reference frame:
		origin - center of mass of spacecraft
		z - Iz, principal axis of inertia
		y - Iy, principal axis of inertia
		x - Ix, principal axis of inertia
    	'''
    	self.F_eci = zeros(3)
    	self.F_o   = zeros(3)
    	self.F_b   = zeros(3)
	
	def rotMax(self,a,b):
		Ra_b = eye(3) + 2*nContraint*sFunc()
	
	def sFunc(e, nPower=1):
		return array([[0,-e[2],e[1]],[e[2],0,-e[0]],[-e[1],e[0],0]])