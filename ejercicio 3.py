def ejecutar_programa():
   
    entrada = input("Ingrese numero de lineas a escribir: ")

    # Validación básica para asegurar que sea un número
    if not entrada.isdigit():
        print("Error: Debe ingresar un número entero positivo.")
        return
    n = int(entrada)
    if n > 0:
        try:
            with open("resultado.txt", "w", encoding="utf-8") as archivo:
                for i in range(1, n + 1):
                    # Pedir la línea al usuario
                    linea = input(f"Ingrese linea #{i} - ")         
                    archivo.write(linea + "\n")
            print(f"\nProceso terminado. Se guardaron {n} líneas en 'resultado.txt'.")
        except IOError:
            print("Hubo un error al intentar escribir en el archivo.")
    else:
        print("El número ingresado no es mayor a 0. No se creó ningún archivo.")

if __name__ == "__main__":
    ejecutar_programa()
