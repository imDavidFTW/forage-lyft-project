from abc import ABC, abstractmethod
from servicable import Servicable
from engines.engine import Engine
from batteries.battery import Battery
from tires.tire import Tire

class Car(Servicable, ABC):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire
    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service():
            return True
        return False