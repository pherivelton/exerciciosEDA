import sys

#counting sort adaptado para o radix sort
def countingSort(array, digito):
    significancia = pow(10,digito) #atualizando o indice significante (unidade, dezena, centena, etc...)
    arrayOrdenado = [0] * len(array)
    arrayAuxiliar = [0] * 10 #array que ira guardar a contagem de cada digito
    for i in range(len(array)):
        #divide pela significancia (1, 10, 100, etc..) e faz o mode 10 para entao
        #pegar o digito significante, colocando o valor no lugar correto do array
        arrayAuxiliar[(array[i]/significancia) % 10] = arrayAuxiliar[(array[i]/significancia) % 10] + 1
    for j in range(1,10):
        arrayAuxiliar[j] = arrayAuxiliar[j] + arrayAuxiliar[j-1]
    for k in range(len(array)-1, -1, -1):
        arrayOrdenado[arrayAuxiliar[(array[k]/significancia) % 10]-1] = array[k]
        arrayAuxiliar[(array[k]/significancia) % 10] = arrayAuxiliar[(array[k]/significancia) % 10] - 1
    return arrayOrdenado


def radixSort(array):
    digito = len(str(max(array))) #quantidade de digitos do maior numero do array
    #iteracao do indice menos significante para o mais significante
    for i in range(digito):
        array = countingSort(array, i)
    return array

#funcao para ajustar o array para a impressao, transformando-os em positivos
#e depois em negativos novamente, para exibir o array original ordenado
def ajustaArrayImpressao(lista, elemento):
    for i in range(len(lista)):
        lista[i] += elemento
    return lista

with open(sys.argv[1]) as inputNumbers:
    lines = inputNumbers.read().splitlines()
    numbers = [int(number) for number in lines]
menorElemento = min(numbers)
#se o array tiver numeros negativos, tratar para deixar todos positivos, ordenar
#e entao transformar em negativo novamente para manter o array com os valores originais ordenados
if menorElemento < 0:
    menorElemento *= -1
    numbers = ajustaArrayImpressao(numbers, menorElemento)
    orderedArrayRadix = radixSort(numbers)
    menorElemento *= -1
    orderedArrayRadix = ajustaArrayImpressao(orderedArrayRadix, menorElemento)
else:
    orderedArrayRadix = radixSort(numbers)
with open(sys.argv[1]+'.txt','wr') as saidaOrdenacao:
  saidaOrdenacao.write("Array ordenado pelo algoritmo Radix Sort\n")
  for number in orderedArrayRadix:
    saidaOrdenacao.write(str(number) + " ")
