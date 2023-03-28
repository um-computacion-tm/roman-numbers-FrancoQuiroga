import unittest

def decimal_to_roman(decimal):
    valoresromano = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] #lista de numeros para restarle a (decimal)
    letrasromano = ['M', 'CM', 'D', ' CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'] #Lista de letras para agregarle a total
    total = ''
    while decimal > 0:
        i = 0
        for _ in range(decimal // valoresromano[i]):
            total += letrasromano[i]
            decimal -= valoresromano[i]
        i += 1
    return total
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
        self.assertEqual(resultado, 'CXXIII')
if __name__ == '__main__':
    unittest.main()
