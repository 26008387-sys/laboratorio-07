def leer_notas():
    n = int(input("¿Cuántas notas vas a ingresar?: "))
    lista_notas = []
    for i in range(n):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        lista_notas.append(nota)
    return lista_notas
# 2. Función para calcular el promedio
def calcular_promedio(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)
# 3. Función para determinar la letra del grado
def obtener_grado(promedio):
    if promedio >= 90:
        return "A"
    elif promedio >= 80:
        return "B"
    elif promedio >= 70:
        return "C"
    elif promedio >= 61:
        return "D"
    else:
        return "F"
# 4. Subrutina principal (main)
def main():
    notas_estudiante = leer_notas()
    promedio_final = calcular_promedio(notas_estudiante)
    grado_letra = obtener_grado(promedio_final)
    # Despliegue de resultados
    print("\n--- Resultados ---")
    print(f"Lista de notas: {notas_estudiante}")
    print(f"Promedio: {promedio_final:.2f}")
    print(f"Grado del estudiante: {grado_letra}")
if __name__ == "__main__":
    main()
