import math as m
import numpy as np


#Constants
earthGravConst = 3.986e14 #Earth-Gravity Constant in m3/s2
earthRadius = 6378 #Radius of Earth in Km.
solarConst = 1367 #Solar Constant in [W/m2]
magmomentEarth = 7.96e15 #Magnetic moment of earth in [Tesla/m3]


FireSat = {
            "M": 215, #Mass [kg]
            "Iz": 90, #Moment of Inertia [Kg.m2] Ix = Iz
            "Iy" : 60, #Moment of Inertia [Kg.m2]
            "orbitAlt" : 700, #Alt [Km], Circular Orbit
            "slewRate" : 1, #0.1 [deg/s]
            "pointingAcc" : 0.1, #[deg]
            "surfaceArea" : 2*1.5, #Surface area cross section of [2m by 1.5m]
            "deltaCOGCOPsolar": 0.3, #Center of gravity to Center of solar pressure difference in [m]
            "coefReflectivity": 0.6, #Coefficent of Reflectivity
            "angleIncidence": 0, #Angle of incidence of the sun in [deg]
            "residualDipole": 1, #Spacecraft magnetic dipole [A.m2]
            "atmosDensityRho": 1e-13, #Atmospheric density Rho [kg/m3]
            "dragCoefCd": 2.0, #Drag Coefficient usually between 2 and 2.5
            "surfAreaAero": 3, #Surface Area in [m2]
            "satVelocity": 7504,   #Velocity of sat in [m/s]
            "deltaCOPCOGaero": 0.2 #Center of gravity to Center of aerodynamic pressure difference in [m]
         }

WinSAT = {
            "M": 30, #Mass [kg]
            "Iz": 0, #Moment of Inertia [Kg.m2] Ix = Iz
            "Iy" : 0, #Moment of Inertia [Kg.m2]
            "orbitAlt" : 0, #Alt [Km], Circular Orbit
            "slewRate" : 0, #0.1 [deg/s]
            "pointingAcc" : 0, #[deg]
            "surfaceArea" : 0, #Surface area cross section of [2m by 1.5m]
            "deltaCOMCOP": 0, #Center of mass to Center of pressure difference in [m]
            "coefReflectivity": 0, #Coefficent of Reflectivity
            "angleIncidence": 0, #Angle of incidence of the sun in [deg]
            "residualDipole": 0, #Spacecraft magnetic dipole [A.m2]
            "atmosDensityRho": 0, #Atmospheric density Rho [kg/m3]
            "dragCoefCd": 2.0, #Drag Coefficient usually between 2 and 2.5
            "surfAreaAero":3, #Surface Area in [m2]
            "satVelocity": 7504, #Velocity of sat in [m/s]
            "deltaCOPCOGaero": 0.2 #Center of gravity to Center of aerodynamic pressure difference in [m]
    }

#REFER TO TABLE 11.9A IN SMAD FOR LIST OF EQUATIONS

"""MAX GRAVITY TORQUE GENERATED BY GRAVITY GRADIENT DISTURBANCE"""

def GG(sat):
    orbitRadius = (earthRadius+sat['orbitAlt'])*1000
    T = ((3*earthGravConst)/(2*((orbitRadius)**3))) * (sat["Iz"] - sat["Iy"]) * (np.sin(np.deg2rad(2*sat["slewRate"])))
    return T

print ("Max torque generated by gravity gradient: " + str(GG(FireSat)) + " N.m")

"""MAX GRAVITY TORQUE GENERATED BY SOLAR RADIATION DISTURBANCE"""
def solarRad(sat):
    speedLight = 3e8 # speed of light in [m/s]
    F = (solarConst/speedLight) * (sat["surfaceArea"]) * (1+sat["coefReflectivity"]) * (np.cos(np.deg2rad(sat["angleIncidence"])))
    TsolarPressure = F*(sat["deltaCOGCOPsolar"])
    return TsolarPressure

print ("Max torque generate by solar radiation is: " + str(solarRad(FireSat)) + " N.m")

"""MAX GRAVITY TORQUE GENERATED BY MAGNETIC FIELD DISTURBANCE"""
def magTorque(sat):
    orbitRadius = (earthRadius+sat['orbitAlt'])*1000
    earthMagfield = 2*(magmomentEarth/(orbitRadius**3)) #For polar orbits-- half this for equatorial orbit
    Tmag = earthMagfield*sat["residualDipole"] #Worst case polar mag field in [N.m]
    return Tmag

print ("Max torque generated by magnetic field is: " + str(magTorque(FireSat)) + " N.m")

"""MAX GRAVITY TORQUE GENERATED BY AERODYNAMIC DISTURBANCE"""
def Aero(sat):
    F = 0.5*(sat["atmosDensityRho"]*sat["dragCoefCd"]*sat["surfAreaAero"]*(sat["satVelocity"])**2)
    Taero = F * (sat["deltaCOPCOGaero"])
    return Taero

print ("Max torque generated by aerodynamic pressure is: " + str(Aero(FireSat)) + " N.m")
