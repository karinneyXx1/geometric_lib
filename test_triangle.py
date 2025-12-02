import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    """Тесты для модуля triangle.py"""
    
    def test_area_normal(self):
        """Площадь треугольника с основанием 6 и высотой 4 должна быть 12"""
        res = area(6, 4)
        self.assertEqual(res, 12)
    
    def test_area_zero_base(self):
        """Площадь треугольника с нулевым основанием должна быть 0"""
        res = area(0, 10)
        self.assertEqual(res, 0)
    
    def test_area_zero_height(self):
        """Площадь треугольника с нулевой высотой должна быть 0"""
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_area_negative(self):
        """Площадь с отрицательными значениями должна возвращать результат"""
        # (-5 * 10) / 2 = -50 / 2 = -25
        res = area(-5, 10)
        self.assertEqual(res, -25)
    
    def test_perimeter_normal(self):
        """Периметр треугольника со сторонами 3, 4, 5 должен быть 12"""
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_perimeter_equilateral(self):
        """Периметр равностороннего треугольника должен быть утроенной стороной"""
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)
    
    def test_perimeter_zero(self):
        """Периметр с нулевыми сторонами должен быть 0"""
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter_negative(self):
        """Периметр с отрицательными сторонами должен возвращать результат"""
        # -3 + 4 + 5 = 6
        res = perimeter(-3, 4, 5)
        self.assertEqual(res, 6)
    
    def test_perimeter_invalid_triangle(self):
        """Периметр для несуществующего треугольника должен возвращать сумму"""
        # Исходная функция просто складывает числа
        # 1 + 2 + 10 = 13
        res = perimeter(1, 2, 10)
        self.assertEqual(res, 13)

