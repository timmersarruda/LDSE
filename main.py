import ldse

lista = ldse.Ldse()

if not lista.estahVazia():
    lista.removerInicio()

lista.inserirInicio('7')
lista.inserirInicio('7')
lista.inserirInicio('6')
lista.inserirInicio('5')
lista.inserirInicio('4')
lista.inserirInicio('7')
lista.inserirInicio('3')
lista.inserirInicio('2')
lista.inserirInicio('1')
lista.inserirInicio('7')

print("#####################################")
print("############### L D S E #############")

lista.imprimir()

print("#######################################")
print(" # Removendo todos os elementos ... 7", lista.removerTodas('7'))
lista.imprimir()

print("#######################################")
print(" # Inserindo '9' na posição 3... ", lista.inserirPosicao('9', 3))
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
print(" # Removendo o elemento 4... ", lista.removerElemento('4'))
lista.imprimir()



print("#######################################")
print("Somando todos os elementos... ", lista.somarElementos())
lista.imprimir()
