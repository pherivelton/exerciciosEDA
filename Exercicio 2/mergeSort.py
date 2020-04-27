import sys
def mergeSort(lista, indEsquerdo, indDireito):
    if (indEsquerdo < indDireito):
        meio = (indEsquerdo + indDireito) // 2
        mergeSort(lista, indEsquerdo, meio)
        mergeSort(lista, meio + 1, indDireito)
        merge(lista, indEsquerdo, meio, indDireito)

def merge(lista, indEsquerdo, meio, indDireito):
    copiaLista = [0] * (indDireito - indEsquerdo + 1)

    i = indEsquerdo
    j = meio + 1
    k = 0

    while (i <= meio and j <= indDireito):
        if (lista[i] < lista[j]):
            copiaLista[k] = lista[i]
            k += 1
            i += 1
        else:
            copiaLista[k] = lista[j]
            k += 1
            j += 1

    while i <= meio:
        copiaLista[k] = lista[i]
        k += 1
        i += 1

    while (j <= indDireito):
        copiaLista[k] = lista[j] 
        k += 1
        j += 1

    for i in range(indEsquerdo, indDireito+1):
        lista[i] = copiaLista[i - indEsquerdo]

with open(sys.argv[1]) as inputNumbers:
    lines = inputNumbers.read().splitlines()
    lista = [int(number) for number in lines]
    indEsquerdo = 0
    indDireito = len(lista) - 1
with open(sys.argv[1]+'.txt','wr') as saidaOrdenacao:
  mergeSort(lista, indEsquerdo, indDireito)
  saidaOrdenacao.write("Array ordenado pelo algoritmo Merge Sort\n")
  for numero in lista:
    saidaOrdenacao.write(str(numero) + " ")
