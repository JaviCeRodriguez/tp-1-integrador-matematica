def evaluar_tipo(resultado):
    """
    Clasifique una función lógica como Tautología, Contradicción o Contingencia.

    Argumento:
    resultado (list): Una lista que representa la tabla de verdad. 
                      La primera fila son los encabezados, las siguientes
                      filas contienen los valores lógicos (0 o 1).
    """
    # Extraemos solo las filas de datos (ignorando la fila de encabezados [0])
    filas_de_datos = resultado[1:] 
    
    # Extraemos todos los valores de la última columna
    valores_finales = [fila[-1] for fila in filas_de_datos]
    
    # Inicializamos contadores para 1s y 0s
    hay_uno = False
    hay_cero = False
    
    # Iteramos sobre los valores finales
    for valor in valores_finales:
        if valor == 1:
            hay_uno = True
        elif valor == 0:
            hay_cero = True
    
    # Clasificación basada en los valores encontrados
    if hay_uno and hay_cero:
        tipo = "Contingencia"
    elif hay_uno and not hay_cero:
        tipo = "Tautología"
    elif not hay_uno and hay_cero:
        tipo = "Contradicción"
    else:
        # En caso de una lista vacía o solo valores no 0/1, lo que no debería pasar
        tipo = "Indefinido/Error" 

    print(f"La función es del tipo {tipo}")

# Ejemplo de uso con los datos parciales de la imagen:
# resultado = [
#     ["p", "q", "r", "(pvq)^r"],
#     [0, 0, 0, 0],
#     [0, 0, 1, 1],
#     # ... (filas intermedias)
#     [1, 1, 1, 0]
# ]
# 
# Si tuviéramos una tabla completa y con la proposición correcta, la función funcionaría.