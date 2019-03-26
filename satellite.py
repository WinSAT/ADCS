class Satellite:
    def __init__(self,
        mass = 215,
        inertiaZ = 90,
        inertiaY = 60,
        orbitAlt = 700,
        slewRate = 30,
        pointingAcc = 0.1,
        surfaceArea = 2*1.5,
        deltaCOGCOPsolar = 0.3,
        coefReflectivity = 0.6,
        angleIncidence = 0,
        residualDipole = 1,
        atmosDensityRho = 1e-13,
        dragCoefCd = 2.0,
        surfAreaAero = 3,
        satVelocity = 7504,
        deltaCOPCOGaero = 0.2,
        marginFactor = 0,
        slewTime = 600,
        orbitalPeriod = 1482,
        yawRollAccuracy = 0.1):

        self.mass = mass
        self.inertia_z = inertiaZ
        self.inertia_y = inertiaY
        self.orbit_altitude = orbitAlt
        self.slew_rate = slewRate
        self.pointing_accuracy = pointingAcc
        self.surface_area = surfaceArea
        self.deltaCOGCOPsolar = deltaCOGCOPsolar
        self.coef_of_reflectivity = coefReflectivity
        self.angle_of_incidence = angleIncidence
        self.magnetic_dipole = residualDipole
        self.atmospheric_density_rho = atmosDensityRho
        self.drag_coefficient = dragCoefCd
        self.surface_area_aero = surfAreaAero
        self.satellite_velocity = satVelocity
        self.deltaCOPCOGaero = deltaCOPCOGaero
        self.margin_factor = marginFactor
        self.slew_time = slewTime
        self.orbital_period = orbitalPeriod
        self.yaw_roll_accuracy = yawRollAccuracy

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

