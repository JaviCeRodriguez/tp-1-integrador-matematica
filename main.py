from helpers.validador_input import validacion_de_funciones
from helpers.evaluar_func import obtener_variables, crear_matriz_combinaciones, evaluar_funcion
from helpers.formatear_results import imprimir_tabla
from helpers.clasificacion_resultado import evaluar_tipo

def main():
    resultado = []

    proposicion_str = validacion_de_funciones()

    variables = obtener_variables(proposicion_str)
    resultado.append(variables)

    matriz = crear_matriz_combinaciones(variables)
    resultado = resultado + matriz

    resultado = evaluar_funcion(resultado)

    evaluar_tipo(resultado)

    imprimir_tabla(resultado)


if __name__ == "__main__":
    main()
