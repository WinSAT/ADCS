class Satellite:
    def __init__(self,param):

        self.mass = param["mass"]
        self.inertia_z = param["inertiaZ"]
        self.inertia_y = param["inertiaY"]
        self.orbit_altitude = param["orbitAlt"]
        self.slew_rate = param["slewRate"]
        self.pointing_accuracy = param["pointingAcc"]
        self.surface_area = param["surfaceArea"]
        self.deltaCOGCOPsolar = param["deltaCOGCOPsolar"]
        self.coef_of_reflectivity = param["coefReflectivity"]
        self.angle_of_incidence = param["angleIncidence"]
        self.magnetic_dipole = param["residualDipole"]
        self.atmospheric_density_rho = param["atmosDensityRho"]
        self.drag_coefficient = param["dragCoefCd"]
        self.surface_area_aero = param["surfAreaAero"]
        self.satellite_velocity = param["satVelocity"]
        self.deltaCOPCOGaero = param["deltaCOPCOGaero"]
        self.margin_factor = param["marginFactor"]
        self.slew_time = param["slewTime"]
        self.orbital_period = param["orbitalPeriod"]
        self.yaw_roll_accuracy = param["yawRollAccuracy"]

    def set_mass(self, mass):
        self.mass = mass
        return self

    def set_inertia_z(self, inertiaZ):
        self.inertia_z = inertiaZ
        return self

    def set_inertia_y(self, inertiaY):
        self.inertia_y = inertiaY
        return self

    def set_orbit_altitude(self, orbitAlt):
        self.orbit_altitude = orbitAlt
        return self

    def set_slew_rate(self, slewRate):
        self.slew_rate = slewRate
        return self

    def set_pointing_accuracy(self, pointingAcc):
        self.pointing_accuracy = pointingAcc
        return self

    def set_surface_area(self, surfaceArea):
        self.surface_area = surfaceArea
        return self

    def set_deltaCOGCOPsolar(self, deltaCOGCOPsolar):
        self.deltaCOGCOPsolar = deltaCOGCOPsolar
        return self

    def set_coef_of_reflectivity(self, coefReflectivity):
        self.coef_of_reflectivity = coefReflectivity
        return self

    def set_angle_of_incidence(self, angleIncidence):
        self.angle_of_incidence = angleIncidence
        return self

    def set_magnetic_dipole(self, magneticDipole):
        self.magnetic_dipole = magneticDipole
        return self

    def set_atmospheric_density_rho(self, atmosDensityRho):
        self.atmospheric_density_rho = atmosDensityRho
        return self



    def set_deltaCOPCOGaero(self, deltaCOPCOGaero):
        self.deltaCOPCOGaero = deltaCOPCOGaero
        return self

