lineas = 0
palabras = 0
with open("tareas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        #Ignoramos la líneas vacías si las hubiera para evitar contar de más
        if linea.strip() != "":
           #lineas = lineas + 1
           lineas += 1
           palabras = palabras + len(linea.split())
           #palabras += len(linea.split())

#Mostramos el resultado 
print(f"El archivo tiene {lineas} lineas y {palabras} palabras.")