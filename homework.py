class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type: str, duration: float, distance: float, speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories    

    def get_message(self) -> str:
        return f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}.'


class Training:
    """Базовый класс тренировки."""
    m_in_km: int = 1000
    len_step: int = 0
    training_type: str = ''

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
        return self.action * self.len_step * self.m_in_km

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(self.training_type, self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories()).get_message()


class Running(Training):
    """Тренировка: бег."""
    len_step: float = 0.65
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20 
    
    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)
        self.training_type = 'Running'

    def get_spent_calories(self) -> float:
        return (self.coeff_calorie_1 * self.get_mean_speed() - self.coeff_calorie_2) / self.m_in_km * self.duration * 60


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    len_step: float = 0.65
    cal_coef_1: float = 0.035
    cal_coef_2: float = 0.029

    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height
        self.training_type = 'SportsWalking'

    def get_spent_calories(self) -> float:
        return (self.cal_coef_1 * self.weight + (self.get_mean_speed**2 // self.height) * self.cal_coef_2 * self.weight) * self.duration * 60
        

class Swimming(Training):
    """Тренировка: плавание."""
    len_step: float = 1.38
    cal_coef_1:float = 1.1
    cal_coef_2:int = 2

    def __init__(self, action: int, duration: float, weight: float, length_pool: float, count_pool: float) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool
        self.training_type = 'Swimming'

    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.m_in_km / self.duration

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + self.cal_coef_1) * self.cal_coef_2 * self.weight


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
    info = Training.show_training_info()
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

