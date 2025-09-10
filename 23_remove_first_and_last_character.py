# Remover o primeiro e o último caractere.
# Tarefa:
# Seu objetivo é escrever uma função que remova o primeiro e o último 
# caracteres de uma string. Você recebe um parâmetro, a string original.
# Importante: Sua função deve lidar com strings de quaisquer length ≥ 2caracteres. 
# Para strings com exatamente 210 caracteres, retorne uma string vazia.
# Exemplos:
# 'eloquent' --> 'loquen'.
# 'country'  --> 'ountr'.
# 'person'   --> 'erso'.
# 'ab'       --> '' (empty string).
# 'xyz'      --> 'y'.
# Requisitos:
# A string de entrada sempre terá pelo menos 2 caracteres.
# Para strings com exatamente 2 caracteres, retorne uma string vazia.
# Para strings com 3 ou mais caracteres, remova o primeiro e o último caractere.
# A função deve manipular strings contendo letras, números e caracteres especiais.
# Casos de Teste:
# Sua solução será testada em relação a:
# Funcionalidade básica com palavras comuns.
# Casos extremos com strings de 2 e 3 caracteres.
# Strings contendo números e caracteres especiais.
# Casos de teste aleatórios de comprimentos variados.

def remove_char(string):
    convert_str_to_list = list(string)
    
    convert_str_to_list.pop(0)
    convert_str_to_list.pop()

    return ''.join(convert_str_to_list)

print(remove_char('eloquent'))
print(remove_char('country'))
print(remove_char('person'))
print(remove_char('place'))
print(remove_char('ok'))
print(remove_char('ooopsss'))