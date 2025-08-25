# Crie uma função que receba um inteiro como argumento e retorne "Even"para números pares ou "Odd"ímpares.

# def even_or_odd(number):
#     if number % 2 == 0:
#         return 'É impar!'
#     else:
#         return 'É par!'
    
# print(even_or_odd(10))
# print(even_or_odd(5))
# print(even_or_odd(20))
# print(even_or_odd(120))

def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'

print(even_or_odd(10))
print(even_or_odd(5))
print(even_or_odd(70))
print(even_or_odd(100))