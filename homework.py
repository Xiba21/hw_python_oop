class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        type_tr = f'Тип тренировки: {self.training_type}; '
        dur = f'Длительность: {self.duration:.3f} ч.; '
        dist = f'Дистанция: {self.distance:.3f} км; '
        avg_speed = f'Ср. скорость: {self.speed:.3f} км/ч; '
        cal_spent = f'Потрачено ккал: {self.calories:.3f}.'
        return type_tr + dur + dist + avg_speed + cal_spent


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: int = 1000
    LEN_STEP: float = 0.65
    training_type: str = ''
    coeff_calorie_1: float = 0
    coeff_calorie_2: float = 0

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
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.training_type,
                           self.duration, self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    LEN_STEP = 0.65

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        self.training_type = 'Running'
        self.coeff_calorie_1 = 18
        self.coeff_calorie_2 = 20

    def get_spent_calories(self) -> float:
        a = self.coeff_calorie_1
        b = self.get_mean_speed()
        c = self.coeff_calorie_2
        d = self.weight
        e = self.M_IN_KM
        f = self.duration
        return (a * b - c) * d / e * f * 60


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    LEN_STEP = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        self.training_type = 'SportsWalking'
        self.coeff_calorie_1 = 0.035
        self.coeff_calorie_2 = 0.029

    def get_spent_calories(self) -> float:
        a = self.coeff_calorie_1
        b = self.weight
        c = self.get_mean_speed()**2
        d = self.height
        e = self.coeff_calorie_2
        f = self.weight
        g = self.duration
        return (a * b + (c // d) * e * f) * g * 60


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.training_type = 'Swimming'
        self.coeff_calorie_1 = 1.1
        self.coeff_calorie_2 = 2

    def get_mean_speed(self) -> float:
        a = self.length_pool
        b = self.count_pool
        c = self.M_IN_KM
        d = self.duration
        return a * b / c / d

    def get_spent_calories(self) -> float:
        a = self.get_mean_speed() + self.coeff_calorie_1
        b = self.coeff_calorie_2 * self.weight
        return a * b


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    to_do = {
        'RUN': Running,
        'WLK': SportsWalking,
        'SWM': Swimming
    }
    return to_do[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info().get_message()
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
