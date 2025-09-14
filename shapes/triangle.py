from .base import Shape
import math


class Triangle(Shape):
    """Класс для представления треугольника"""

    def __init__(self, a: float, b: float, c: float):
        """
        Инициализирует треугольник

        Args:
            a, b, c: Стороны треугольника (должны быть положительными)
        """
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """Вычисляет площадь треугольника по формуле Герона"""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        """Вычисляет периметр треугольника"""
        return self.a + self.b + self.c

    def is_valid(self) -> bool:
        """Проверяет, является ли треугольник валидным"""
        sides = sorted([self.a, self.b, self.c])
        return (self.a > 0 and self.b > 0 and self.c > 0 and
                sides[0] + sides[1] > sides[2])

    def is_right_triangle(self, tolerance: float = 1e-6) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным

        Args:
            tolerance: Допустимая погрешность для сравнения с плавающей точкой

        Returns:
            bool: True если треугольник прямоугольный
        """
        if not self.is_valid():
            return False

        sides = sorted([self.a, self.b, self.c])
        # Проверяем теорему Пифагора
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < tolerance

    def __repr__(self):
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"