# Dados dois números inteiros a e b, que podem ser positivos ou negativos, 
# encontre a soma de todos os números inteiros entre eles e incluindo-os e retorne-a. 
# Se os dois números forem iguais, retorne a ou b.
# Nota: a e bnão são ordenados!
# Exemplos (a, b) --> saída (explicação):
# (1, 0) --> 1 (1 + 0 = 1)
# (1, 2) --> 3 (1 + 2 = 3)
# (0, 1) --> 1 (0 + 1 = 1)
# (1, 1) --> 1 (1 since both are same)
# (-1, 0) --> -1 (-1 + 0 = -1)
# (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)
# Sua função deve retornar apenas um número, não a explicação sobre como você obteve esse número.

def get_sum(valueA, valueB):
    if valueA != valueB:
        return valueA + valueB
    else:
        return f'{valueA} since both are same'

print(get_sum(1, 0))
print(get_sum(-1, 2))
print(get_sum(1, 1))