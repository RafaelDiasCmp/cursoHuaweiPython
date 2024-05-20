#Programa que leia dois números inteiros e mostre apenas o menor entre os dois
#Se forem iguais, mostre apenas um deles

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 >= num2:
    maior = num1
else:
    maior = num2
print(f'O maior número é {maior}')
