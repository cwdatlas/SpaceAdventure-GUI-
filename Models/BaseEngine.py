class Engine():
    # Name of the part, like F-1
    name: str
    # in kg
    mass: int
    # in kn (kili Nuton)
    thrust: int
    # in seconds
    isp: int
    # in meters
    width: float

    def __init__(self, name, mass, thrust, isp, width):
        self.name = name
        self.mass = mass
        self.thrust = thrust
        self.isp = isp
        self.width = width
