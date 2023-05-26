from car_part.tires import Tires
from utils import add_years_to_date


class OctoprimeTires(Tires):
    def __init__(self, tire_wear: list):
        for i in range(3):
            self.tire_wear[i] = tire_wear[i]

    def needs_service(self) -> bool:
        sum = 0
        for i in range(3):
            sum += self.tire_wear[i]
        return (sum >= 3)
            