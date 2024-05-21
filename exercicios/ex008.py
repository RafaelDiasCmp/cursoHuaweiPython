'''Enunciado
Programa que mostre a PA dos 10 primeiros termos de um PA
lendo o P e o R'''

P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão da PA: '))
Q = int(input('Digite a quantidade de termos da PA: '))
Termos = []

cont = 0

while cont < Q:
    Termos.append(P)
    P = P + R
    cont += 1
print('\nLista Resultante')
print(Termos)
print('Fim do programa')