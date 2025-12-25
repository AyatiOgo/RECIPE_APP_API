from django.test import SimpleTestCase
from .calc import add

class CalcTest(SimpleTestCase):

    def test_calc(self):
        res = add(2, 5)

        return self.assertEqual(res, 7)
