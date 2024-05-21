'''Enunciado
Programa que lê um número inteiro D > 0 e exiba os números < 100 que são divisíveis
 pelo número D escolhido'''

print('Início do programa')
D = int(input('Digite um número para saber seus múltiplos: '))
cont = 1

if D > 0:
    while cont <= 100:
        if cont % D == 0:
            print(f'{cont}')
        cont += 1
else:
    print(f'{D} é menor que 0')
print('Fim do Programa')



