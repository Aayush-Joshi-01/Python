class CelestialObject:

    def __init__(self, name, mass):
        self.name = name

        self.mass = mass

    def describe(self):
        return f"{self.name} has a mass of {self.mass} kg."


# Single Inheritance

class Star(CelestialObject):

    def __init__(self, name, mass, spectral_type):
        super().__init__(name, mass)

        self.spectral_type = spectral_type

    def describe(self):
        return f"{super().describe()} It is a {self.spectral_type} type star."


# Multilevel Inheritance

class Planet(Star):

    def __init__(self, name, mass, spectral_type, orbital_period):
        super().__init__(name, mass, spectral_type)

        self.orbital_period = orbital_period

    def describe(self):
        return f"{super().describe()} It orbits its star every {self.orbital_period} days."


# Hierarchical Inheritance

class Moon(CelestialObject):

    def __init__(self, name, mass, host_planet):
        super().__init__(name, mass)

        self.host_planet = host_planet

    def describe(self):
        return f"{super().describe()} It orbits the planet {self.host_planet}."


# Multiple Inheritance

class SpaceStation:

    def __init__(self, name, mass, country):
        self.name = name

        self.mass = mass

        self.country = country

    def describe(self):
        return f"{self.name} is a space station with a mass of {self.mass} kg, operated by {self.country}."


class OrbitingStation(CelestialObject, SpaceStation):

    def __init__(self, name, mass, country, orbital_period):
        CelestialObject.__init__(self, name, mass)

        SpaceStation.__init__(self, name, mass, country)

        self.orbital_period = orbital_period

    def describe(self):
        return f"{CelestialObject.describe(self)} It orbits every {self.orbital_period} days. Operated by {self.country}."


# Hybrid Inheritance

class Comet(CelestialObject):

    def __init__(self, name, mass, orbital_period, tail_length):
        super().__init__(name, mass)

        self.orbital_period = orbital_period

        self.tail_length = tail_length

    def describe(self):
        return f"{super().describe()} It has an orbital period of {self.orbital_period} days and a tail length of {self.tail_length} km."


# Creating objects of different classes to demonstrate inheritance

star = Star("Sun", 1.989e30, "G2V")

planet = Planet("Earth", 5.972e24, "G2V", 365.25)

moon = Moon("Moon", 7.342e22, "Earth")

space_station = OrbitingStation("ISS", 420000, "International", 92)

comet = Comet("Halley's Comet", 2.2e14, 2752, 24)

# Displaying descriptions

print(star.describe())

print(planet.describe())

print(moon.describe())

print(space_station.describe())

print(comet.describe())
