# Você obtém uma matriz de números e retorna a soma de todos os números positivos.
# Exemplo:
# [1, -4, 7, 12]=> 1 + 7 + 12 = 20.
# Observação:
# Se não houver nada para somar, a soma padrão será 0.


def positive_sum(numbers_list):
    sum_numbers = []
    for num in numbers_list:
        if num < 0:
            continue
        
        sum_numbers.append(num)

    return sum(sum_numbers)

positive_sum([1, -4, 7, 12])
positive_sum([1, -4, 7, -12])
positive_sum([1, -4, 7, -12, 100, 5, -100, -200, 10])