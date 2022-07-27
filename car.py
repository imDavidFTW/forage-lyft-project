from abc import ABC, abstractmethod
from servicable import Servicable
from engines.engine import Engine
from batteries.battery import Battery

class Car(Servicable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        return False