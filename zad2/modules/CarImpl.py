from modules.Car import Car


class CarImpl:
    def __init__(self, car: Car) -> None:
        self._car = car

    def car_fuel_check_message(self) -> str:
        if self._car.needs_fuel():
            return "Low fuel level"
        else:
            return "Fuel ok"

    def car_engine_temperature_message(self) -> str:
        engine_temperature = self._car.get_engine_temperature()
        if engine_temperature < 90:
            return "Temperature of the engine is too low"
        elif engine_temperature > 100:
            return "Temperature of the engine is too high"
        else:
            return "Temperature of engine is ok"

    def car_set_destination(self, destination: str) -> str:
        return f'GPS is set to ${self._car.drive_to(destination)}'
