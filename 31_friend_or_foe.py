# Crie um programa que filtre uma lista de strings e retorne uma lista 
# contendo apenas o nome de seus amigos.
# Se um nome tiver exatamente 4 letras, você pode ter certeza de 
# que é um amigo seu! Caso contrário, pode ter certeza de que não é...
# Input = ["Ryan", "Kieran", "Jason", "Yous"].
# Output = ["Ryan", "Yous"].
# Input = ["Peter", "Stephen", "Joe"].
# Output = [].
# As sequências de entrada conterão apenas letras.
# Observação: mantenha a ordem original dos nomes na saída.

def friend(list):
    friend_list = []

    for friend in list:
        if len(friend) == 4:
            friend_list.append(friend)

    return friend_list

string_list = ['Ryan', 'Kieran', 'Jason', 'Yous']

print(friend(string_list))
