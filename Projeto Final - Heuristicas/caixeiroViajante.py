import sys
import random

#verifica se um dado caminho eh valido
def verificaCaminho(distancias, cidade1, cidade2):

    return distancias[cidade1][cidade2] > 0 

def caixeiroViajante(distancias, cidades):

    numVertices = len(cidades)
    soma = 0
    for i in range(numVertices-1):

        #se nao existir caminho entre duas cidades, eh considerado uma
        #solucao invalida
        if (verificaCaminho(distancias, cidades[i], cidades[i+1])) == False:

            return "Solução invalida"

        soma += distancias[cidades[i]][cidades[i+1]] #incrementa a distancia entre duas cidades

    soma += distancias[cidades[numVertices-1]][cidades[0]] #incrementa a distancia da ultima cidade para a origem
    
    return soma

#extrai o vizinho aleatorio dentre os mais proximos de uma cidade
def extraiVizinhoAleatorio(distancias, cidades, vertAtual, visitados):

    vizinhos = []
    for vertice in range(len(cidades)):
        if distancias[vertAtual][vertice] > 0 and visitados[vertice] == False:
            vizinhos.append((vertice, distancias[vertAtual][vertice]))
    vizinhos.sort(key=lambda tup: tup[1]) #ordena o array de vizinhos pela distancia
    vertAleatorio = random.choice(vizinhos[0:(len(vizinhos)//2)+1])#como o array esta ordenado pela distancia (do menor para o maior) pego os 50% primeiros
    return vertAleatorio[0]

#extrai o vizinho mais proximo de uma cidade
def extraiVizinhoMaisProximo(distancias, cidades, vertAtual, visitados):

    menorDistancia = sys.maxsize
    for vertice in range(len(cidades)):
        if distancias[vertAtual][vertice] > 0 and visitados[vertice] == False and distancias[vertAtual][vertice] < menorDistancia:
            vertMinimo = vertice
            menorDistancia = distancias[vertAtual][vertice]

    return vertMinimo

#extrai o vizinho mais distante de uma cidade
def extraiVizinhoMaisDistante(distancias, cidades, vertAtual, visitados):

    maiorDistancia = 0
    for vertice in range(len(cidades)):
        if distancias[vertAtual][vertice] > 0 and visitados[vertice] == False and distancias[vertAtual][vertice] > maiorDistancia:
            vertMaximo = vertice
            maiorDistancia = distancias[vertAtual][vertice]

    return vertMaximo

#extrai o vizinho mais barato a partir da formula
#dik + dkj - dij, onde
#i - origem
#j - extremo
#k - cidade a ser inserida na rota
def extraiVizinhoMaisBarato(distancias, cidades, ordemCidades, visitados):

    menorDistancia = sys.maxsize
    up = len(ordemCidades)-1
    for u in range(len(ordemCidades)-1):
        for v in cidades:
            somaDistancias = (distancias[ordemCidades[u]][v] + distancias[v][ordemCidades[u+1]] - distancias[ordemCidades[u]][ordemCidades[u+1]])
            if somaDistancias < menorDistancia and visitados[v] == False:
                menorDistancia = somaDistancias
                vertAAdd = v
                posicao = u+1
    for v in cidades:
        somaDistancias = (distancias[ordemCidades[up]][v] + distancias[v][ordemCidades[0]] - distancias[ordemCidades[up]][ordemCidades[0]])
        if somaDistancias < menorDistancia and visitados[v] == False:
            menorDistancia = somaDistancias
            vertAAdd = v
            posicao = len(ordemCidades)
            
    return (posicao,vertAAdd)

def construcaoAleatoria(distancias, cidades, vertInicial):

    numCidades = len(cidades)
    ordemCidades = [vertInicial] #inicializa o vetor com a ordem das cidades
    visitados = [False] * numCidades #inicializa o vetor de cidades visitadas
    visitados[vertInicial] = True #seta a cidade origem como visitada
    contCidades = 1
    vertAtual = vertInicial

    #enquanto todas as cidades nao forem visitadas
    #pega o vizinho mais proximo e adicionar na rota
    while contCidades < numCidades:

        vertAtual = extraiVizinhoAleatorio(distancias, cidades, vertAtual, visitados) #pega a cidade vizinha dentre as 50% mais proximas
        visitados[vertAtual] = True #seta a cidade como visitada
        ordemCidades.append(vertAtual) #adiciona a cidade na rota
        contCidades += 1

    solucao = caixeiroViajante(distancias, ordemCidades) #calcula a distancia da rota encontrada

    return (solucao, ordemCidades)


def vizinhoMaisProximo(distancias, cidades, vertInicial):

    numCidades = len(cidades)
    ordemCidades = [vertInicial] #inicializa o vetor com a ordem das cidades
    visitados = [False] * numCidades #inicializa o vetor de cidades visitadas
    visitados[vertInicial] = True #seta a cidade origem como visitada
    contCidades = 1
    vertAtual = vertInicial

    #enquanto todas as cidades nao forem visitadas
    #pega o vizinho mais proximo e adicionar na rota
    while contCidades < numCidades:

        vertAtual = extraiVizinhoMaisProximo(distancias, cidades, vertAtual, visitados) #pega a cidade vizinha mais proxima
        visitados[vertAtual] = True #seta a cidade como visitada
        ordemCidades.append(vertAtual) #adiciona a cidade na rota
        contCidades += 1

    solucao = caixeiroViajante(distancias, ordemCidades) #calcula a distancia da rota encontrada

    return (solucao, ordemCidades)

def vizinhoMaisDistante(distancias, cidades, vertInicial):

    numCidades = len(cidades)
    ordemCidades = [vertInicial] #inicializa o vetor com a ordem das cidades
    visitados = [False] * numCidades #inicializa o vetor de cidades visitadas
    visitados[vertInicial] = True #seta a cidade origem como visitada
    contCidades = 1
    vertAtual = vertInicial

    #enquanto todas as cidades nao forem visitadas
    #pega o vizinho mais proximo e adicionar na rota
    while contCidades < numCidades:

        vertAtual = extraiVizinhoMaisDistante(distancias, cidades, vertAtual, visitados) #pega a cidade vizinha mais proxima
        visitados[vertAtual] = True #seta a cidade como visitada
        ordemCidades.append(vertAtual) #adiciona a cidade na rota
        contCidades += 1

    solucao = caixeiroViajante(distancias, ordemCidades) #calcula a distancia da rota encontrada

    return (solucao, ordemCidades)

def bellmoreENemhauser(distancias, cidades, vertInicial):

    numCidades = len(cidades)
    ordemCidades = [vertInicial] #inicializa o vetor com a ordem das cidades
    visitados = [False] * numCidades #inicializa o vetor de cidades visitadas
    visitados[vertInicial] = True #seta a cidade origem como visitada
    contCidades = 2
    vertAtual = vertInicial
    vertAtual = extraiVizinhoMaisProximo(distancias, cidades, vertAtual, visitados) #pega a cidade vizinha mais proxima
    visitados[vertAtual] = True #seta a cidade como visitada
    ordemCidades.append(vertAtual) #adiciona a cidade na rota

    #enquanto todas as cidades nao forem visitadas
    #pega a cidade que menos dista a um dos extremos da rota
    while contCidades < numCidades:

        ultimoVert = len(ordemCidades)-1
        ext1 = ordemCidades[0]
        ext2 = ordemCidades[ultimoVert]
        v1 = extraiVizinhoMaisProximo(distancias, cidades, ordemCidades[0], visitados) #cidade vizinha mais proxima da origem
        v2 = extraiVizinhoMaisProximo(distancias, cidades, ordemCidades[ultimoVert], visitados) #cidade vizinha mais proxima do extremo
        dist1 = distancias[v1][ext1] #distancia entre a cidade mais proxima da origem e a origem
        dist2 = distancias[v2][ext2] #distancia entre a cidade mais proxima do extremo e o extremo

        #se a distancia entre a cidade mais proxima da origem e a origem for menor que a distancia
        #da cidade mais proxima do extremo e o extremo, a cidade a ser inserida na rota é antes da origem
        #senao apos o extremo
        if dist1 <= dist2:
            visitados[v1] = True #seta a cidade como visitada
            ordemCidades.insert(0, v1) #adiciona a cidade na rota
        else:
            visitados[v2] = True #seta a cidade como visitada
            ordemCidades.insert(len(ordemCidades), v2) #adiciona a cidade na rota
        
        contCidades += 1

    solucao = caixeiroViajante(distancias, ordemCidades) #calcula a distancia da rota encontrada

    return solucao

def insercaoMaisBarata(distancias, cidades, vertInicial):

    numCidades = len(cidades)
    ordemCidades = [vertInicial] #inicializa o vetor com a ordem das cidades
    visitados = [False] * numCidades #inicializa o vetor de cidades visitadas
    visitados[vertInicial] = True #seta a cidade origem como visitada
    vertAtual = vertInicial

    #pega q cidade cuja distancia entre a origem eh a menor
    vertAtual = extraiVizinhoMaisProximo(distancias, cidades, vertAtual, visitados)
    ordemCidades.append(vertAtual) #adiciona a cidade na rota
    visitados[vertAtual] = True #seta a cidade como visitada

    #pega a cidade cuja distancia entre os extremos eh a menor (forma a subrota)
    menorDistancia = sys.maxsize
    for v in cidades:
        somaDist = distancias[ordemCidades[0]][v] + distancias[ordemCidades[len(ordemCidades)-1]][v]
        if visitados[v] == False and somaDist < menorDistancia:
            vert = v
            menorDistancia = somaDist
    ordemCidades.append(vert) #adiciona a cidade na rota
    visitados[vert] = True #seta a cidade como visitada
        
    #enquanto todas as cidades nao forem visitadas, extrai o vizinho mais barato para
    #adicionar na rota
    while len(ordemCidades) < len(cidades):
        
        vertAtual = extraiVizinhoMaisBarato(distancias, cidades, ordemCidades, visitados) #pega a cidade vizinha mais barata
        ordemCidades.insert(vertAtual[0], vertAtual[1]) #adiciona a cidade na rota, na posicao correta
        visitados[vertAtual[1]] = True #seta a cidade como visitada

    solucao = caixeiroViajante(distancias, ordemCidades) #calcula a distancia da rota encontrada

    return (solucao, ordemCidades)
                                         
#ajustando a rota, invertendo os vertices entre i e j
def swap(rota, vertA, vertB):

    novaRota = []
    for i in range(vertA):
        novaRota.append(rota[i])
    aux = 0
    for j in range(vertA, vertB+1):
        novaRota.append(rota[vertB-aux])
        aux += 1
    for k in range(vertB+1, len(rota)):
        novaRota.append(rota[k])
    return novaRota

#mover o vertice de uma posicao i para uma posicao j
def moverVertice(rota, vertA, vertB):

    novaRota = []
    for i in range(vertA):
        novaRota.append(rota[i])
    for j in range(vertA+1, vertB+1):
        novaRota.append(rota[j])
    novaRota.append(rota[vertA])
    for k in range(vertB+1, len(rota)):
        novaRota.append(rota[k])
    return novaRota

#metodo que tem a finalidade de pegar duas arestas nao adjacentes
#e reconecta-las com outras duas arestas
def twoOpt(distancias, solucao):

    rota = solucao[1]
    distancia = solucao[0]
    aux = 1
    while (aux != 0):
        aux = 0
        for i in range(1,len(rota)-2):
            for j in range(i+1, len(rota)-1):
                #se a soma das distancias (i,i-1) + (j,j+1) for maior que distancias entre 
                #(i,j+1) + (i-1,j) -> AB + CD > AC + BD  
                if ((distancias[rota[i-1]][rota[i]] + distancias[rota[j]][rota[j+1]]) >=
                    (distancias[rota[i]][rota[j+1]] + distancias[rota[i-1]][rota[j]])):
                    rota = swap(rota, i, j)
                    novaDistancia = caixeiroViajante(distancias, rota)
                    if novaDistancia < distancia:
                        distancia = novaDistancia
                        aux += 1
    return (distancia, rota)

#metodo que tem o objetivo trocar um vertice com outro, caso a troca traga melhora na solucao
#passada como parametro
def reInsercao(distancias, solucao):

    distancia = solucao[0]
    rota = solucao[1]
    aux = 1
    while (aux != 0):
        aux = 0
        for i in range(1,len(rota)-1):
            for j in range(i+1, len(rota)-1):
                #se a soma das distancias entre as quantidades de arestas a sair for maior que a distancia
                #das arestas que irao entrar, significa que devo mover o vertice da posicao i para a j
                arestasASair = distancias[rota[i-1]][rota[i]] + distancias[rota[i]][rota[i+1]] + distancias[rota[j]][rota[j+1]]
                arestasAEntrar = distancias[rota[i-1]][rota[i+1]] + distancias[rota[i+1]][rota[j]] + distancias[rota[i+1]][rota[j+1]]
                if arestasASair >= arestasAEntrar:
                    rota = moverVertice(rota, i, j)
                    novaDistancia = caixeiroViajante(distancias, rota)
                    if novaDistancia < distancia:
                        distancia = novaDistancia
                        aux += 1
    return (distancia, rota)
    
                
def VND(distancias, solucao):

    fAtual = solucao[0]
    sAtual = solucao[1]
    #while que fica verificando se existe alguma solucao melhor executando o 2-opt e reinsercao
    #apos o 2-opt, executa-se o reinsercao, se houver um resultado melhor, passa o resultado para
    #o 2-opt e continua a execucao. O metodo se encerra quando 2-opt e reinsercao nao fornecem um
    #resultado melhor que o atual.
    while True:
        k = 1
        while k != 0:
            solucaoAux = twoOpt(distancias, solucao)
            fAux = solucaoAux[0]
            sAux = solucaoAux[1]
            if fAux < fAtual:
                fAtual = fAux
                sAtual = sAux
                solucao = (fAux, sAux)
                k += 1
            else:
                k = 0
        #chama o reinsercao com a solucao mais otima retornada do VND
        vizDistanteAux = reInsercao(distancias, solucao)
        fAux = solucaoAux[0]
        sAux = solucaoAux[1]
        #se o reinsercao retornar uma solucao melhor, atualiza e repassa essa solucao ao 2-opt
        #caso contrario ele encerra o metodo, pois nenhuma das duas heuristicas retornou um resultado melhor
        if fAux < fAtual:
            fAtual = fAux
            sAtual = sAux
            solucao = (fAux, sAux)
        else:
            break
    return (fAtual, sAtual)

#metaheuristica que chama o VND por uma quantidade de vezes passada por parametro
#sempre armazenando a melhor solucao
def multiStart(distancias, solucao, vertInicial, qtdVezes):
    distancia = sys.maxsize 
    for i in range(qtdVezes):
        solucaoAleatoria = construcaoAleatoria(distancias, solucao, vertInicial) #solucao aleatoria a ser passada ao VND
        solucaoLocal = VND(distancias, solucaoAleatoria)
        distanciaLocal = caixeiroViajante(distancias, solucaoLocal[1]) #distancia entre a solucao retornada pelo VND
        if distanciaLocal < distancia:
            solucao = solucaoLocal[1]
            distancia = distanciaLocal
    return (distancia, solucao)

#leitura do arquivo da instancia e parametros passado como argumento
with open(sys.argv[1]) as inputNumbers:
    lines = inputNumbers.read().splitlines()
    arquivo = [number for number in lines]
    distancias = []
    for i in range(3, len(arquivo)):
        distancias.append([int(number) for number in arquivo[i].split()])
    cidades = range(len(distancias))
    vertInicial = 0
    qtdVezes = int(sys.argv[2]) #quantidade de vezes que o multistart repetirá.
    
#distancias = [[0,2,1,4,9,1],[2,0,5,9,7,2],[1,5,0,3,8,6],[4,9,3,0,2,5],[9,7,8,2,0,2],[1,2,6,5,2,0]]
#cidades = range(len(distancias))
#vertInicial = 0
#distancias2 = [[0,0,1,4,9,1],[0,0,5,9,7,2],[1,5,0,3,8,6],[4,9,3,0,2,5],[9,7,8,2,0,2],[1,2,6,5,2,0]]
#print vizinhoMaisProximo(distancias, cidades, vertInicial)
#print vizinhoMaisDistante(distancias, cidades, vertInicial)
#print bellmoreENemhauser(distancias, cidades, vertInicial)
#print insercaoMaisBarata(distancias, cidades, vertInicial)
#solucao = solucaoAleatoria(distancias, cidades, vertInicial)
#print twoOpt(distancias, solucao)
#print reInsercao(distancias, solucao)
#print VND(distancias, solucao)
print multiStart(distancias, cidades, vertInicial, qtdVezes)
#print caixeiroViajante(distancias2, cidades)
