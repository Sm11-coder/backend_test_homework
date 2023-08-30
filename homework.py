class InfoMessage:
    """Информационное сообщение о тренировке."""
    def show_training_info(self):
        return InfoMessage(self)

    def __str__(self):
        return (
            f'''Тип тренировки: {self.training_type:.3f};
         Длительность: {self.duration:.3f} ч.;
         Дистанция: {self.get_distance():.3f} км;
         Ср. скорость: {self.get_speed():.3f} км/ч;
         Потрачено ккал: {self.get_spent_calories():.3f}.'''
        )


class Training:
    """Базовый класс тренировки."""
    # Константы
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
        return ((self.CALORIES_MEAN_SPEED_MULTIPLIER
                * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT)
                * self.weight / self.M_IN_KM
                * self.duration)

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""
    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


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
