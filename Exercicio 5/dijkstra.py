import sys

def extraiMenorDistancia(distancias, visitados, numVertices):

    menorDistancia = sys.maxsize #colocando todos como infinito

    for vertice in range(numVertices):

        #calcula o vertice que possui a menor distancia
        if distancias[vertice] < menorDistancia and visitados[vertice] == False:
            menorDistancia = distancias[vertice]
            vert = vertice

    return vert

def dijkstra(grafo, numVertices, origem):
    distancias = [sys.maxsize] * numVertices #seta as distancias como infinito
    distancias[origem] = 0 #atualiza o vertice da origem
    visitados = [False] * numVertices

    for i in range(numVertices):

        u = extraiMenorDistancia(distancias, visitados, numVertices)
        visitados[u] = True

        for v in range(numVertices):
            if grafo[u][v] > 0 and visitados[v] == False and distancias[v] > (distancias[u] + grafo[u][v]):
                distancias[v] = distancias[u] + grafo[u][v] #relaxando o vertice

    print ("Vertex tDistance from Source")
    for i in range(numVertices):
        print (i, "t", distancias[i])
