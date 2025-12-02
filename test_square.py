import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    """Тесты для модуля square.py"""
    
    def test_area_normal(self):
        """Площадь квадрата со стороной 4 должна быть 16"""
        res = area(4)
        self.assertEqual(res, 16)
    
    def test_area_zero(self):
        """Площадь квадрата со стороной 0 должна быть 0"""
        res = area(0)
        self.assertEqual(res, 0)
    
    def test_area_one(self):
        """Площадь квадрата со стороной 1 должна быть 1"""
        res = area(1)
        self.assertEqual(res, 1)
    
    def test_area_negative(self):
        """Площадь с отрицательной стороной должна возвращать положительное значение"""
        # (-5) * (-5) = 25
        res = area(-5)
        self.assertEqual(res, 25)
    
    def test_perimeter_normal(self):
        """Периметр квадрата со стороной 4 должен быть 16"""
        res = perimeter(4)
        self.assertEqual(res, 16)
    
    def test_perimeter_zero(self):
        """Периметр квадрата со стороной 0 должен быть 0"""
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_one(self):
        """Периметр квадрата со стороной 1 должен быть 4"""
        res = perimeter(1)
        self.assertEqual(res, 4)
    
    def test_perimeter_negative(self):
        """Периметр с отрицательной стороной должен возвращать положительное значение"""
        # 4 * (-5) = -20
        res = perimeter(-5)
        self.assertEqual(res, -20)

