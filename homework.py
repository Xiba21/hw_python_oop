from dataclasses import dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                + f'Длительность: {self.duration:.3f} ч.; '
                + f'Дистанция: {self.distance:.3f} км; '
                + f'Ср. скорость: {self.speed:.3f} км/ч; '
                + f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
<<<<<<< HEAD
=======
    training_type: str = ''
    COEFF_CALORIE_1: float = 0
    COEFF_CALORIE_2: float = 0
>>>>>>> 8f91d9b6d50f3a121fe85c2cdf42453a8953c6a1
    MINS_IN_HOUR: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('Определите get_spent_calories в %s.'
                                  + str(self.__class__.__name__))

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
<<<<<<< HEAD
        return InfoMessage(self.__class__.__name__,
=======
        return InfoMessage(self.training_type,
>>>>>>> 8f91d9b6d50f3a121fe85c2cdf42453a8953c6a1
                           self.duration, self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    LEN_STEP = 0.65
<<<<<<< HEAD
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 20

    def get_spent_calories(self) -> float:
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                * self.get_mean_speed()
                - self.CALORIES_MEAN_SPEED_SHIFT)
=======
    COEFF_CALORIE_1 = 18
    COEFF_CALORIE_2 = 20

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        self.training_type = 'Running'

    def get_spent_calories(self) -> float:
        return ((self.COEFF_CALORIE_1
                * self.get_mean_speed()
                - self.COEFF_CALORIE_2)
>>>>>>> 8f91d9b6d50f3a121fe85c2cdf42453a8953c6a1
                * self.weight / self.M_IN_KM
                * self.duration
                * self.MINS_IN_HOUR)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    LEN_STEP = 0.65
<<<<<<< HEAD
    CALORIES_WEIGHT_COEFF = 0.035
    CALORIES_MEAN_SPEED_COEFF = 0.029
=======
    COEFF_CALORIE_1 = 0.035
    COEFF_CALORIE_2 = 0.029
>>>>>>> 8f91d9b6d50f3a121fe85c2cdf42453a8953c6a1

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
<<<<<<< HEAD
        return ((self.CALORIES_WEIGHT_COEFF
                * self.weight
                + (self.get_mean_speed()**2
                   // self.height)
                * self.CALORIES_MEAN_SPEED_COEFF
=======
        return ((self.COEFF_CALORIE_1
                * self.weight
                + (self.get_mean_speed()**2
                   // self.height)
                * self.COEFF_CALORIE_2
>>>>>>> 8f91d9b6d50f3a121fe85c2cdf42453a8953c6a1
                * self.weight)
                * self.duration
                * self.MINS_IN_HOUR)


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
<<<<<<< HEAD
    CALORIES_MEAN_SPEED_SHIFT = 1.1
    CALORIES_MEAN_SPEED_MULTIPLIER = 2
=======
    COEFF_CALORIE_1 = 1.1
    COEFF_CALORIE_2 = 2
>>>>>>> 8f91d9b6d50f3a121fe85c2cdf42453a8953c6a1

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.length_pool
                * self.count_pool
                / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed()
<<<<<<< HEAD
                + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.CALORIES_MEAN_SPEED_MULTIPLIER
=======
                + self.COEFF_CALORIE_1)
                * self.COEFF_CALORIE_2
>>>>>>> 8f91d9b6d50f3a121fe85c2cdf42453a8953c6a1
                * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    to_do = {
        'RUN': Running,
        'WLK': SportsWalking,
        'SWM': Swimming
    }

    try:
        return to_do[workout_type](*data)
    except Exception(ValueError):
        raise ValueError(f'Тренировки {workout_type}у нас нет')


def main(training: Training) -> None:
    """Главная функция."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
