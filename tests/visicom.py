import pytest
from pydantic.error_wrappers import ValidationError

from visicom import Visicom


@pytest.mark.parametrize(
    "token",
    [
        "414eb149c5b857fb898dbaf80bcb1de",
        "414eb149c5b857fb898dbaf80bcb1de11f",
        None,
        123,
    ],
)
def test_instantiate_failure(token):
    with pytest.raises(ValidationError):
        Visicom(token=token)


@pytest.mark.parametrize(
    "invalid_key", ["414eb149c5b857fb898dbaf80bcb1dsf"],
)
def test_geocode_method_failure(invalid_key):
    address = "Київська область, Мостище, вул. Слобідська, 1"
    with pytest.raises(ValueError):
        api = Visicom(token=invalid_key)
        api.geocode(address)


def test_geocode_method_success():
    pass


def test_fetch_method():
    pass