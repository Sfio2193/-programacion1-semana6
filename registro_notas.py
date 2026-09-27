print("Registro de notas — Programación I")
notas = []

nota = int(input("Ingrese una nota (<=0 para terminar): "))

while nota > 0:
    assert nota <= 10, "La nota debe estar entre 1 y 10"
    notas.append(nota)
    nota = int(input("Ingrese una nota (<=0 para terminar): "))

if len(notas) == 0:
    print("No se cargaron notas.")
else:
    promedio = sum(notas) / len(notas)

    invertida = []
    for n in notas:
        invertida.insert(0, n)

        registro_cerrado = tuple(notas)    

        print(f"\nNotas cargadas: {notas}")
        print(f"Cantidad: {len(notas)} | Mayor: {max(notas)} | Menor: {min(notas)}")
        print(f"Promedio: {promedio:.2f}")
        print(f"De la última a la primera: {invertida}")
        print(f"Registro cerrado: {registro_cerrado}")