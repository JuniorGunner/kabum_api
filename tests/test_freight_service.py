import unittest
from services.freight_service import FreightService

class TestFreightService(unittest.TestCase):
    def setUp(self):
        self.service = FreightService()

    def test_valid_freight_calculation(self):
        # Teste com dados válidos
        data = {"dimensao": {"altura": 100, "largura": 50}, "peso": 500}
        result = self.service.calculate_freight(data)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)


    def test_invalid_dimensions(self):
        # Teste com dimensões inválidas
        data = {"dimensao": {"altura": 300, "largura": 50}, "peso": 500}
        result = self.service.calculate_freight(data)
        self.assertEqual(len(result), 0)


    def test_negative_weight(self):
        # Teste com peso negativo
        data = {"dimensao": {"altura": 100, "largura": 50}, "peso": -10}
        result = self.service.calculate_freight(data)
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
