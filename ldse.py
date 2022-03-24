# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:34:22 2022

@author: PC
"""

"""Classe que representa o Nó"""

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
        self.quant +=1
            
    def removerInicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
        
    def imprimir(self):
        aux = self.prim
        while aux!= None:
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
    
    def removerElemento(self,valor):
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
            aux = ant = self.prim
            while aux.prox != None or aux.prox == None: 
              ant = aux
              aux = aux.prox
              if aux.info == valor:
                  ant.prox = aux.prox
                  if aux == self.prim:
                      self.prim = ant.prox
                  if aux == self.ult:
                      self.ult = ant                
                  self.quant -= 1   
                  
                
                
        
                