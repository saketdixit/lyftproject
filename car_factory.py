from datetime import date
from car import Car
from car_part.battery import Battery
from car_part.engine import Engine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory():
    def __init__(self) -> None:
        pass

    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        calliope = Car(engine, battery, current_date, last_service_date, current_mileage, last_service_mileage)

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        glissade = Car(engine, battery, current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        palindrome = Car(engine, battery, current_date, last_service_date, warning_light_on)

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        rorshach = Car(engine, battery, current_date, last_service_date, current_mileage, last_service_mileage)

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        thovex = Car(engine, battery, current_date, last_service_date, current_mileage, last_service_mileage)