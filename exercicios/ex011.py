'''Enunciado
Programa que lê número inteiro N e em seguida leia N números inteiros carregando
os valores positivos em uma lista e positivos em outra, exibindo as listas e seu tamanho'''

N = int(input('Digite um número: '))
positivos = []
negativos = []

for i in range(N):
    x = int(input(f' elemento {i} >> '))
    if x >= 0:
        positivos.append(x)
    else:
        negativos.append(x)
print(f'\nListe de Negativos: {negativos}, contém {len(negativos)} elementos')
print(f'\nLista de Positivos: {positivos}, contém {len(positivos)} elementos')
print('Fim do programa')