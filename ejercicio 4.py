def procesar_expresion():
    entrada = input("Ingrese la expresión: ")

    # Regla: Si solo está el par "()", error
    if entrada == "()":
        print("Hay un error en la expresión")
        return

    # Verificar si empieza con '(' y termina con ')'
    empieza_con = entrada.startswith("(")
    termina_con = entrada.endswith(")")

    # Regla: Si falta uno de los dos paréntesis (solo abierto o solo cerrado), error
    # Usamos XOR (^) para saber si solo uno de los dos es verdadero
    if empieza_con ^ termina_con:
        print("Hay un error en la expresión")
    
    # Regla: Si está contenida entre paréntesis, quitar solo los de más "afuera"
    elif empieza_con and termina_con:
        print(entrada[1:-1])
    
    # Regla: Si no está entre paréntesis, desplegar lo mismo
    else:
        print(entrada)

if __name__ == "__main__":
    procesar_expresion()
