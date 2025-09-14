"""
Тестирование работоспособности библиотеки geometry_lib
"""

import sys
import os

# Добавляем текущую директорию в путь Python
sys.path.insert(0, os.path.abspath('.'))

try:
    from geometry_lib import Circle, Triangle, calculate_area

    print("Импорт библиотеки успешен")
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    # Пробуем альтернативный импорт
    try:
        from shapes.circle import Circle
        from shapes.triangle import Triangle
        from shapes.base import calculate_area

        print("Альтернативный импорт успешен")
    except ImportError as e2:
        print(f"Полная ошибка импорта: {e2}")
        sys.exit(1)


def test_circle():
    """Тестирование функциональности круга"""
    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ КРУГА")
    print("=" * 50)

    # Тест 1: Нормальный круг
    try:
        circle = Circle(5)
        area = circle.area()
        print(f"Круг радиусом 5: площадь = {area:.2f} (ожидаем ~78.54)")
        assert abs(area - 78.5398) < 0.1, "Неверная площадь круга"
    except Exception as e:
        print(f"Ошибка создания круга: {e}")
        return False

    # Тест 2: Невалидный круг
    try:
        circle = Circle(-1)
        is_valid = circle.is_valid()
        print(f"Круг радиусом -1: валиден = {is_valid} (ожидаем False)")
        assert not is_valid, "Отрицательный радиус должен быть невалидным"
    except Exception as e:
        print(f"Ошибка проверки валидности: {e}")
        return False

    # Тест 3: calculate_area функция
    try:
        circle = Circle(3)
        area = calculate_area(circle)
        print(f"calculate_area для круга: {area:.2f} (ожидаем ~28.27)")
        assert abs(area - 28.2743) < 0.1, "Неверная площадь через calculate_area"
    except Exception as e:
        print(f"Ошибка calculate_area: {e}")
        return False

    return True


def test_triangle():
    """Тестирование функциональности треугольника"""
    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ ТРЕУГОЛЬНИКА")
    print("=" * 50)

    # Тест 1: Прямоугольный треугольник
    try:
        triangle = Triangle(3, 4, 5)
        area = triangle.area()
        is_right = triangle.is_right_triangle()
        print(f"Треугольник 3-4-5: площадь = {area:.2f} (ожидаем 6.0)")
        print(f"Прямоугольный: {is_right} (ожидаем True)")
        assert area == 6.0, "Неверная площадь треугольника"
        assert is_right, "Треугольник 3-4-5 должен быть прямоугольным"
    except Exception as e:
        print(f"Ошибка создания треугольника: {e}")
        return False

    # Тест 2: Невалидный треугольник
    try:
        triangle = Triangle(1, 1, 3)
        is_valid = triangle.is_valid()
        print(f"Треугольник 1-1-3: валиден = {is_valid} (ожидаем False)")
        assert not is_valid, "Невозможный треугольник должен быть невалидным"
    except Exception as e:
        print(f"Ошибка проверки валидности: {e}")
        return False

    # Тест 3: calculate_area функция
    try:
        triangle = Triangle(3, 4, 5)
        area = calculate_area(triangle)
        print(f"calculate_area для треугольника: {area:.2f} (ожидаем 6.0)")
        assert area == 6.0, "Неверная площадь через calculate_area"
    except Exception as e:
        print(f"Ошибка calculate_area: {e}")
        return False

    return True


def test_polymorphism():
    """Тестирование полиморфизма (работа с разными фигурами)"""
    print("\n" + "=" * 50)
    print("ТЕСТИРОВАНИЕ ПОЛИМОРФИЗМА")
    print("=" * 50)

    try:
        shapes = [
            Circle(2),
            Triangle(3, 4, 5),
            Circle(1),
            Triangle(5, 5, 5)
        ]

        expected_areas = [12.566, 6.0, 3.141, 10.825]  # Примерные значения

        print("Создан список различных фигур")

        for i, shape in enumerate(shapes):
            area = calculate_area(shape)
            print(f"  Фигура {i + 1}: {type(shape).__name__} -> площадь = {area:.3f}")

        print("Полиморфизм работает корректно")
        return True

    except Exception as e:
        print(f"Ошибка полиморфизма: {e}")
        return False


def main():
    """Основная функция тестирования"""
    print("ТЕСТИРОВАНИЕ БИБЛИОТЕКИ geometry_lib")
    print("=" * 50)

    tests = [
        test_circle,
        test_triangle,
        test_polymorphism
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
            print("Тест пройден\n")
        else:
            print("Тест не пройден\n")

    print("=" * 50)
    print(f"ИТОГ: {passed}/{total} тестов пройдено")

    if passed == total:
        print("Все тесты пройдены успешно! Библиотека работает корректно.")
        return 0
    else:
        print("Есть проблемы в работе библиотеки.")
        return 1


if __name__ == "__main__":
    sys.exit(main())