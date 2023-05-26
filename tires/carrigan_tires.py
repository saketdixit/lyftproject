from car_part.tires import Tires
from utils import add_years_to_date


class CarriganTires(Tires):
    def __init__(self, tire_wear: list):
        for i in range(3):
            self.tire_wear[i] = tire_wear[i]

    def needs_service(self) -> bool:
        for i in range(3):
            if(self.tire_wear[i] >= 0.9):
                return True
        return False
            