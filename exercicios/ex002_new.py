#Programa que leia dois números inteiros e mostre apenas o menor entre os dois
#Se forem iguais, mostre apenas um deles
#Agora exibindo a mensagem os dois números são iguais caso forem números iguais
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('DIgite o segundo número: '))

if num1 == num2:
    print('Os números são iguais!')
else:
    if num1 > num2:
        maior = num1
        print(f'O maior número é o {num1}')
    else:
        maior = num2
        print(f'O maior número é o {num2}')


