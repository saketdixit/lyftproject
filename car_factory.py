from datetime import date
from car import Car

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory():
    def __init__(self) -> None:
        pass

    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires( tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = CarriganTires( tire_wear)
        car = Car(engine, battery, tires)
        return car
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear: list) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(tire_wear)
        car = Car(engine, battery, tires)
        return car

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires( tire_wear)
        car = Car(engine, battery, tires)
        return car

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires( tire_wear)
        car = Car(engine, battery, tires)
        return car