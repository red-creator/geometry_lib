from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Абстрактный базовый класс для всех фигур"""

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры"""
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        """Проверяет, является ли фигура валидной"""
        pass


def calculate_area(shape: Shape) -> float:
    """
    Вычисляет площадь фигуры без знания типа в compile-time

    Args:
        shape: Объект фигуры, наследующий от Shape

    Returns:
        float: Площадь фигуры

    Raises:
        ValueError: Если фигура невалидна
    """
    if not shape.is_valid():
        raise ValueError("Фигура невалидна")
    return shape.area()