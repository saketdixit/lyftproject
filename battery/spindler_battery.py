from abc import ABC
from battery import Battery

class SpindlerBattery(ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year = self.last_service_date.year + 4)
        return service_threshold_date < self.current_date