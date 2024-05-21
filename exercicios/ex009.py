'''Enunciado
Programa que mostre a PA dos 10 primeiros termos de um PA
lendo o P e o R COM A FUNÇÃO RANGE'''

P = int(input('Digite o primeiro termo: '))
R = int(input('Digite a razão da PA: '))
Q = int(input('Digite a quantidade de termos da PA: '))

ultimo = P + R * (Q-1)
Termos = list(range(P, ultimo+1, R))
print('Lista gerada com range')
print(Termos)
print('Fim do Programa')