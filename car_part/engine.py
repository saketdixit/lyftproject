from car import Car
from engine.willoughby_engine import WilloughbyEngine
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine

class Engine(Car):
    def __init__(self) -> None:
        
    def needs_service(self) -> bool:
        return super().needs_service()