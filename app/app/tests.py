from django.test import TestCase

from app.calc import add, sub


class CalcTests(TestCase):
    def test_add_numbers(self):
        '''
        Testcat
        '''
        self.assertEqual(add(3, 8), 11)

    def test_sub_numbers(self):
        self.assertEqual(sub(11, 3), 8)
