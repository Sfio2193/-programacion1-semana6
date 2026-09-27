# PARTE 1 - CADENAS

# Ejercicio 1.1
palabra = input("Ingrese una palabra: ")
print(f"En mayúscula es {palabra.upper()}")
print(f"En minúscula es {palabra.lower()}")
print(f"En capatalizada es {palabra.capitalize()}")

# Ejercicio 1.2
frase = input("Ingrese una frase: ")
palabras = frase.split()
print(f"La frase tiene {len(palabras)} palabras")

# Ejercicio 1.3
palabra = input("Ingrese una palabra: ")
resultado = ""
for letra in palabra:
    if letra.lower() in "aeiou": 
            resultado = resultado + "*"
    else:
            resultado = resultado + letra
print(f"Resultado: {resultado}")

# Ejercicio 1.4
palabra = input("Ingrese una palabra: ")
print(f"Primeros 3: {palabra[:3]}")
print(f"Últimos 3: {palabra[-3:]}")    
print(f"Invertida: {palabra[::-1]}")


# PARTE 2 - LISTAS

# Ejercicio 2.1
numeros = []
for i in range(5):
         numeros.append(int(input("Ingrese un número: ")))
print(f"Lista: {numeros}")
print(f"Mayor: {max(numeros)} | Menor: {min(numeros)}")

# Ejercicio 2.2
frutas = ["pera", "banana", "manzana"]
frutas.append("uva")     
frutas.remove("banana")  
print(frutas)

# Ejercicio 2.3
lista = [1, 2, 3, 4, 5]
invertida = []
for elemento in lista:
    invertida.insert(0, elemento)
print(f"Original:  {lista}")
print(f"Invertida: {invertida}")


# PARTE 3 - LISTAS ANIDADAS (MATRICES)

# Ejercicio 3.1
matriz = []
for f in range(2):
    fila = []
    for c in range(2):
        fila.append(int(input(f"Ingrese el valor [{f}][{c}]: ")))
    matriz.append(fila)
print("Matriz ingresada")
for f in range(2):
    for c in range(2):
        print(matriz[f] [c], end=" ")
    print()

# Ejercicio 3.2
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
suma = 0
for f in range(len(matriz)):
    for c in range(len(matriz[0])):
        suma = suma + matriz[f][c]
print(f"La suma de todos los elementos es: {suma}")


# PARTE 4 - TUPLAS

# Ejercicio 4.1
numeros = (10, 25, 3, 47, 8)
print(f"Primero: {numeros[0]} | Último: {numeros[-1]}")

# Ejercicio 4.2
notas_lista = [8, 6, 9, 7]
notas = tuple(notas_lista)         
promedio = sum(notas) / len(notas)
print(f"Las notas fueron: {notas}")
print(f"El promedio es: {promedio}")

# Ejercicio 4.3
colores = ("rojo", "verde", "azul")
c1, c2, c3 = colores              
print(f"Color 1: {c1} / Color 2: {c2} / Color 3: {c3}")