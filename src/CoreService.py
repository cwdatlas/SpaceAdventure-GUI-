import math

from src.Models.BaseCapsule import Capsule
from src.Models.BaseEngine import Engine
from src.Models.BaseTank import Tank


class Core:
    def __init__(self):
        print("initializing application")
        # initialize dictionary that holds rocket parts (rocket should be a class in a long term project)
        self.rocket = {"name": "First Rocket", "capsule": None, "tank": None, "engine": None}
        # Create a list of capsules to choose from
        self.capsules = {"Apollo": Capsule("Apollo", 11900, 3),
                         "Dragon": Capsule("Dragon", 12519, 4),
                         "Orion": Capsule("Orion", 10400, 4)}
        # Create a list of tanks to choose from
        self.tanks = {"small": Tank("small", 10000, 75000, 2.4),
                      "medium": Tank("medium", 27000, 400700, 3.7),
                      "large": Tank("large", 137000, 2077000, 10.1)}
        # Create a list of engines to choose from
        self.engines = {"F-1": Engine("F-1", 8400, 7770, 304, 3.7),
                        "Raptor": Engine("Raptor", 1600, 2690, 363, 1.3),
                        "RD-170": Engine("RD-170", 9750, 7900, 337, 3.8)}
        # Set Delta V to 0
        self.delta_v = 0
        # set game status
        self.game_running = False

    def get_rocket_mass(self):
        mass = (self.rocket["capsule"].mass +
                self.rocket["tank"].mass +
                self.rocket["engine"].mass +
                self.rocket["tank"].liquid_fuel)
        return mass

    def get_thrust(self):
        return self.rocket["engine"].thrust * 1000

    def get_thrust_to_weight(self):
        return self.get_thrust() / (self.get_rocket_mass() * 9.81)

    def engine_mountable(self):
        return self.rocket["tank"] is None

    def set_engines(self, chosen_engine):
        self.rocket["engine"] = self.engines[chosen_engine]

    def set_capsule(self, capsule):
        self.rocket["capsule"] = self.capsules[capsule]

    def set_tank(self, tank):
        self.rocket["tank"] = self.tanks[tank]

    def rocket_launchable(self):
        return (self.rocket["capsule"] is not None
                and self.rocket["tank"] is not None
                and self.rocket["engine"] is not None)

    def calculate_delta_v(self):
        isp = self.rocket["engine"].isp
        g = 9.81  # Gravity at earths surface
        m = self.get_rocket_mass()
        mf = m - self.rocket["tank"].liquid_fuel
        self.delta_v = isp * g * math.log(m / mf)

    def made_to_orbit(self):
        self.calculate_delta_v()
        return self.delta_v > 7000
