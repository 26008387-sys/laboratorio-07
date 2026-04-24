def procesar_expresion():
    entrada = input("Ingrese la expresión: ")

    if entrada == "()":
        print("Hay un error en la expresión")
        return

    empieza_con = entrada.startswith("(")
    termina_con = entrada.endswith(")")
    if empieza_con ^ termina_con:
        print("Hay un error en la expresión")
    elif empieza_con and termina_con:
        print(entrada[1:-1])
    else:
        print(entrada)

if __name__ == "__main__":
    procesar_expresion()
