def validacion_de_funciones():
    operadores = ['^', 'v', '~', '=>', '<=>'] #operadores permitidos
    fun_bool = input(f"Escriba la función booleana, usando los siguientes operadores {', '.join(operadores)}: ") #(a^b) v (~c), por ejemplo

    func_aux = ""
    for c in fun_bool:
        if not c.isalpha() or c == 'v':
            func_aux += c
    
    func_aux = func_aux.replace("<=>", "").replace("=>", "").replace("~", "").replace("v", "").replace("^", "").replace("(", "").replace(")", "")

    if func_aux == "":
        print("Función correctamente verificada. Procediendo a evaluar...")
        return fun_bool
    else:
        raise ValueError(f"Función inválida. Solo se permiten los operadores {', '.join(operadores)} y letras (que no sea v)")
