import sys

def mochilaInteira(pesoMochila, pesos, valores, qtdObjetos): 

    #Se o peso da mochila for 0 ou a quantidade de objetos for 0, retorna 0
    if qtdObjetos == 0 or pesoMochila == 0 : 
        return 0

    #Se o peso do ultimo item for maior que o peso da mochila, chama recursivo
    #a funcao passando o item anterior
    if (pesos[qtdObjetos-1] > pesoMochila): 
        return mochilaInteira(pesoMochila, pesos, valores, qtdObjetos-1)

    #senao pega o max entre o valor do item atual e o da chamada recursiva
    #do item anterior descontando o valor do peso do item atual
    else:
        return max( 
            valores[qtdObjetos-1] + mochilaInteira( 
                pesoMochila-pesos[qtdObjetos-1], pesos, valores, qtdObjetos-1),  
                mochilaInteira(pesoMochila, pesos, valores, qtdObjetos-1))

#metodo que retorna os itens inseridos na mochila
def itensEscolhidos(pesoMochila, pesos):
    aux = len(pesos)
    itens = []
    for i in range(len(pesos)-1, -1, -1):
        if (pesoMochila - pesos[i]) >= 0:
            pesoMochila -= pesos[i]
            itens.append(aux)
        aux -= 1
    return sorted(itens)
            
with open(sys.argv[1]) as inputNumbers:
    lines = inputNumbers.read().splitlines()
    qtdObjetos = int(lines[0].split()[0])
    pesoMochila = int(lines[0].split()[1])
    pesos = []
    valores= []
    for i in range(1, len(lines)):
        pesos.append(int(lines[i].split()[0]))
        valores.append(int(lines[i].split()[1]))
    itensEscolhidos = itensEscolhidos(pesoMochila, pesos)
with open(sys.argv[1]+'.txt','wr') as saidaOrdenacao:
  valorMochila = mochilaInteira(pesoMochila, pesos, valores, qtdObjetos)
  saidaOrdenacao.write("Valor: " + str(valorMochila) + "\n")
  itens = ""
  for item in itensEscolhidos:
      itens += (str(item) + " ")
  saidaOrdenacao.write("Produtos Escolhidos: " + itens)
