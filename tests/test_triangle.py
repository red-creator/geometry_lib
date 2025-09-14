import unittest
import math
import sys
import os

# Добавляем путь к корневой директории
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from geometry_lib import Triangle
    from geometry_lib.shapes.base import calculate_area
except ImportError:
    # Альтернативный импорт для отладки
    from shapes.triangle import Triangle
    from shapes.base import calculate_area


class TestTriangle(unittest.TestCase):

    def test_area_valid_triangle(self):
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0
        self.assertAlmostEqual(triangle.area(), expected_area)

    def test_area_equilateral_triangle(self):
        triangle = Triangle(2, 2, 2)
        expected_area = math.sqrt(3)  # (√3/4)*a² = √3
        self.assertAlmostEqual(triangle.area(), expected_area, places=6)

    def test_is_valid_positive_sides(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_valid())

    def test_is_valid_negative_side(self):
        triangle = Triangle(-1, 2, 3)
        self.assertFalse(triangle.is_valid())

    def test_is_valid_impossible_triangle(self):
        triangle = Triangle(1, 1, 3)
        self.assertFalse(triangle.is_valid())

    def test_is_right_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_is_not_right_triangle(self):
        triangle = Triangle(2, 3, 4)
        self.assertFalse(triangle.is_right_triangle())

    def test_calculate_area_function(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)

    def test_calculate_area_invalid_triangle(self):
        triangle = Triangle(1, 1, 3)
        with self.assertRaises(ValueError):
            calculate_area(triangle)


if __name__ == '__main__':
    unittest.main()