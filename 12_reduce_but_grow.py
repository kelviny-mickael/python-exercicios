# Dado um array não vazio de inteiros, retorne o resultado da multiplicação dos valores em ordem.
# Exemplo:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24.

def grow(arr_numbers):
    result = 1
    for number in arr_numbers:
        print(result * number)


grow([1, 2, 3, 4])