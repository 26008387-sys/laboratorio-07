import sys

# Verificamos que se pasen los argumentos necesarios
if len(sys.argv) < 3:
    print("Uso: hola nombre_archivo mundo")
else:
    nombre_archivo = sys.argv[1]
    mundo = sys.argv[2]

    try:
        # Abrimos el archivo en modo lectura ('r')
        with open(nombre_archivo, "r") as archivo:
            # Recorremos el archivo línea por línea
            for linea in archivo:
                # Si la palabra está en la línea, la imprimimos
                if mundo in linea:

                    print(linea.strip())
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
