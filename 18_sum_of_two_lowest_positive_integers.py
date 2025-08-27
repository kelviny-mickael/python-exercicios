# Crie uma função que retorne a soma dos dois menores números positivos, 
# dado um array de no mínimo 4 inteiros positivos. 
# Nenhum número flutuante ou inteiro não positivo será passado.
# Por exemplo, quando um array é passado como [19, 5, 42, 2, 77], a saída deve ser 7.
# [10, 343445353, 3453445, 3453545353453]deve retornar 3453455.

def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]

print(sum_two_smallest_numbers([10, 500, 15, 2000]))
print(sum_two_smallest_numbers([153450, 500, 15345435, 2000]))
print(sum_two_smallest_numbers([100, 5001, 150, 24534000]))