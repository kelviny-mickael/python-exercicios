# Escreva uma função para dividir uma string e convertê-la em um array de palavras.
# Exemplos (Entrada ==> Saída):
# "Robin Singh" ==> ["Robin", "Singh"].
# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"].

def string_to_array(str):
    return str.split() if str else ['']

print(string_to_array('Eu sou o Kelviny, tudo bem?'))
print(string_to_array(''))