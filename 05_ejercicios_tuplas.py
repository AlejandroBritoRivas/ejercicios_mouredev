"""
1. Crea una tupla con los valores (10, 20, 30, 40, 50) e 
imprímela. 
"""

tupla_01= (10,20,30,40,50)
print(tupla_01)

"""
2. Accede al segundo elemento de la tupla (100, 200, 300, 
400, 500) y muéstralo. 
"""

tupla_02= (100,200,300,400,500)
print(tupla_02[1])

"""
3. Intenta modificar el primer elemento de la tupla (1, 2, 
3) a 10 y observa el resultado. 

"""

tupla_03 = (1,2,3)
tupla_03.append = (10)
#AttributeError: 'tuple' object has no attribute 'append' and no __dict__ for setting new attributes

"""
4. Cuenta cuántas veces aparece el número 3 en la tupla (1, 
2, 3, 3, 4, 5, 3). 
"""

tupla_04 = (1, 2, 3, 3, 4, 5, 3)
print(tupla_04.count(3))

"""
5. Encuentra el índice de la primera aparición de la cadena 
"Python" en la tupla ("Java", "Python", "JavaScript", 
"Python"). 
"""

tupla_05= ("Java", "Python", "JavaScript", "Python")
print(tupla_05.index("Python"))

"""
6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la 
tupla resultante. 
"""

tupla_06 =(1,2,3)
tupla_07 =(4,5,6)
suma_tuplas= tupla_06 + tupla_07
print(suma_tuplas)

"""
7. Crea una subtupla con los elementos desde la posición 2 
hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 
40, 50). 
"""
print(tupla_01[1:4])
"""
8. Convierte la tupla ("rojo", "verde", "azul") en una 
lista, cambia el segundo elemento a "amarillo" y vuelve 
a convertirla en una tupla. Imprime la tupla resultante. 
"""
tupla_08 = ("rojo", "verde", "azul")
tupla_08 = list(tupla_08)
tupla_08.remove("azul")
tupla_08.append("amarillo")
tupla_08 = tuple(tupla_08)
print(tupla_08)

"""
9. Elimina una tupla llamada my_tuple usando del y luego 
intenta imprimirla para ver el resultado. 
"""
my_tuple = (1,2,3)
print(my_tuple)
del my_tuple
print(my_tuple)
#NameError: name 'my_tuple' is not defined
"""
10. 
Crea una tupla con un solo elemento (el número 100) 
e imprímela. Asegúrate de usar la sintaxis correcta para 
crear una tupla con un solo elemento.
"""
tupla_09= (100)
print(tupla_09)