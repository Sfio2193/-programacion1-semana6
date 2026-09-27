with open("tareas.txt", "r", encoding="utf-8") as archivo: #Abre el archivo "tareas.txt" en modo lectura ("r") con codificación "utf-8" y le asigna el alias "archivo" para usarlo de forma segura (with garantiza que se cierre solo al terminar.)   
    for linea in archivo: #Recorre el archivo línea por línea
        print(linea.strip()) #Imprime el contenido, sacando los espacios y saltos de línea

#Sin el strip, imprime un salto de línea por cada print realizado
#FileNotFoundError si se cambia el nombre de "tareas.txt"