'''Enunciado
Programa que lê o número inteiro N e em seguida leia N números reais carregando-os em uma lista
exibindo os elementos da lista na tabela um em cada linha'''

N = int(input('Digite um número inteiro: '))
L = []
for i in range(N):
    x = float(input(f' elemento {i}: '))
    L.append(x)
print('\nResultado')
for valor in L:
    print(f' {valor:.2f}')
print('Fim do programa')