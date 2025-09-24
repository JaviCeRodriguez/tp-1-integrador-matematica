
from op_booleanas import *

OPERACIONES = {
    "^": AND,
    "v": OR,
    "~": NOT,
    "=>": IMPL,
}

def obtener_variables(funcion: str):
    """
    Obtiene las variables de la función
    Ejemplo:
    (pvq)^r -> ["p", "q", "r", (pvq)^r]
    """
    variables = []
    for caracter in funcion:
        if caracter.isalpha() and not caracter in OPERACIONES:
            variables.append(caracter)
    
    variables = list(set(variables))
    variables.append(funcion)

    return variables


def crear_matriz_combinaciones(variables: list):
    """
    Crea una matriz de combinaciones para la tabla de verdad
    Ejemplo:
    variables: ["p", "q", "pvq"]
    resultado: [["p", "q", "pvq"], [0, 0, None], [0, 1, None], [1, 0, None], [1, 1, None]]
    """
    matriz = []
    for i in range(2**(len(variables)-1)):
        binario = bin(i)[2:].zfill(len(variables)-1)
        combinacion = [int(bit) for bit in binario]
        combinacion.append(None)
        matriz.append(combinacion)
    return matriz


if __name__ == "__main__":
    funcion_test = "(pvq)^r"
    resultado = []

    # Obtener variables
    variables = obtener_variables(funcion_test)
    resultado.append(variables)

    # Crear matriz de combinaciones para tabla de verdad
    matriz = crear_matriz_combinaciones(variables)
    resultado = resultado + matriz

    print(resultado)