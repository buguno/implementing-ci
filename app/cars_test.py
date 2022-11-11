from faker import Faker

from app.cars import CarParams, CarService

faker = Faker()
sut = CarService()


def make_params() -> CarParams:
    return CarParams(
        brand=faker.word(),
        model=faker.word(),
        plate=faker.word()
    )


def test_should_return_correct_response_on_success_add_car():
    params = make_params()
    result = sut.add_car(params)
    assert result.brand == params.brand
    assert result.model == params.model
    assert result.plate == params.plate


def test_should_return_correct_response_on_success_get_all_cars():
    sut.reset_cars()
    params = make_params()
    sut.add_car(params)
    result = sut.get_all_cars()
    assert result.cars[0].brand == params.brand
    assert result.cars[0].model == params.model
    assert result.cars[0].plate == params.plate
