import sys

#metodo para fazer a troca dos elementos
def troca(array, i, j):
    aux = array[i]
    array[i] = array[j]
    array[j] = aux
    return array

def maxHeapfy(array, n, i):
    maior = i #seta o maior como o i passado como parametro
    esquerdo = (2*i) + 1 #soma +1 por conta da posicao 0
    direito = (2*i) + 2 #soma +1 por conta da posicao 0
    if (esquerdo < n and array[i] < array[esquerdo]):
        maior = esquerdo #atualiza o maior com o esquerdo
    if (direito < n and array[maior] < array[direito]):
        maior = direito #atualiza o maior com o direito
    if maior != i:
        troca(array, i, maior)
        maxHeapfy(array, n, maior)
    
def buildMaxHeap(array):
    n = len(array)
    #itera ate a metade da arvore, pois nao precisa chamar o maxHeapfy para folhas
    for i in range((len(array)//2)-1, -1, -1):
        maxHeapfy(array, n, i)
    return array

def heapSort(array):
    array = buildMaxHeap(array)
    for i in range(len(array)-1, 0, -1):
        troca(array, 0, i)
        maxHeapfy(array, i, 0) #passa a posicao 0, pelo fato de ser o maior elemento
    return array

with open(sys.argv[1]) as inputNumbers:
    lines = inputNumbers.read().splitlines()
    numbers = [int(number) for number in lines]
with open(sys.argv[1]+'.txt','wr') as saidaOrdenacao:
  orderedArrayInsertion = heapSort(numbers)
  saidaOrdenacao.write("Array ordenado pelo algoritmo Heapsort\n")
  for number in orderedArrayInsertion:
    saidaOrdenacao.write(str(number) + " ")
        
