from tests import TestCase

from nhtsa.data import Car


class TestCar(TestCase):
    def test_create(self):
        car1 = Car(2016, 'Honda', 'Accord')
        car2 = Car(2016, 'Honda')
        car3 = Car(2016)

        self.assertIsNotNone(car1)
        self.assertEqual(car1.year, 2016)
        self.assertEqual(car1.make, 'Honda')
        self.assertEqual(car1.model, 'Accord')
        self.assertTrue(car1.is_complete)

        self.assertIsNotNone(car2)
        self.assertEqual(car2.year, 2016)
        self.assertEqual(car2.make, 'Honda')
        self.assertIsNone(car2.model)
        self.assertFalse(car2.is_complete)

        self.assertIsNotNone(car3)
        self.assertEqual(car3.year, 2016)
        self.assertIsNone(car3.make)
        self.assertIsNone(car3.model)
        self.assertFalse(car3.is_complete)

    def test_raises_invalid_year(self):
        self.assertRaises(AttributeError, Car, '2016')
