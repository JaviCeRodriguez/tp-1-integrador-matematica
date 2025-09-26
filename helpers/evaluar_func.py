
from helpers.op_booleanas import *

OPERACIONES = {
    "^": AND,
    "v": OR,
    "~": NOT,
    "=>": IMPL,
    "<=>": XIMPL
}

def obtener_variables(funcion: str):
    """
    Extrae las variables únicas de una expresión booleana.
    
    Args:
        funcion: String con la expresión booleana (ej: "(pvq)^r")
    
    Returns:
        list: Lista con las variables únicas encontradas más la función original
        
    Ejemplo:
        obtener_variables("(pvq)^r") -> ["p", "q", "r", "(pvq)^r"]
        obtener_variables("~(pvq)^(r^~t)=>t") -> ["p", "q", "r", "t", "~(pvq)^(r^~t)=>t"]
    """
    variables = []
    for caracter in funcion:
        if caracter.isalpha() and not caracter in OPERACIONES and not caracter in variables:
            variables.append(caracter)
    
    variables.append(funcion)

    return variables


def crear_matriz_combinaciones(variables: list):
    """
    Genera todas las combinaciones posibles de 0 y 1 para las variables.
    
    Args:
        variables: Lista con las variables (la última es la función a evaluar)
    
    Returns:
        list: Matriz con todas las combinaciones binarias, cada fila termina en None
        
    Ejemplo:
        variables = ["p", "q", "pvq"]
        resultado = [
            ["p", "q", "pvq"],
            [0, 0, None],
            [0, 1, None],
            [1, 0, None],
            [1, 1, None]
        ]
    """
    matriz = []
    for i in range(2**(len(variables)-1)):
        binario = bin(i)[2:].zfill(len(variables)-1)
        combinacion = [int(bit) for bit in binario]
        combinacion.append(None)
        matriz.append(combinacion)
    return matriz


def evaluar_funcion(matriz: list) -> list:
    """
    Evalúa la función booleana para cada combinación de valores de variables.
    
    Args:
        matriz: Lista de listas donde la primera fila contiene las variables
                y la función, y las siguientes filas contienen combinaciones
                de valores con None en la última columna
    
    Returns:
        list: Matriz completa con todos los None reemplazados por los
              resultados de la evaluación (0 o 1)
        
    Ejemplo:
        matriz = [
            ["p", "q", "pvq"],
            [0, 0, None],
            [0, 1, None],
            [1, 0, None],
            [1, 1, None]
        ]
        resultado = [
            ["p", "q", "pvq"],
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
    """
    # Obtener la función a evaluar (última columna del header)
    funcion = matriz[0][-1]
    variables = matriz[0][:-1]  # Todas las variables excepto la función
    
    # Crear una copia de la matriz para no modificar la original
    resultado = [fila[:] for fila in matriz]
    
    # Evaluar cada fila de combinaciones (saltando el header)
    for i in range(1, len(matriz)):
        # Crear diccionario con los valores de las variables para esta fila
        valores = {}
        for j, variable in enumerate(variables):
            valores[variable] = matriz[i][j]
        
        # Evaluar la función con estos valores
        resultado[i][-1] = evaluar_expresion(funcion, valores)
    
    return resultado


def evaluar_expresion(expresion: str, valores: dict) -> int:
    """
    Evalúa expresiones booleanas complejas con paréntesis.
    
    Args:
        expresion: String con la expresión booleana (ej: "(pvq)^r")
        valores: Diccionario con los valores de las variables (ej: {"p": 1, "q": 0, "r": 1})
    
    Returns:
        int: Resultado de la evaluación (0 o 1)
        
    Nota:
        Maneja paréntesis y respeta la precedencia de operadores:
        NOT > AND > OR > IMPL > XIMPL
    """
    # Reemplazar variables con sus valores
    expr = expresion
    for variable, valor in valores.items():
        expr = expr.replace(variable, str(valor))
    
    # Convertir a lista de tokens
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i] in "()":
            tokens.append(expr[i])
            i += 1
        elif expr[i] in "01":
            tokens.append(int(expr[i]))
            i += 1
        elif expr[i:i+3] == "<=>":
            tokens.append(expr[i:i+3])
            i += 3
        elif expr[i:i+2] in ["=>", "<="]:
            tokens.append(expr[i:i+2])
            i += 2
        elif expr[i] in "^v~":
            tokens.append(expr[i])
            i += 1
        else:
            i += 1
    
    # Evaluar usando precedencia: NOT, AND, OR, IMPL, XIMPL
    return evaluar_tokens(tokens)


def evaluar_tokens(tokens: list) -> int:
    """
    Evalúa una lista de tokens respetando la precedencia de operadores.
    
    Args:
        tokens: Lista de tokens que puede contener:
               - Números (0, 1)
               - Paréntesis ()
               - Operadores (^, v, ~, =>, <=>)
    
    Returns:
        int: Resultado final de la evaluación (0 o 1)
        
    Algoritmo:
        1. Resuelve paréntesis recursivamente
        2. Aplica operadores en orden de precedencia:
           NOT > AND > OR > IMPL > XIMPL
        3. Reemplaza pares de operandos con su resultado
    """
    # Manejar paréntesis
    while "(" in tokens:
        inicio = -1
        fin = -1
        for i, token in enumerate(tokens):
            if token == "(":
                inicio = i
            elif token == ")":
                fin = i
                break
        
        if inicio != -1 and fin != -1:
            # Evaluar contenido de los paréntesis
            contenido = tokens[inicio+1:fin]
            resultado = evaluar_tokens(contenido)
            # Reemplazar paréntesis con el resultado
            tokens = tokens[:inicio] + [resultado] + tokens[fin+1:]
        else:
            break
    
    # Aplicar operadores en orden de precedencia
    # NOT
    i = 0
    while i < len(tokens):
        if tokens[i] == "~":
            if i + 1 < len(tokens):
                tokens[i] = NOT(tokens[i + 1])
                tokens.pop(i + 1)
            else:
                break
        else:
            i += 1
    
    # AND
    i = 0
    while i < len(tokens):
        if tokens[i] == "^":
            if i > 0 and i + 1 < len(tokens):
                resultado = AND(tokens[i - 1], tokens[i + 1])
                tokens[i - 1] = resultado
                tokens.pop(i)
                tokens.pop(i)
                i -= 1
            else:
                break
        else:
            i += 1
    
    # OR
    i = 0
    while i < len(tokens):
        if tokens[i] == "v":
            if i > 0 and i + 1 < len(tokens):
                resultado = OR(tokens[i - 1], tokens[i + 1])
                tokens[i - 1] = resultado
                tokens.pop(i)
                tokens.pop(i)
                i -= 1
            else:
                break
        else:
            i += 1
    
    # IMPL
    i = 0
    while i < len(tokens):
        if tokens[i] == "=>":
            if i > 0 and i + 1 < len(tokens):
                resultado = IMPL(tokens[i - 1], tokens[i + 1])
                tokens[i - 1] = resultado
                tokens.pop(i)
                tokens.pop(i)
                i -= 1
            else:
                break
        else:
            i += 1
    
    # XIMPL
    i = 0
    while i < len(tokens):
        if tokens[i] == "<=>":
            if i > 0 and i + 1 < len(tokens):
                resultado = XIMPL(tokens[i - 1], tokens[i + 1])
                tokens[i - 1] = resultado
                tokens.pop(i)
                tokens.pop(i)
                i -= 1
            else:
                break
        else:
            i += 1
    
    return tokens[0] if tokens else 0


if __name__ == "__main__":
    funcion_test = "~(pvq)^(r^~t)=>t"
    resultado = []

    # Obtener variables
    variables = obtener_variables(funcion_test)
    resultado.append(variables)

    # Crear matriz de combinaciones para tabla de verdad
    matriz = crear_matriz_combinaciones(variables)
    resultado = resultado + matriz


    resultado = evaluar_funcion(resultado)

    for r in resultado:
        print(r)