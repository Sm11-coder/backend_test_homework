class InfoMessage:
    """Информационное сообщение о тренировке."""
    def get_message(self, training_type: str,
                    duration: float, distance: float,
                    speed: float, calories: float):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
        return f'''Тип тренировки: {self.training_type};
                Длительность: {self.duration:.3f} ч.;
                Дистанция: {self.distance:.3f} км;
                Ср. скорость: {self.speed:.3f} км/ч;
                Потрачено ккал: {self.calories:.3f}.'''


class Training:
    """Базовый класс тренировки."""
    # константы
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79
    M_IN_KM = 1000
    LEN_STEP = 0.65

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
        pass


class Running(Training):
    """Тренировка: бег."""
    SEC_IN_MIN = 60

    def get_spent_calories(self) -> float:
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.weight / self.M_IN_KM
                * (self.duration / self.SEC_IN_MIN))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    K_1 = 0.035
    K_2 = 0.029

    def __init__(self, action: int,
                 duration: float,
                 weight: float,
                 height: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        return ((self.K_1 * self.weight
                + self.get_mean_speed() ** 2
                / self.height)
                * self.K_2 * self.weight) * self.duration


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_types = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': Warning
    }
    training = workout_types[workout_type](*data)
    return training


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    return info.get_message()


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
