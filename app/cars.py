from time import time

from pydantic import BaseModel


class CarParams(BaseModel):
    brand: str
    model: str
    plate: str


class CarResponse(BaseModel):
    brand: str
    model: str
    plate: str
    timestamp: int


class GetAllCars(BaseModel):
    cars: list[CarResponse]


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

    def get_all_cars(self) -> GetAllCars:
        return GetAllCars(cars=self.cars)

    def reset_cars(self) -> None:
        self.cars = []
