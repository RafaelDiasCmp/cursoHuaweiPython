#Estrutura de Repetição
'''Programa que lê um valor x e enquanto X for diferente de 0
Continua dizendo s eo número é par ou ímpar'''
print('Ínicio do Programa')
x = int(input('Digite um número inteiro X: '))
resto = x % 2

while x != 0:
    if resto == 0:
        print(f'O número {x} é Par!')
        x = int(input('Digite outro número inteiro X: '))
    else:
        print(f'O número {x} Ímpar!')
        x = int(input('Digite outro número inteiro X: '))
print('0 = Fim do Programa!')
print('Fim do programa!')