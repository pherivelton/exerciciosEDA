import sys
def countingSort(array):
    maiorElemento = max(array) #pega o maior elemento
    arrayOrdenado = [0] * len(array) #cria o array de saida
    arrayAuxiliar = [0] * (maiorElemento+1) #array que ira guardar a contagem dos elementos
    for i in range(len(array)):
        #conta a ocorrencia de um elemento no array
        arrayAuxiliar[array[i]] = arrayAuxiliar[array[i]] + 1
    for j in range(1,maiorElemento+1):
        arrayAuxiliar[j] = arrayAuxiliar[j] + arrayAuxiliar[j-1]
    for k in range(len(array)-1, -1, -1):
        #coloca o elemento no local adequado na ordenacao
        arrayOrdenado[arrayAuxiliar[array[k]]-1] = array[k]
        arrayAuxiliar[array[k]] = arrayAuxiliar[array[k]] - 1
    return arrayOrdenado

#metodo que auxilia na formatacao do array para imprimi-lo na saida
def ajustaArrayImpressao(lista, elemento):
    for i in range(len(lista)):
        lista[i] += elemento
    return lista

with open(sys.argv[1]) as inputNumbers:
    lines = inputNumbers.read().splitlines()
    numbers = [int(number) for number in lines]
menorElemento = min(numbers)
if menorElemento < 0:
    menorElemento *= -1
    numbers = ajustaArrayImpressao(numbers, menorElemento)
    orderedArrayCounting = countingSort(numbers)
    menorElemento *= -1
    orderedArrayCounting = ajustaArrayImpressao(orderedArrayCounting, menorElemento)
else:
    orderedArrayCounting = countingSort(numbers)
with open(sys.argv[1]+'.txt','wr') as saidaOrdenacao:
  saidaOrdenacao.write("Array ordenado pelo algoritmo Counting Sort\n")
  for number in orderedArrayCounting:
    saidaOrdenacao.write(str(number) + " ")
