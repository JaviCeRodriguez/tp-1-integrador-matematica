from helpers.op_booleanas import AND, OR, NOT, COND, BICOND

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
