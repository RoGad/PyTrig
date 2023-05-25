import unittest
from trig import app

class Test(unittest.TestCase):

    def test_sin(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'sin', 'num_2': 60, 'num_3': 1, 'num_4': 'on'})
            self.assertIn(b'-0.3', response.data)

    def test_cos(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'cos', 'num_2': 60, 'num_3': 3, 'num_4': 'on'})
            self.assertIn(b'-0.952', response.data)

    def test_tan(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'tan', 'num_2': 60, 'num_3': 4, 'num_4': 'on'})
            self.assertIn(b'0.32', response.data)

    def test_ctg(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'ctg', 'num_2': 0, 'num_3': 0, 'num_4': 'None'})
            self.assertIn(bytes("нет решения", "utf-8"), response.data)

    def test_random_name(self):
        with app.test_client() as client:
            response = client.post('/', data={'num_1': 'dlbfksdjf', 'num_2': 0, 'num_3': 0, 'num_4': 'None'})
            self.assertIn(bytes("такой функции нет", "utf-8"), response.data)


if __name__ == '__main__':
    unittest.main()
