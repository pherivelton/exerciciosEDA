import sys
def quickSort(lista, indEsquerdo, indDireito):
    if (indEsquerdo < indDireito):
        meio = particao(lista, indEsquerdo, indDireito)
        quickSort(lista, indEsquerdo, meio - 1)
        quickSort(lista, meio + 1, indDireito)

def particao(lista, indEsquerdo, indDireito):
    i = indEsquerdo + 1
    j = indDireito
    pivo = lista[indEsquerdo] #cria o pivo para manipular os indices

    while (i <= j):
        if (lista[i] <= pivo):
            i += 1
        elif lista[j] > pivo:
            j -= 1
        else:
            troca(lista, i, j) #faz a troca dos valores dos indices

    troca(lista, indEsquerdo, j)

    return j

#metodo que realiza a troca dos valores pelos indices
def troca(lista, i, j):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux
    
with open(sys.argv[1]) as inputNumbers:
    lines = inputNumbers.read().splitlines()
    lista = [int(number) for number in lines]
    indEsquerdo = 0
    indDireito = len(lista) - 1
with open(sys.argv[1]+'.txt','wr') as saidaOrdenacao:
  quickSort(lista, indEsquerdo, indDireito)
  saidaOrdenacao.write("Array ordenado pelo algoritmo Quick Sort\n")
  for numero in lista:
    saidaOrdenacao.write(str(numero) + " ")
