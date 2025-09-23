# Escreva uma função que calcule a média dos números em uma determinada matriz.
# Observação: matrizes vazias devem retornar 0.

def find_average(numbers):
    media = len(numbers)
    sum = 0
    for number in numbers:
        sum += number
    if media > 0:
        return int(sum / media)
    else:
        return 0

print(find_average([]))

class Thiago():
    nome = 'tHIAGO'