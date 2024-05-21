'''Enunciado
Faça um programa que enquanto o valor lido for diferente de 0, totalize e conte os
valores digitados, exceto o zero e apresente os valores na tela
Totalizar = Somar valores'''
print('Início do Programa')
A = int(input('Digite um número: '))
soma = qtde = 0
while A != 0:
    soma = soma + A
    qtde += 1
    A = int(input('Digite um número: '))
print(f'A soma dos valores = {soma}')
print(f'Quantidade = {qtde}')
print('Fim do programa')