from numpy import *
from scipy.spatial.transform import Rotation as R

'''
Notaion:



'''

class Satellite:
    def __init__(self):
    	'''
    	F_eci = Earth-Centered Inertial Frame - Globally Referenced:
    	origin - center of earth
    	z - Earth axis of rotation to celestial North Pole
    	x - Center of Sun to center of Earth during vernal equinox
    	y - completed axis for right-hand orthonormal frame

    	Rx_y - Rotation Matrix from frame y to x : v_x = Rx_y (dot) v_y

		Ro_e = Spacecraft Orbit Reference Frame - Rotation Maxtrix Globally Referenced:
		origin - center of mass of spacecraft
		er - axis coincide with vector r, center of earth to spacecraft
		eh - axis parallel to orbital angular momentum vector, pointing in the orbital normal direction
		et - theta axis, completed axis for right-hand orthonormal frame

		Vector convention: [x,y,z]

		Rb_e = Spacecraft body reference frame - Rotation Maxtrix Globally Referenced:
		origin - center of mass of spacecraft
		z - Iz, principal axis of inertia
		y - Iy, principal axis of inertia
		x - Ix, principal axis of inertia
    	'''
    	self.F_eci = eye(3)
    	self.Ro_e   = zeros(3)
    	self.Rb_e   = zeros(3)

    	self.COM_eci = zeros(3) #Globally Referenced
    	self.angularMomentum_e = zeros(3) #Globally Referenced

    def setCOM_eci(self,vector):
    	self.COM_eci = vector 

    def setAngularMomentum_e(self,vector):
    	self.angularMomentum_e = vector

    def setEarthInertialFrame(self,frame):
    	self.F_eci = frame

    def setSpacecraftOrbitFrame(self,frame):
    	if self.COM_eci == zeros(3) or self.angularMomentum_e == zeros(3):
    		raise Exception("COM_eci: angularMomentum_e: {}".format(self.COM_eci,self.angularMomentum_e))

    #Greenwich Mean Sidereal Time (GMST) angle
    # T0 - number of Julian centuries elapsed since J2000 epoch
    def getThetaGMST(self, T0, hh, mm, ss):
    	return (1/240.) * ((24110.54841 + (8640184.812866*T0) + (0.093104*T0**2) + (-6.2e-6 * T0**3) + (1.002737909350795 * (3600*hh + 60*mm + ss))) % 86400.)

	def getRf_i(self):
		thetaGMST = self.getThetaGMST()
		return array([[cos(thetaGMST),sin(thetaGMST),0],[-sin(thetaGMST),cos(thetaGMST),0],[0,0,1]])

	#r - radius from body to earth center, phi - body latitude, psi - body longitude
	#S - {s1, s2, s3} - rotating frame - point in direction of increasing r,phi,psi respectively
	def getRs_f(self,r,phi,psi):
		return array([[sin(phi)*cos(psi),sin(phi)*sin(psi),cos(phi)],[cos(phi)*cos(psi),cos(phi)*sin(psi),-sin(phi)],[-sin(psi),cos(psi),0]])

	#ECI to Orbital Reference frame: r - spacecraft position vector in ECI frame, v - spacefract velovity vector in ECI frame
	def getRi_o(self,r,v):
		o3 = -r/linalg.norm(r)
		o2 = -(cross(r,v)/linalg.norm(cross(r,v)))
		return array([cross(o2,o3),o2,o3])

	def rotMax(self,a,b):
		Ra_b = eye(3) + 2*nContraint*sFunc()
	
	def sFunc(, nPower=1):
		return array([[0,-e[2],e[1]],[e[2],0,-e[0]],[-e[1],e[0],0]])