# Se você não consegue dormir, é só contar carneirinhos!!
# Tarefa:
# Dado um inteiro não negativo, 3 por exemplo, retorne uma string com um murmúrio: 
# "1 sheep...2 sheep...3 sheep...". A entrada sempre será válida, ou seja, 
# sem inteiros negativos.

def count_sheep(num):
    for count_sheep in range(1, (num + 1)):
        print(f'{count_sheep} sheep')

count_sheep(10)