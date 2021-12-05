from unittest.mock import Mock
from unittest import TestCase
from assertpy import assert_that
from modules.CarImpl import CarImpl
from modules.Car import Car


class TestCarImpl(TestCase):
    def test_car_fuel_ok(self) -> None:
        car = Car()
        car.needs_fuel = Mock(name="needs_fuel")
        car.needs_fuel.return_value = False
        car_impl = CarImpl(car)
        assert_that(car_impl.car_fuel_check_message()).is_equal_to("Fuel ok")

    def test_car_fuel_low(self) -> None:
        car = Car()
        car.needs_fuel = Mock(name="needs_fuel")
        car.needs_fuel.return_value = True
        car_impl = CarImpl(car)
        assert_that(car_impl.car_fuel_check_message()).is_equal_to("Low fuel level")

    def test_car_engine_temperature_too_low(self) -> None:
        car = Car()
        car.get_engine_temperature = Mock(name="get_engine_temperature")
        car.get_engine_temperature.return_value = 70
        car_impl = CarImpl(car)
        assert_that(car_impl.car_engine_temperature_message()
                    ).ends_with("too low")

    def test_car_engine_temperature_too_high(self) -> None:
        car = Car()
        car.get_engine_temperature = Mock(name="get_engine_temperature")
        car.get_engine_temperature.return_value = 110
        car_impl = CarImpl(car)
        assert_that(car_impl.car_engine_temperature_message()
                    ).ends_with("too high")

    def test_car_engine_temperature_message_ok(self) -> None:
        car = Car()
        car.get_engine_temperature = Mock(name="get_engine_temperature")
        car.get_engine_temperature.return_value = 100
        car_impl = CarImpl(car)
        assert_that(car_impl.car_engine_temperature_message()
                    ).ends_with("is ok")

    def test_car_set_destination(self) -> None:
        car = Car()
        trip_destination = "Gdansk"
        car.drive_to = Mock(name="drive_to")
        car.drive_to.return_value = trip_destination
        car_impl = CarImpl(car)
        assert_that(car_impl.car_set_destination(trip_destination)
                    ).is_equal_to(f'GPS is set to ${trip_destination}')
