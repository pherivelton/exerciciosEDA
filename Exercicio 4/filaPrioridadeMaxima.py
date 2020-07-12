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

def heapMaximun(array):
    return array[0]

def heapExtractMax(array):
    n = len(array)
    maior = array[0]
    array[0] = array[n-1]
    maxHeapfy(array, n, 0)
    return maior

def heapIncreaseKey(array, i, chave):
    array[i] = chave
    pai = i // 2
    while (i > 1 and array[pai] < array[i]):
        troca(array, pai, i)
        i = pai

def maxHeapInsert(array, chave):
    array.append(None)
    heapIncreaseKey(array, len(array)-1, chave)
