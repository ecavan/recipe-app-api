from django.test import TestCase

from app.calc import add, subtract

class CalcTests(TestCase):

    def test_add(self):
        self.assertEqual(add(3,8),11)


    def test_subtract(self):
        self.assertEqual(subtract(5,11),6)