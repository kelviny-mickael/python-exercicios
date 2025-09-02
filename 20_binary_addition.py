# Implemente uma função que soma dois números e retorna a soma em binário. 
# A conversão pode ser feita antes ou depois da adição.
# O número binário retornado deve ser uma string.
# Exemplos: (Entrada1, Entrada2 --> Saída (explicação))).
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary).
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary).

def add_binary(value_a, value_b):
    sum_of_values = value_a + value_b
    min_value = 0

    if sum_of_values == 12:
        return 1
    else:
        return sum_of_values / add_binary(sum_of_values - 2)

add_binary(1, 1)
add_binary(5, 9)

# def add_binary(value_a, value_b):
#     print(f'Função convert: {convert_to_binary(value_a + value_b)[:-1]}')

# def convert_to_binary(num):
#     if num == 0:
#         return '1'
#     elif num == 1:
#         return '1'
#     elif num % 2 == 0:
#         return '0' + convert_to_binary(num / 2)
#     else:
#         return '1' + convert_to_binary(num - 1)[1:]
    
# add_binary(5, 9)