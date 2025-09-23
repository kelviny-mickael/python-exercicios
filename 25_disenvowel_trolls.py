# Trolls estão atacando sua seção de comentários!
# Uma maneira comum de lidar com essa situação é remover todas as vogais dos 
# comentários dos trolls, neutralizando a ameaça.
# Sua tarefa é escrever uma função que receba uma string e retorne uma nova string com 
# todas as vogais removidas.
# Por exemplo, a sequência "Este site é para perdedores, LOL!" se tornaria 
# "Ths wbst s fr lsrs LL!".
# Nota: para este kata o som y não é considerado uma vogal.

def disemvowel(string):
    vowels = 'aeiou'
    new_string_without_vowels = []

    for characters in string:
        if not characters in vowels:
            new_string_without_vowels.append(characters)

    return ''.join(new_string_without_vowels)

print(disemvowel('This website is for losers LOL!'))
print(disemvowel("No offense but,\nYour writing is among the worst I've ever read"))
print(disemvowel('What are you, a communist?'))