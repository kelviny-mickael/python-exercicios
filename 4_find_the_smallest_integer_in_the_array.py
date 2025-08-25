# Dado um conjunto de inteiros, sua solução deve encontrar o menor inteiro.
# Por exemplo:
# Dada [34, 15, 88, 2] a sua solução retornará 2.
# Dada [34, -345, -1, 100] a sua solução retornará -345.
# Você pode assumir, para o propósito deste kata, que o array fornecido não estará vazio.

def find_smallest_int(arr):
    return min(arr)

print(find_smallest_int([100, 35, 240, -100, 242, -350, 100]))