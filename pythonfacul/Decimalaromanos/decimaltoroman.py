def decimal_to_roman(decimal):
    valoresromano = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] #lista de numeros para restarle a (decimal)
    letrasromano = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'] #Lista de letras para agregarle a total
    total = ''
    i = 0
    while decimal > 0:
        for _ in range(decimal // valoresromano[i]):
            total += letrasromano[i]
            decimal -= valoresromano[i]
        i += 1
    return total