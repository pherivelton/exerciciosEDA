import sys
def insertionSort(lista):
  for i in range(1, len(lista)):
    chave = lista[i]
    k = i
    while k > 0 and chave < lista[k - 1]:
        lista[k] = lista[k - 1]
        k -= 1
    lista[k] = chave
  return lista

def selectionSort(lista):

   for i in range(len(lista)):
       menorIndice = i
       for j in range(i+1, len(lista)):
           if lista[j] < lista[menorIndice]:
               menorIndice = j     
       temp = lista[i]
       lista[i] = lista[menorIndice]
       lista[menorIndice] = temp

   return lista

with open(sys.argv[1]) as inputNumbers:
    lines = inputNumbers.read().splitlines()
    numbers = [int(number) for number in lines]
with open(sys.argv[1]+'.txt','wr') as saidaOrdenacao:
  orderedArrayInsertion = insertionSort(numbers)
  orderedArraySelection = selectionSort(numbers)
  saidaOrdenacao.write("Array ordenado pelo algoritmo Insertion Sort\n")
  for number in orderedArrayInsertion:
    saidaOrdenacao.write(str(number) + " ")
  saidaOrdenacao.write("\nArray ordenado pelo algoritmo Selection Sort\n")
  for number in orderedArraySelection:
    saidaOrdenacao.write(str(number) + " ")
