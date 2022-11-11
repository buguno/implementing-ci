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
