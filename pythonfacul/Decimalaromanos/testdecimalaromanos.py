import unittest
from decimaltoroman import decimal_to_roman
class TestDecimalToRoman(unittest.TestCase):
        def test_uno(self):
            # pre condicion
            ### NO HAY ###
            # proceso
            resultado = decimal_to_roman(1)
            # verificacion
            self.assertEqual(resultado, 'I')

        def test_diez(self):
            resultado = decimal_to_roman(10)
            self.assertEqual(resultado, 'X')

        def test_cinco(self):
            resultado = decimal_to_roman(5)
            self.assertEqual(resultado, 'V')

        def test_dos(self):
            resultado = decimal_to_roman(2)
            self.assertEqual(resultado, 'II')

        def test_tres(self):
            resultado = decimal_to_roman(3)
            self.assertEqual(resultado, 'III')
        def test_cientotres(self):
            resultado = decimal_to_roman(103)
            self.assertEqual(resultado,'CIII')
        def test_124(self):
            resultado = decimal_to_roman(124)
            self.assertEqual(resultado, 'CXXIV')
        def test_444(self):
            resultado = decimal_to_roman(444)
            self.assertEqual(resultado, 'CDXLIV')
        def test_555(self):
            resultado = decimal_to_roman(555)
            self.assertEqual(resultado, 'DLV')
        def test_999(self):
            resultado = decimal_to_roman(999)
            self.assertEqual(resultado, 'CMXCIX')

if __name__ == '__main__':
    if __name__ == '__main__':
        print("decimal to roman")
        unittest.main()
