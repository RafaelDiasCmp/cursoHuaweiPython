'''Enunciado
Programa que mostre na tela os 10 primeiros termos de uma PA com primeiro termo P
e Razão R
Os dois números P e R são inteiros e devem ser lidos no teclado'''
print('Início do programa!')
P = int(input('Digite o primeiro termo de sua PA: '))
R = int(input('Digite a razão de sua PA: '))
cont = 1

while cont <= 10:
    if P == P:
        print(f'{P}')
        P = P + R
        cont += 1
    else:
        PA = P + R
        print(f'{PA}')
        cont += 1
        P = P + R
print('Fim do Programa')
