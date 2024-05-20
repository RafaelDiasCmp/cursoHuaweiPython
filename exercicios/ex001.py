# Programa que recebe um número inteiro e retorna se o mesmo é Par ou Ímpar

num1 = int(input('Digite um número: '))
resto = num1 % 2

if resto == 0:
    print(f'O número {num1} é Par')
else:
    print(f'O número {num1} é Ímpar')