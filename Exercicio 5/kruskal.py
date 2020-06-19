def buscaConjunto(pai, vertice):
    if pai[vertice] == vertice:
        return vertice
    return buscaConjunto(pai, pai[i])

def uniao(pai, subconjunto, vertX, vertY):

    raizX = buscaConjunto(pai, vertX)
    raizY = buscaConjunto(pai, vertY)

    if subconjunto[raizX] < subconjunto[raizY]:
        pai[raizX] = raizY
    elif subconjunto[raizX] > subconjunto[raizY]:
        pai[raizY] = raizX
    else:
        pai[raizY] = raizX
        subconjunto[raizX] += 1

def kruskal(grafo, numVertices):

    arvore = [] #resultado da arvore de menor caminho
    aux = 0
    arvIndex = 0
    grafo = sorted(grafo, key=lambda item: item[2]) #ordena pelo peso
    pai = []
    subconjunto = []

    for vertice in range(numVertices):
        pai.append(vertice)
        subconjunto.append(0)

    while arvIndex < numVertices - 1:

        u, v, peso = grafo[aux]
        aux += 1
        vertX = buscaConjunto(pai, u)
        vertY = buscaConjunto(pai, v)

        if vertX != vertY:

            arvIndex += 1
            arvore.append([u,v,peso])
            uniao(pai, subconjunto, x, y)
    
