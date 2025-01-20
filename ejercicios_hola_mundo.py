#1. Imprime "¡Hola Mundo!" por consola.

print("¡Hola Mundo!")
      
#2. Escribe un comentario de una sola línea explicando qué hace el código del Ejercicio 1.

print("¡Hola Mundo!") #Este codigo imprime en pantalla el texto de "¡Hola Mundo!"
      

#3. Imprime tu nombre y edad en la misma línea utilizando la función print.

print("Alejandro Brito 30 años")

#4. Usa la función type() para imprimir el tipo de dato de una cadena de texto, un número entero y un número decimal.

print(type("Alejandro"))
print(type(2))
print (type(3.5))

#5. Escribe un comentario en varias líneas explicando qué son los tipos de datos en Python.

"""
esto deberia ser un comentario
que abacrca varias lineas
"""
#6. Imprime el resultado de concatenar dos cadenas de texto, por ejemplo: "Hola" y "Mundo".

cadena_1= "Hola "
cadena_2= "Mundo"

concatenar= cadena_1 + cadena_2 

print(concatenar)

#7. Crea una variable para almacenar tu nombre, otra para tu edad, e imprime ambas en la misma línea.

nombre= "Alejandro"
edad= 30 

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

#8. Escribe un programa que solicite al usuario su nombre y lo imprima junto con un saludo.

nombre = input("Dime tu nombre: ")

print(f"Hola {nombre}, en que puedo ayudarte?")

#9. Usa print() para mostrar el resultado de la suma de dos números enteros y el tipo de dato resultante.

primer_numero=int(input("Dime un numero: "))    
segundo_numero=int(input("Dime otro numero: ")) 

suma= primer_numero + segundo_numero            

print( suma , type(suma))                      

#10. Comenta el código del Ejercicio 9, y explica qué hace cada línea usando comentarios de una sola línea.

primer_numero=int(input("Dime un numero: "))    # le pido al usuario el primer numero y lo guardo en la variable llamada primer_numero.
segundo_numero=int(input("Dime otro numero: ")) # le pido al usuario el segundo numero y lo guardo en la variable llamada segundo_numero.

suma= primer_numero + segundo_numero            # Creo la variable suma y hago la operacion sumando las dos variables que me dio el usuario.

print( suma , type(suma))                       # con la funcion print imprimo en pantalla el resultado de la suma y con la concatenacion (,) le añado la funcion type para que me devuelva el tipo del resultado de la operacion 


