import unittest
import math
import sys
import os

# Добавляем путь к корневой директории
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from geometry_lib import Circle
    from geometry_lib.shapes.base import calculate_area
except ImportError:
    # Альтернативный импорт для отладки
    from shapes.circle import Circle
    from shapes.base import calculate_area


class TestCircle(unittest.TestCase):

    def test_area_positive_radius(self):
        circle = Circle(5)
        expected_area = math.pi * 25
        self.assertAlmostEqual(circle.area(), expected_area)

    def test_area_zero_radius(self):
        circle = Circle(0)
        self.assertFalse(circle.is_valid())

    def test_area_negative_radius(self):
        circle = Circle(-1)
        self.assertFalse(circle.is_valid())

    def test_calculate_area_function(self):
        circle = Circle(3)
        expected_area = math.pi * 9
        self.assertAlmostEqual(calculate_area(circle), expected_area)

    def test_calculate_area_invalid_circle(self):
        circle = Circle(-1)
        with self.assertRaises(ValueError):
            calculate_area(circle)


if __name__ == '__main__':
    unittest.main()