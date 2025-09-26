def imprimir_tabla(tabla):
    if not tabla:
        print("La tabla está vacía.")
        return
    
    # Calcularemos el ancho máximo para cada columna, se inicializa en 0 pero el número de columnas se saca del encabezado
    num_columnas = len(tabla[0])
    ancho_columnas = [0] * num_columnas

    # Recorremos cada celda para encontrar el texto más largo asi nos aseguramos que la columna se alinee correctamente.
    for fila in tabla:
        for i, celda in enumerate(fila):
            if len(str(celda)) > ancho_columnas[i]:
                ancho_columnas[i] = len(str(celda))
    
    # Este for es para imprimir el encabezado de la tabla
    encabezado = tabla[0]
    linea_encabezado = ""
    for i, item_encabezado in enumerate(encabezado):
        #Utilizando f-string formatting centramos el texto. Luego sumamos 2 al ancho para tener un espacio de relleno de cada lado.
        linea_encabezado += f" {item_encabezado:^{ancho_columnas[i]}} |"

    print(linea_encabezado[:-1])

    # Aquí agregamos una línea separadora (por ej: ---------)
    separar_linea = ""
    for ancho in ancho_columnas:
        separar_linea += "-" * (ancho + 2) + "+"

    print(separar_linea[:-1])

    #Imprimimos las filas de datos, se recorre la tabla desde la segunda fila en adelante (indice 1)
    for fila in tabla[1:]:
        linea_fila = ""
        for i, celda in enumerate(fila):
            linea_fila += f" {str(celda):^{ancho_columnas[i]}} |"

        print(linea_fila[:-1])
    

if __name__ == "__main__":
    resultados_prueba = [
        ['p', 'q', 'p->q'],
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 1],
        [0, 0, 1]
    ]

    print("Tabla de verdad para la proposición: p -> q")
    imprimir_tabla(resultados_prueba)

    print("\n" + "="*40 + "\n")
