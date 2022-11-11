from pydantic import BaseModel
from time import time


class CarParams(BaseModel):
    brand: str
    model: str
    plate: str


class CarResponse(BaseModel):
    brand: str
    model: str
    plate: str
    timestamp: int


class CarService():
    def __init__(self):
        self.cars = []

    def add_car(self, car: CarParams) -> CarResponse:
        new_car = CarResponse(
            brand=car.brand,
            model=car.model,
            plate=car.plate,
            timestamp=int(time())
        )

        self.cars.append(new_car.__dict__)
        return new_car

