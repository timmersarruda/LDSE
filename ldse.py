class No:
    def __init__(self, info, proximo):
        self.info = info
        self.prox = proximo


"CLasse que inicia a lista dinâmica simplesmente encadeada"


class Ldse:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def estahVazia(self):
        return self.quant == 0

    def inserirInicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.prim = No(valor, self.prim)
        self.quant += 1

    def inserirFim(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1

    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1

    def imprimir(self):
        aux = self.prim
        while aux != None:
            print(aux.info, end=' ')
            aux = aux.prox
            print()

    def getQuant(self):
        return self.quant

    def removerFim(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            aux = self.prim
            while aux.prox != self.ult:
                aux = aux.prox
            aux.prox = None
            self.ult = aux
        self.quant -= 1

    def getFirstElement(self):
        if not self.estahVazia():
            return self.prim.info

    def getLastElement(self):
        if not self.estahVazia():
            return self.ult.info

    def removerElemento(self, valor):
        if self.quant == 1:
            if (self.prim.info == valor):
                self.prim = self.ult = None
                self.quant -= 1
        else:
            aux = ant = self.prim
            while aux.prox != None and aux.info != valor:
                ant = aux
                aux = aux.prox
            if aux.info == valor:
                ant.prox = aux.prox
                if aux == self.prim:
                    self.prim = ant.prox
                if aux == self.ult:
                    self.ult = ant
                self.quant -= 1

    def removerTodas(self, valor):
        if self.quant == 1:
            if self.prim.info == valor:
                self.prim = self.ult = None
            self.quant -= 1
        else:
            if self.prim.info == valor:
                self.prim = self.prim.prox
                self.quant -= 1
            aux = ant = self.prim
            while aux.prox != None:
                ant = aux
                aux = aux.prox
                if aux.info == valor and aux.prox != None:
                    ant.prox = aux.prox
                    if aux == self.prim:
                        self.prim = ant.prox
                    if aux == self.ult:
                        self.ult = ant
                    self.quant -= 1
            aux = ant = self.prim
            if self.ult.info == valor:
                while aux.prox != None:
                    ant = aux
                    aux = aux.prox
                aux = ant
                aux.prox = None
                self.ult = aux
                self.quant -= 1

    def inserirPosicao(self, valor, posicao):
        ant =  aux = self.prim
        cont = 1
        while cont != posicao:
            cont += 1
            ant = aux
            aux = aux.prox
        if cont == 1:
            self.prim.prox = aux.prox
            self.prim = No(valor, self.prim.prox)
        if cont == self.quant:
            self.ult.prox = self.ult = No(valor, None)
        else:
            ant.prox = No(valor, aux)
        self.quant += 1
        
    def somarElementos(self):
        aux = ant = self.prim
        soma = ""
        while aux.prox != None:
            soma += aux.info
            ant = aux
            aux = aux.prox
        soma += self.ult.info
        self.ult.prox = self.ult = No(soma, None)
