def troca(array, i, j):
    aux = array[i]
    array[i] = array[j]
    array[j] = aux
    return array

def maxHeapfy(array, n, i):
    maior = i
    esquerdo = (2*i) + 1
    direito = (2*i) + 2
    if (esquerdo < n and array[i] < array[esquerdo]):
        maior = esquerdo
    if (direito < n and array[maior] < array[direito]):
        maior = direito
    if maior != i:
        troca(array, i, maior)
        maxHeapfy(array, n, maior)
    
def buildMaxHeap(array):
    n = len(array)
    for i in range((len(array)//2)-1, -1, -1):
        maxHeapfy(array, n, i)
    return array

def heapSort(array):
    array = buildMaxHeap(array)
    for i in range(len(array)-1, 0, -1):
        troca(array, 0, i)
        maxHeapfy(array, i, 0)
    return array
        
