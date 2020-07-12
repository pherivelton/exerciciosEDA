import sys

#funcao que extrai o vertice com o menor caminho para um outro vertice
#que ainda nao foi incluido na arvore minima
def extraiMinimo(chave, visitados, numVertices):

    menor = sys.maxint #menor inicia como infinito

    for v in range(numVertices):
        if chave[v] < menor and visitados[v] == False:
            menor = chave[v]
            menorVertice = v
    return menorVertice

def prim(grafo, numVertices):

    chave = [sys.maxint] * numVertices #array para armazenar os menores pesos
    pai = [None] * numVertices #array para ir construindo a arvore
    pai[0] = -1 #primeiro elemento sempre eh a raiz
    chave[0] = 0
    visitados = [False] * numVertices #array de vertices visitados, inicia todos como false

    for i in range(numVertices):

        u = extraiMinimo(chave, visitados, numVertices)
        visitados[u] = True

        for v in range(numVertices):
            if grafo[u][v] > 0 and visitados[v] == False and chave[v] > grafo[u][v]:
                chave[v] = grafo[u][v]
                pai[v] = u

    for i in range(1,numVertices):
        print pai[i], "-", i, "\t", grafo[i][pai[i]]
