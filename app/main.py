from http import HTTPStatus
from fastapi import FastAPI

from app.cars import CarParams, CarResponse, CarService


app = FastAPI()

car_service = CarService()

@app.post(
    '/car',
    responses={
        HTTPStatus.CREATED.value: {'model': CarResponse, 'description': 'car added'},
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {'description': 'Internal Server Error'}
    },
    status_code=HTTPStatus.CREATED,
    tags=['Cars']
)
def add_car(body: CarParams):
    return car_service.add_car(body)
