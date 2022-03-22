# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:33:53 2022

@author: PC
"""

import ldse

lista = ldse.Ldse()

if not lista.estahVazia():
    lista.removerInicio()

lista.inserirInicio('F')
lista.inserirInicio('E')
lista.inserirInicio('D')
lista.inserirInicio('C')
lista.inserirInicio('B')
lista.inserirInicio('A')

print("#####################################")
print("############### L D S E #############")

lista.imprimir()

print("#####################################")
print(" # Tamanho da lista:" , lista.getQuant())

print("#####################################")
print(" # Consultando primeiro elemento... ")
print(" Primeiro elemento da lista: ", lista.getFirstElement())

print("#######################################")
print(" # Consultando ultimo elemento... ")
print("Último elemento da lista: ", lista.getLastElement())

print("#######################################")
print(" # Removendo o primeiro elemento...", lista.removerInicio())
lista.imprimir()


print("#######################################")
print(" # Removendo o último elemento...", lista.removerFim())
lista.imprimir()

print("#######################################")
print(" # Removendo o elemento D... ", lista.removerElemento('D'))
lista.imprimir()



