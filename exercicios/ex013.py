'''Enunciado
Programa que permaneça em laço lendo inteiros terminando quando digitado 0.
Adicione valores que não sejam repetidos na lista, se for repetido uma mensagem de erro
é exibida na tela!
Exiba os elementos e a quantidade de elementos dessa lista'''

lista = []
N = int(input('Digite um número: '))
while N != 0:
    if N not in lista:
        lista.append(N)
    else:
        print(f' Erro. o valor {N} já está na lista.')
    N = int(input('Digite um número: '))

print(f'A lista possui {len(lista)} elementos, sendo eles {lista}')
print('Fim do programa')