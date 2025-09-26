from helpers.validador_input import validacion_de_funciones
from helpers.evaluar_func import obtener_variables, crear_matriz_combinaciones, evaluar_funcion


def main():
    resultado = []

    proposicion_str = validacion_de_funciones()

    variables = obtener_variables(proposicion_str)
    resultado.append(variables)

    matriz = crear_matriz_combinaciones(variables)
    resultado = resultado + matriz

    resultado = evaluar_funcion(resultado)

    print(resultado)


if __name__ == "__main__":
    main()
