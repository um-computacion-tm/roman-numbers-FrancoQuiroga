def roman_to_decimal(roman):
    total = 0
    i = ''
    for letter in roman:
        if letter == 'I':
            total += 1
            i = 'I'
        elif letter == 'V':
            if i == 'I':
                total -= 2
            total += 5
        elif letter == 'X':
            if i == 'I':
                total -= 2
            total += 10
            i = 'X'
        elif letter == 'L':
                if i == 'X':
                    total -= 20
                total += 50
        elif letter == 'C':
                if i == 'X':
                    total -= 20
                total += 100
                i = 'C'
        elif letter == 'D':
                if i == 'C':
                    total -= 200
                total += 500
        elif letter == 'M':
                if i == 'C':
                    total -= 200
                total += 1000
    return total