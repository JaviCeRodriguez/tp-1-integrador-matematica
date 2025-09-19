"""
- Inicia el programa
- Se pide al usuario ingresar una proposición compuesta
- Analizar la proposición
  - Cantidad de variables
  - Agrupar en términos a evaluar
  - "Transformar" operaciones dadas por usuario en operadores lógicos
- Ejecutar todas las operaciones con distintas combinaciones de 0 y 1 en las variables
- Imprimir la tabla de verdad con formato lindo (usar módulo pprint?)
- A partir del resultado final, entender si es tautología, contradicción o contingencia
"""

def generar_tabla(resultado):
    """
    Se imprime tabla con formato para que se pueda
    leer bien los inputs y el resultado
    """
    return ""

def analizar_proposicion(proposicion):
    """
    Devuelve:
    [
        ["p", "q", "r", "(pvq)^r"],
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        .
        .
        .
        [1, 1, 1, 0]
    ]
    """
    return None

def user_input():
    return "a^b"

def main():
    proposicion_str = user_input()
    resultado = analizar_proposicion(proposicion_str)
    tabla = generar_tabla(resultado)
    print(tabla)
