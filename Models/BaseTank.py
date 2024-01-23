class Tank():
    name: str
    # in kg (specifically dry mass)
    mass: int
    # in kg (fuel mass)
    liquid_fuel: int
    # in meters
    width: float

    def __init__(self, name, mass, liquid_fuel, width):
        self.name = name
        self.mass = mass
        self.liquid_fuel =liquid_fuel
        self.width = width
