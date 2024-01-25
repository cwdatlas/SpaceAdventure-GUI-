class Capsule():
    name: str
    # in kg
    mass: int
    # Number of astronauts that can be aboard
    crew: int

    def __init__(self, name, mass, crew):
        self.name = name
        self.mass = mass
        self.crew = crew

