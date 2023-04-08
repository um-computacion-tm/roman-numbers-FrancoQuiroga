import unittest
from decimaltoroman import decimal_to_roman
# Tests del programa Decimal a Romanos
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
#Tests del programa Romano a Decimal
from romantodecimal import roman_to_decimal
class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)
    def test_II(self):
        resultado = roman_to_decimal('II')
        self.assertEqual(resultado, 2)
    def test_III(self):
        resultado = roman_to_decimal('III')
        self.assertEqual(resultado, 3)
    def test_V(self):
        resultado = roman_to_decimal('V')
        self.assertEqual(resultado, 5)
    def test_X(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)
    def test_VI(self):
        resultado = roman_to_decimal('VI')
        self.assertEqual(resultado, 6)
    def test_VII(self):
        resultado = roman_to_decimal('VII')
        self.assertEqual(resultado, 7)
    def test_IV(self):
        resultado = roman_to_decimal('IV')
        self.assertEqual(resultado, 4)
    def test_IX(self):
        resultado = roman_to_decimal('IX')
        self.assertEqual(resultado, 9)
    def test_XI(self):
        resultado = roman_to_decimal('XI')
        self.assertEqual(resultado, 11)
    def test_XX(self):
        resultado = roman_to_decimal('XX')
        self.assertEqual(resultado, 20)
    def test_XXV(self):
        resultado = roman_to_decimal('XXV')
        self.assertEqual(resultado, 25)
    def test_XXVIII(self):
        resultado = roman_to_decimal('XXVIII')
        self.assertEqual(resultado, 28)
    def test_XXIX(self):
        resultado = roman_to_decimal('XXIX')
        self.assertEqual(resultado, 29)
    def test_XLV(self):
        resultado = roman_to_decimal('XLV')
        self.assertEqual(resultado, 45)
    def test_XLIX(self):
        resultado = roman_to_decimal('XLIX')
        self.assertEqual(resultado, 49)
    def test_LXIV(self):
        resultado = roman_to_decimal('LXIV')
        self.assertEqual(resultado, 64)
    def test_XCIX(self):
        resultado = roman_to_decimal('XCIX')
        self.assertEqual(resultado, 99)
    def test_CLIX(self):
        resultado = roman_to_decimal('CLIX')
        self.assertEqual(resultado, 159)
    def test_CXCIX(self):
        resultado = roman_to_decimal('CXCIX')
        self.assertEqual(resultado, 199)
    def test_CD(self):
        resultado = roman_to_decimal('CD')
        self.assertEqual(resultado, 400)
    def test_CM(self):
        resultado = roman_to_decimal('CM')
        self.assertEqual(resultado, 900)

if __name__ == '__main__':
    unittest.main()
if __name__ == '__main__':
    if __name__ == '__main__':
        print("decimal to roman")
        unittest.main()
