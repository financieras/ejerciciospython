'''Dada una lista de números enteros, positivos, calcular el segundo mínimo y decir que posición o posiciones ocupa en la lista.
'''
lista_original=[1,1,9,7,8,4,9,4,5]
print(lista_original,"Lista")
minimo=min(lista_original)
#print("minimo:",minimo)
lista_reducida=lista_original[:]
while minimo==min(lista_reducida):
    del lista_reducida[lista_reducida.index(minimo)]
#print(lista_reducida,"Lista reducida")
segundo=min(lista_reducida)
print("El segundo mínimo es",segundo)

#print("En la lista original ocupa la posición de índice:",lista_original.index(segundo))
print("En la Lista el segundo mínimo ocupa la posición o posiciones de indice:")
for i,v in enumerate(lista_original):
    if v==segundo:
        print(i)
