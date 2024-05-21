'''Enunciado
Escreva um programa que permaneça em um laço lendo números inteiros. O laço termina quando
for digitado 0. Cada valor diferente de zero digitado deve ser colocado em uma lista.
Ao final exiba a lista na tela e a quantidade de elementos que ela contém!'''
lista = []
N = int(input('Digite um número: '))

while N != 0:
    lista.append(N)
    N = int(input('Digite um número: '))
print(f'A lista possui {len(lista)} elementos, sendo eles {lista}')
print('Fim do programa')