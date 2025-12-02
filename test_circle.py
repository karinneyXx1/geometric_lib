import unittest
import math
from circle import area, perimeter

class CircleTestCase(unittest.TestCase):
    """Тесты для модуля circle.py"""
    
    def test_area_normal(self):
        """Площадь круга радиусом 5 должна быть примерно 78.5398"""
        res = area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_area_zero(self):
        """Площадь круга радиусом 0 должна быть 0"""
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area_one(self):
        """Площадь круга радиусом 1 должна быть π"""
        res = area(1)
        self.assertAlmostEqual(res, math.pi, places=5)
    
    def test_area_negative(self):
        """Площадь с отрицательным радиусом должна возвращать положительное значение"""
        # (-5)² = 25, умноженное на π дает положительное число
        res = area(-5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_perimeter_normal(self):
        """Длина окружности радиусом 5 должна быть примерно 31.4159"""
        res = perimeter(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(res, expected, places=5)
    
    def test_perimeter_zero(self):
        """Длина окружности радиусом 0 должна быть 0"""
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_one(self):
        """Длина окружности радиусом 1 должна быть 2π"""
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi, places=5)
    
    def test_perimeter_negative(self):
        """Периметр с отрицательным радиусом должен возвращать отрицательное значение"""
        # 2 * π * (-5) = отрицательное число
        res = perimeter(-5)
        expected = 2 * math.pi * (-5)  # Отрицательное значение
        self.assertAlmostEqual(res, expected, places=5)

