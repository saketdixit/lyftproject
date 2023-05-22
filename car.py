from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
from datetime import date

class Car(ABC):
    def __init__(self, engine: Engine, battery: Battery, current_date: date, last_service_date: date, 
                 current_mileage: int = None, last_service_mileage: int = None, warning_light_on: bool = None):
        
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.warning_light_on = warning_light_on

        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() 
