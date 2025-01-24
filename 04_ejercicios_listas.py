#1. Crea una lista con los números del 1 al 5 e imprímela.

mi_lista = [1,2,3,4,5]
print(mi_lista) 

"""
2. Accede e imprime el tercer elemento de la lista [10, 20, 
30, 40, 50].
"""

mi_otra_lista = [10,20,30,40,50]
print(mi_otra_lista[3])

""" 
3. Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] 
e imprímela.
"""

mi_lista.append(6)
print(mi_lista)

""" 
4. Inserta el número 15 en la posición 2 de la lista [10, 
20, 30, 40, 50].
"""

mi_otra_lista.insert(1,15)
print(mi_otra_lista)

""" 
5. Elimina el primer valor 30 de la lista [10, 20, 30, 30, 
40, 50].
"""

mi_tercera_lista = [10,20,30,30,40,50]
mi_tercera_lista.remove(30)
print(mi_tercera_lista)

""" 
6. Usa la función pop() para eliminar el último elemento de 
la lista [1, 2, 3, 4, 5] y almacénalo en una variable. 
Imprime la variable y la lista. 
"""

pop_mi_lista= mi_lista.pop()
print(mi_lista)
print(pop_mi_lista)
"""
7. Invierte la lista [100, 200, 300, 400, 500] e imprímela. 
"""

mi_cuarta_lista = [100,200,300,400,500]
mi_cuarta_lista.reverse()
print(mi_cuarta_lista)
"""
8. Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e 
imprímela. 
"""
lista_nueva= [3,1,4,2,5]
lista_nueva.sort()
print(lista_nueva)
"""
9. Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el 
resultado en una nueva lista. Imprime la lista 
resultante. 
"""
lista_01 =[1,2,3]
lista_02= [4,5,6]

lista_total= lista_01 + lista_02 

print(lista_total)

"""
10. 
Crea una sublista con los elementos de la lista 
[10, 20, 30, 40, 50] que van desde la posición 1 hasta 
la 3 (sin incluir la posición 3). 
"""
lista_03 = [10,20,30,40,50]
print(lista_03 [1:3])