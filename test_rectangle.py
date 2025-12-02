import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    """Тесты для модуля rectangle.py"""
    
    def test_area_normal(self):
        """Площадь прямоугольника 4x5 должна быть 20"""
        res = area(4, 5)
        self.assertEqual(res, 20)
    
    def test_area_square(self):
        """Площадь квадрата 10x10 должна быть 100"""
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_area_zero(self):
        """Площадь прямоугольника с нулевой стороной должна быть 0"""
        res = area(10, 0)
        self.assertEqual(res, 0)
        res = area(0, 10)
        self.assertEqual(res, 0)
    
    def test_area_negative(self):
        """Площадь с отрицательными сторонами должна возвращать положительное значение"""
        # Умножение отрицательных чисел дает положительный результат
        res = area(-5, 10)
        self.assertEqual(res, -50)  # -5 * 10 = -50
    
    def test_perimeter_normal(self):
        """Периметр прямоугольника 4x5 должен быть 18"""
        res = perimeter(4, 5)
        self.assertEqual(res, 18)
    
    def test_perimeter_square(self):
        """Периметр квадрата 10x10 должен быть 40"""
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    
    def test_perimeter_zero(self):
        """Периметр с нулевыми сторонами должен быть 0"""
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter_negative(self):
        """Периметр с отрицательными сторонами должен возвращать результат"""
        # 2 * (-5 + 10) = 2 * 5 = 10
        res = perimeter(-5, 10)
        self.assertEqual(res, 10)
