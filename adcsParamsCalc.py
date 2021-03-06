import math as m
import numpy as np
import satellite


#Constants
earthGravConst = 3.986e14 #Earth-Gravity Constant in m3/s2
earthRadius = 6378 #Radius of Earth in Km.
solarConst = 1367 #Solar Constant in [W/m2]
magmomentEarth = 7.96e15 #Magnetic moment of earth in [Tesla/m3]
rmsSINavg = 0.707 #Sinusoidal RMS average


FireSat = satellite.Satellite( 
        {"mass" : 215,
        "inertiaZ" : 90,
        "inertiaY" : 60,
        "orbitAlt" : 700,
        "slewRate" : 30,
        "pointingAcc" : 0.1,
        "surfaceArea" : 2*1.5,
        "deltaCOGCOPsolar" : 0.3,
        "coefReflectivity" : 0.6,
        "angleIncidence" : 0,
        "residualDipole" : 1,
        "atmosDensityRho" : 1e-13,
        "dragCoefCd" : 2.0,
        "surfAreaAero" : 3,
        "satVelocity" : 7504,
        "deltaCOPCOGaero" : 0.2,
        "marginFactor" : 0,
        "slewTime" : 600,
        "orbitalPeriod" : 1482,
        "yawRollAccuracy" : 0.1 })

WinSAT = {
"mass": 30, #Mass [kg]
"inertia_z": 0, #Moment of Inertia [Kg.m2] Ix = Iz
"inertia_y" : 0, #Moment of Inertia [Kg.m2]
"orbit_altitude" : 0, #Alt [Km], Circular Orbit
"slew_rate" : 0, #0.1 [deg/s]
"pointing_accuracy" : 0, #[deg]
"surface_area" : 0, #Surface area cross section of [2m by 1.5m]
"deltaCOMCOP": 0, #Center of mass to Center of pressure difference in [m]
"coef_of_reflectivity": 0, #Coefficent of Reflectivity
"angle_of_incidence": 0, #Angle of incidence of the sun in [deg]
"magnetic_dipole": 0, #Spacecraft magnetic dipole [A.m2]
"atmospheric_density_rho": 0, #Atmospheric density Rho [kg/m3]
"drag_coefficient": 2.0, #Drag Coefficient usually between 2 and 2.5
"surface_area_aero":3, #Surface Area in [m2]
"satellite_velocity": 7504, #Velocity of sat in [m/s]
"deltaCOPCOGaero": 0.2, #Center of gravity to Center of aerodynamic pressure difference in [m]
"margin_factor": 0, #Margin factor for required counter torque needed to counteract disturbances
"slew_time": 600, #Slew time in [s]
"orbital_period": 5679 #Orbital period in [s]
}
#REFER TO TABLE 11.9A IN SMAD FOR LIST OF EQUATIONS

"""MAX GRAVITY TORQUE GENERATED BY GRAVITY GRADIENT DISTURBANCE"""

def GG(sat):
    orbitRadius = (earthRadius+sat.orbit_altitude)*1000
    T = ((3*earthGravConst)/(2*((orbitRadius)**3))) * (sat.inertia_z - sat.inertia_y) * (np.sin(np.deg2rad(2*sat.slew_rate)))
    return T
print ("Max torque generated by gravity gradient: " + str(GG(FireSat)) + " N.m")

"""MAX GRAVITY TORQUE GENERATED BY SOLAR RADIATION DISTURBANCE"""
def solarRad(sat):
    speedLight = 3e8 # speed of light in [m/s]
    F = (solarConst/speedLight) * (sat.surface_area) * (1+sat.coef_of_reflectivity) * (np.cos(np.deg2rad(sat.angle_of_incidence)))
    TsolarPressure = F*(sat.deltaCOGCOPsolar)
    return TsolarPressure
print ("Max torque generate by solar radiation is: " + str(solarRad(FireSat)) + " N.m")

"""MAX GRAVITY TORQUE GENERATED BY MAGNETIC FIELD DISTURBANCE"""
def magTorque(sat):
    orbitRadius = (earthRadius+sat.orbit_altitude)*1000
    earthMagfield = 2*(magmomentEarth/(orbitRadius**3)) #For polar orbits-- half this for equatorial orbit
    Tmag = earthMagfield*sat.magnetic_dipole #Worst case polar mag field in [N.m]
    return Tmag
print ("Max torque generated by magnetic field is: " + str(magTorque(FireSat)) + " N.m")

"""MAX GRAVITY TORQUE GENERATED BY AERODYNAMIC DISTURBANCE"""
def Aero(sat):
    F = 0.5*(sat.atmospheric_density_rho*sat.drag_coefficient*sat.surface_area_aero*(sat.satellite_velocity)**2)
    Taero = F * (sat.deltaCOPCOGaero)
    return Taero
print ("Max torque generated by aerodynamic pressure is: " + str(Aero(FireSat)) + " N.m")

""" SIZING ADCS HARDWARE """

print("-------- SIZING ADCS HARDWARE ---------")

#Constants
a = GG(FireSat)
b = solarRad(FireSat)
c = magTorque(FireSat)
d = Aero(FireSat)

#List of disturbances
disturbanceList = [a,b,c,d]
greatestdisurbanceTd = max(disturbanceList)

"""Calculates torque required to counter balance the effect of a disturbance"""
def requiredcounterTorque(sat):
    Trw = greatestdisurbanceTd*sat.margin_factor
    return Trw
print ("Counter torque required from reaction wheel due to greatest disturbance is: " + str(requiredcounterTorque(FireSat)) + " N.m")


""" Calculates torque required to slew to a required angle """
def slewTorque(sat):
    Tslew = (4*sat.slew_rate*(np.pi/180)*sat.inertia_z)/(sat.slew_time)**2
    return Tslew
print ("Counter torque required from reaction wheel to slew is: " + str(slewTorque(FireSat)) + " N.m")


"""Estimates the wheel momentum stored in reaction wheel for one orbital period"""
def momentumStorage(sat):
    wheelmomentumH = (greatestdisurbanceTd*sat.orbital_period*rmsSINavg)/(4)
    return wheelmomentumH
print ("Wheel momentum stored in one orbit is: " + str(momentumStorage(FireSat)) + " N.m.s")

"""Angular momentum required for a specific Roll and Yaw with a given degree accuracy"""
def requiredAngmomentum(sat):
    angularmomentumreq = (greatestdisurbanceTd*sat.orbital_period)/(sat.yaw_roll_accuracy*(np.pi/180))
    return angularmomentumreq
print ("Angular momentum required to Yaw or Roll with specific accuracy is: " + str(requiredAngmomentum(FireSat)) + " N.m.s")

"""Magnetic torquer ability to counteract worst case disturbance during momentum dumping"""
def magneticTorquer(sat):
    orbitRadius = (earthRadius+sat.orbit_altitude)*1000
    earthMagfield = 2*(magmomentEarth/(orbitRadius**3))
    magDiploleD = (greatestdisurbanceTd/earthMagfield) + 3
    return magDiploleD
print("the magnetic torquing ability of the magnetorquer is: "+ str(magneticTorquer(FireSat)) + " N.m.s")


