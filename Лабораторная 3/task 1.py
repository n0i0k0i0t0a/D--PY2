if __name__ == "__main__":

    class Car:
        def __init__(self, color: str, year: int, consumption: int, tank_volume: int, milage: int, type_: str):
            """
            Создание объекта и подготовка к работе
            :param color: Цвет автомобиля
            :param year: Год выпуска авто
            :param consumption: Потребление топлива
            :param tank_volume: Объем бензопака
            :param milage: Пробег
            """
            self.color = color
            self.year = year
            self.consumption = consumption
            self.tank_volume = tank_volume
            self.milage = milage
            self.type_ = type_
            self.engine_on = True

        def drive(self, distance: int) -> str:
            """
            Метод который описывает процесс вождения авто, годится и для легкового и для грузового автомобилей
            :param distance: Дистанция которую проехал автомобиль
            :return: Строку с описанием пути, который был пройден и количество оставшегося топлива
            """
            if not self.engine_on:
                raise ValueError("Двигатель не запущен.")
            if self.tank_volume / self.consumption * 100 < distance:
                raise ValueError("Малый запас топлива.")
            else:
                self.milage += distance
                self.tank_volume -= distance / 100 * self.consumption
            return f"Проехали {distance} км. Остаток топлива: {self.tank_volume} л."

        def __str__(self) -> str:
            return f"""
            Цвет автомобиля: {self.color}. 
            Год выпуска автомобиля: {self.year}. 
            Потребление топлива: {self.consumption}.
            Объем бензобака: {self.tank_volume}.
            Пробег: {self.milage},
            Тип: {self.type_}.
            """

        def __repr__(self) -> str:
            return f"""
            {self.__class__.__name__}
            (color={self.color!r}, 
            year={self.year!r},
            consumption={self.consumption},
            tank_volume={self.tank_volume},
            milage={self.milage},
            type={self.type_})
            """

    class Passenger(Car):
        def __init__(self, color, year, consumption, tank_volume, milage, type_, speed):
            super().__init__(color, year, consumption, tank_volume, milage, type_)
            self.speed = speed

        @staticmethod
        def by_the_car(valid_price: int, amount_of_funds: int) -> str:
            """
            Метод описывающий процесс покупки легкового автомобиля
            :param valid_price: Дейсвтвительная цена на автомобиль
            :param amount_of_funds: Количество имеющихся средств у покупателя
            :return: количество оставшихся средств у покупателя
            """
            if not isinstance(valid_price, int):
                raise TypeError('Действителяьная цена на втомобиль должна быть типа int')
            if not isinstance(amount_of_funds, int):
                raise TypeError('Количество имеющихся средств должно быть типа int')

            if valid_price > amount_of_funds:
                raise ValueError('Вы не можете приобрести данный автомобиль ввиду недостатка средств')
            amount_of_funds -= valid_price
            return f'Остаток ваших средств {amount_of_funds} $'

        def drive(self, distance) -> str:
            super().drive(distance)
            return f"Проехали {distance} км. Остаток топлива: {self.tank_volume} л."

        def __repr__(self):
            return f"{self.__class__.__name__}" \
                   f"(color={self.color!r}, " \
                   f"year={self.year!r}, " \
                   f"type={self.type_}," \
                   f"consumption={self.consumption!r}," \
                   f"speed={self.speed!r})"

    class Truck(Car):
        def __init__(self, color, year, consumption, tank_volume, milage,  type_, luggage):
            super().__init__(color, year, consumption, tank_volume, milage, type_)
            self.luggage = luggage

        @staticmethod
        def by_the_car(valid_price: int, amount_of_funds: int) -> str:
            """
            Метод описывающий процесс покупки грузового автомобиля
            :param valid_price: Дейсвтвительная цена на автомобиль
            :param amount_of_funds: Количество имеющихся средств у покупателя
            :return: количество оставшихся средств у покупателя
            """
            if not isinstance(valid_price, int):
                raise TypeError('Действителяьная цена на втомобиль должна быть типа int')
            if not isinstance(amount_of_funds, int):
                raise TypeError('Количество имеющихся средств должно быть типа int')

            if valid_price > amount_of_funds:
                raise ValueError('Вы не можете приобрести данный автомобиль ввиду недостатка средств')
            amount_of_funds -= valid_price
            return f'Остаток ваших средств {amount_of_funds} $'

        def drive(self, distance) -> str:
            super().drive(distance)
            self.engine_on = True
            return f"Проехали {distance} км. Остаток топлива: {self.tank_volume} л."

        def __repr__(self):
            return f"{self.__class__.__name__}" \
                   f"(color={self.color!r}, " \
                   f"year={self.year!r}, " \
                   f"type={self.type_}," \
                   f"consumption={self.consumption!r}," \
                   f"luggage={self.luggage!r})"


    truck = Truck(color='красный',
                  year=2002,
                  consumption=10,
                  tank_volume=40,
                  milage=0,
                  type_='Грузовой автомобиль',
                  luggage=100)
    path = truck.drive(distance=10)
    buy = truck.by_the_car(valid_price=1000, amount_of_funds=2000)
    print(truck)
    print(repr(truck))
    print(path)
    print(buy)


