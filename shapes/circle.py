from .base import Shape
from math import pi


class Circle(Shape):
    """Класс для представления круга"""

    def __init__(self, radius: float):
        """
        Инициализирует круг

        Args:
            radius: Радиус круга (должен быть положительным)
        """
        self.radius = radius

    def area(self) -> float:
        """Вычисляет площадь круга"""
        return pi * self.radius ** 2

    def is_valid(self) -> bool:
        """Проверяет, является ли круг валидным"""
        return self.radius > 0

    def __repr__(self):
        return f"Circle(radius={self.radius})"