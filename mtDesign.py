from numpy import *
import matplotlib.pyplot as plt
from IPython import embed
from scipy.optimize import minimize

#based on: http://www.raumfahrt.fh-aachen.de/compass-1/download/Diploma_Thesis_Ali_Aydinlioglu.pdf

#https://en.wikibooks.org/wiki/Engineering_Tables/Standard_Wire_Gauge
V_bus = 5.0 #V
u_0 = 1.25663706e-6 #m kg s-2 A-2 - permiability of free space
u_r = 2000. #relative permisability = material permiability / u_0
R_m = 1.55e-8 #R_m - resistance of wire material - Ohm*m

guageCSA = {
20: 0.5176e-6,
21: 0.4105e-6,
22: 0.3255e-6,
23: 0.2582e-6,
24: 0.2047e-6,
25: 0.1624e-6,
26: 0.1288e-6,
27: 0.1021e-6,
28: 0.0810e-6,
29: 0.0642e-6,
30: 0.0509e-6,
31: 0.0404e-6,
32: 0.0320e-6,
33: 0.0254e-6,
34: 0.0201e-6,
35: 0.0160e-6,
36: 0.0127e-6,
37: 0.0100e-6,
38: 0.0080e-6,
39: 0.0063e-6,
40: 0.0050e-6,
}

materialDict = {
	'Copper': {
		'density': [8.92e3,'kg/m^3'],
		'permiability': [1.256629e-6,'H/m'],
		'resistivity': [1.55e-8,'Ohm*m'],
		'u_r':  [1.256629e-6/u_0, 'u/u0']
	},
	#'Al': {
	#	'density': [2.7e-3,'g/mm^3'],
	#	'resistivity': [2.5e-5,'Ohm*mm'],
	#	'tempCoeffResistivity': [3.90e-3,'1/K'],
	#},
	'MnZnFerrite': {
		'density': [8.74e3, 'kg/m^3'],
		'u_r': [2300,'u/u0'],
	}
}
'''
xMap:
0 - radius of the core
1 - N number of turns of wire
'''

#guage, m^2

allResults = []
for guage, a_w in guageCSA.items():
	def demagnetizingFactor(params):
		rc, lc, N = params
		return 4*(log(lc/rc)-1.)/((lc/rc)**2 - 4*log(lc/rc))

	def magDipoleMoment(params, mat_core=materialDict['MnZnFerrite'], mat_wire=materialDict['Copper']):
		rc, lc, N = params
		M = (pi*(rc**2)*N*V_bus/wireResistance(params))*(1+((mat_core['u_r'][0]-1)/(1.+(mat_core['u_r'][0]-1)*demagnetizingFactor(params))))
		return M

	def objective(params):
		return -magDipoleMoment(params)

	def powerConstraint(params, power=0.2, mat_core=materialDict['MnZnFerrite'], mat_wire=materialDict['Copper'], get=False):
		rc, lc, N = params
		result = V_bus**2/wireResistance(params)
		if get:
			return result
		return power - result

	def numTurnsConstraint(params, numTurns=10000):
		rc, lc, N = params
		return numTurns - N

	def dimensionConstraint(params):
		rc, lc, N = params
		return lc - rc
	
	def wireResistance(params, mat_core=materialDict['MnZnFerrite'], mat_wire=materialDict['Copper']):
		rc, lc, N = params
		#R_m - resistance of wire material - Ohm*m
		#a_w - guage of wire - m^2
		return 2*pi*rc*N*mat_wire['resistivity'][0]/a_w

	def massConstraint(params, mass=0.08, mat_core=materialDict['MnZnFerrite'], mat_wire=materialDict['Copper'], get=False):
		rc, lc, N = params
		l_wire = 2*pi*rc*N
		result = (mat_core['density'][0]*pi*(rc**2)*lc + a_w*l_wire*mat_wire['density'][0])
		if get:
			return result
		return mass - result

	cons = [{'type': 'ineq', 'fun': massConstraint},
		{'type': 'ineq', 'fun': powerConstraint},
		{'type': 'ineq', 'fun': numTurnsConstraint},
		{'type': 'ineq', 'fun': dimensionConstraint}]

	#rc, lc, N
	x0 = [4e-3, 50e-3, 5000]

	bnds = ((10e-3, 100e-3), (50e-3, 90e-3), (1000, 10000))

	sol = minimize(objective, x0, method='SLSQP', constraints=cons, bounds=bnds)

	xOpt = sol.x
	paramOpt = -sol.fun
	status = 'Pass' if sol.status else 'Fail'
	print 'Status: {} - G: {} AWG, M: {} Am^2, Mass: {} g, Power: {} W, r_c: {} mm, l_c: {}m, N: {}'.format(status, guage, paramOpt,massConstraint(xOpt, get=True), powerConstraint(xOpt, get=True), xOpt[0]*1e3, xOpt[1], xOpt[2])
	allResults.append([guage, massConstraint(xOpt, get=True), powerConstraint(xOpt, get=True), paramOpt]+list(xOpt))
allResults = array(allResults).T

from mpl_toolkits.mplot3d import Axes3D
zPlots = {
	'Magnetic Dipole Moment [Am^2]': allResults[3],
	'Mass [g]': allResults[1],
	'Power [W]': allResults[2],
}
#gauge, massConstr, powerConstr, magMoment, r_c, l_c, N
for zTitle, zs in zPlots.items():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	xs = allResults[4]*1e3
	ys = allResults[5]*1e3
	values = allResults[0]
	ax.set_xlabel('Radius [mm]')
	ax.set_ylabel('Length [mm]')
	ax.set_zlabel(zTitle)
	ax.set_xlim3d(0,max(xs)*1.1)
	ax.set_ylim3d(0,max(ys)*1.1)
	p = ax.scatter3D(xs, ys, zs=zs, c=values, cmap='hot')
	
	fig.colorbar(p, ax=ax)
plt.show()
plt.pause(.001)
embed()
