'''Enunciado
Programa que mostre a tabuada do número inteiro N digitado'''
print('Início do programa')
N = int(input('Digite um número para mostrar sua tabuada: '))
cont = 1
while cont <= 10:
    tabuada = N * cont
    print(f'{N} x {cont} = {tabuada}')
    cont += 1
print('Fim do Programa')