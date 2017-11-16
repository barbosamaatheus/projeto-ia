import random

class PriorityQueue(object):

    def push(self, elemento, prioridade):
        heapq.heappush(self, (priodirade))

    def pop(self):
        return heapq.heappop(self)
    
def calcularErrados(object):
    k=0
    matrizPerfeita = [[1,2,3],[4,5,6],[7,8,0]]
    for i in range(3):
        for j in range(3):
            if(object[i][j] != matrizPerfeita[i][j]):
                k+=1
    return k
def busca(matriz):
    frontiera = PriorityQueue()
    x= calcularErrados(matriz)
    fronteira.push(self, matriz,x)
    while(True):
        p = obterPosicaoVazia(object)
        if(p[0]==1):
            nova = cima(matriz)
            fronteira.push(self, nova, calcularErrados(matriz))
            nova2 = baixo(matriz)
            fronteira.push(self, nova2, calcularErrados(matriz))
            if(p[1]==1):
                nova3 = direita(matriz)
                fronteira.push(self, nova3, calcularErrados(matriz))
                nova4 = esquerda(matriz)
                fronteira.push(self, nova4, calcularErrados(matriz))
                
         
                
        
def obterPosicaoVazia(object):
    posicao = []
    for i in range(3):
        for j in range(3):
            if(object[i][j]==0):
                posicao.append(i)
                posicao.append(j)
    return posicao

def cima(object):
    x = object
    p = obterPosicaoVazia(object)
    x[p[0]][p[1]] = x[p[0]-1][p[1]]
    x[p[0]-1][p[1]] = 0
    return x

def baixo(object):
    x = object
    p = obterPosicaoVazia(object)
    x[p[0]][p[1]] = x[p[0]+1][p[1]]
    x[p[0]+1][p[1]] = 0
    return x

def direita(object):
    x = object
    p = obterPosicaoVazia(object)
    x[p[0]][p[1]] = x[p[0]][p[1]+1]
    x[p[0]][p[1]+1] = 0
    return x

def esquerda(object):
    x = object
    p = obterPosicaoVazia(object)
    x[p[0]][p[1]] = x[p[0]][p[1]-1]
    x[p[0]][p[1]-1] = 0
    return x
      

matriz = []
matriz1 = [] 
for i in range(3):
     matriz.append([])
     for j in range(3):
         num = random.randint(0,8)
         while(num in matriz1):
             num = random.randint(0,8)
         matriz[i].append(num)
         matriz1.append(num)

def mostrarMatriz(object):
    for i in range(len(object)):
        for j in range(len(object[i])):
            print(object[i][j], end=" ")
        print ("\n")
        
print(mostrarMatriz(matriz))
print(calcularErrados(matriz))
print(obterPosicaoVazia(matriz))
print(mostrarMatriz(cima(matriz)))
print(mostrarMatriz(direita(matriz)))
print(mostrarMatriz(baixo(matriz)))
print(mostrarMatriz(esquerda(matriz)))

