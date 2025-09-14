import unittest
import os
import sys

# Добавляем корневую директорию в путь
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Функция для запуска всех тестов
def run_all_tests():
    """Запускает все тесты в папке tests"""
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(__file__))
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return result

# Импорты для удобства
from .test_circle import TestCircle
from .test_triangle import TestTriangle

__all__ = ['run_all_tests', 'TestCircle', 'TestTriangle']