import heapq

class Estado(object):
    def __init__(self, nome, custoEstimado):
        self.nome = nome
        self.custoEstimado = custoEstimado

    def addVizinhos(self, vizinho):
        self.vizinhos = vizinho

    def __repr__(self):
        return self.nome

class NoBusca(object):
    def __init__(self, estado, custo):
        self.estado = estado
        self.custo = custo

    def setPai(self, pai):
        self.pai = pai

    def __repr__(self):
        return self.estado.nome

class PriorityQueue(list):

    def push(self, elemento, prioridade, ultimaEstimativa):
        heapq.heappush(self,(prioridade+elemento.estado.custoEstimado - ultimaEstimativa, elemento))

    def pop(self):
        return heapq.heappop(self)

class Busca(object):

    def  __init__ (self, inicio, objetivo):
        self.inicio = NoBusca(inicio, 0)
        self.inicio.pai = None
        self.objetivo = objetivo

    def alterarFronteira(self, fronteira, noBusca, ultimaEstimativa):
        for i in fronteira:
            custoNo = i[0]
            no = i[1]

            if (no.estado.nome == noBusca.estado.nome):
                if(noBusca.custo < custoNo):
                   fronteira.push(noBusca, noBusca.custo, ultimaEstimativa)
                   return fronteira
                else:
                   return fronteira
        fronteira.push(noBusca, noBusca.custo, ultimaEstimativa)

    def procurarEstado(self, fronteira):
         return fronteira.pop()

    def busca(self):
        fronteira = PriorityQueue()
        fronteira.push(self.inicio, 0, 0)
        explorados = set()
        passos = 1
        ultimaEstimativa = 0

        while True:

            print("Passo: ", passos)
            print("Fronteira: ", fronteira)

            if (len(fronteira) == 0):
                return False

            novoEstadoI = self.procurarEstado(fronteira)
            novoEstado = novoEstadoI[1]
            custoNovoEstado = novoEstadoI[0]

            explorados.add(novoEstado.estado)

            if(novoEstado.estado == self.objetivo):
                print("Explorado; ", novoEstado)
                return novoEstado

            for i in novoEstado.estado.vizinhos:
                estado = i[0]
                custoEstado = i[1]
                ultimaEstimativa = novoEstado.estado.custoEstimado

                if estado not in explorados:
                    estadoAux = NoBusca( estado, custoEstado+custoNovoEstado)
                    self.alterarFronteira(fronteira, estadoAux, ultimaEstimativa)
                    estadoAux.setPai(novoEstado)

            print("Explorado: ", novoEstado, "\n")
            passos += 1
    

joaoPessoa = Estado("joao pessoa",460)
itabaiana = Estado("itabaiana",360)
campinaGrande = Estado("campina grande",300)
santaRita = Estado("santa rita",451)
mamanguape = Estado("mamanguape", 380)
guarabira = Estado("guarabira", 340)
areia = Estado("areia", 316)
coxixola = Estado("coxixola", 232)
soledade = Estado("soledade",243)
picui = Estado("picui",250)
monteiro = Estado("monteiro", 195)
patos = Estado("patos", 122)
pombal = Estado("pombal", 55)
itaporanga = Estado("itaporanga", 65)
catoleDoRocha = Estado("catole do rocha", 110)
sousa = Estado("sousa", 20)
cajazeiras = Estado("cajazeiras",0)

joaoPessoa.addVizinhos([(itabaiana, 68), (campinaGrande, 125), (santaRita, 26)])
itabaiana.addVizinhos([(joaoPessoa, 68), (campinaGrande, 65)])
santaRita.addVizinhos([(joaoPessoa, 26), (mamanguape, 64)])
mamanguape.addVizinhos([(santaRita, 64), (guarabira, 42)])
guarabira.addVizinhos([(mamanguape, 42), (areia, 41)])
areia.addVizinhos([(guarabira, 41), (campinaGrande, 40)])
campinaGrande.addVizinhos([(itabaiana, 65), (areia, 40), (soledade, 58), (coxixola, 128), (joaoPessoa, 125)])
soledade.addVizinhos([(campinaGrande, 58), (patos, 117), (picui, 69)])
picui.addVizinhos([(soledade, 68)])
coxixola.addVizinhos([(campinaGrande, 128), (monteiro, 83)])
patos.addVizinhos([(soledade, 117), (itaporanga, 108), (pombal, 71)])
monteiro.addVizinhos([(coxixola, 83), (itaporanga, 224)])
catoleDoRocha.addVizinhos([(pombal, 57)])
pombal.addVizinhos([(patos, 71), (catoleDoRocha, 57), (sousa, 56)])
itaporanga.addVizinhos([(patos, 108), (cajazeiras, 121), (monteiro, 224)])
sousa.addVizinhos([(pombal, 56), (cajazeiras, 43)])
cajazeiras.addVizinhos([(sousa, 43), (itaporanga, 121)])
    

busca = Busca(joaoPessoa, cajazeiras)
ultimoEstado = busca.busca()

def printCaminho(estado):
    estadoPai = estado.pai
    print(estado)

    while estadoPai:
        print(estadoPai)
        estadoPai = estadoPai.pai

print("")
printCaminho(ultimoEstado)
















            
