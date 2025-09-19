# Clasificador de Proposiciones Compuestas

Permitan al usuario ingresar una proposición compuesta (por ejemplo, p∨¬p, p∧¬p o p⇒q).
El programa debe generar la tabla de verdad y clasificarla como tautología, contradicción o contingencia según corresponda

## Flujo de funcionamiento del programa

1. Inicia el programa
2. Se pide al usuario ingresar una proposición compuesta
3. Analizar la proposición

- Cantidad de variables
- Agrupar en términos a evaluar
- "Transformar" operaciones dadas por usuario en operadores lógicos

4. Ejecutar todas las operaciones con distintas combinaciones de 0 y 1 en las variables
5. Imprimir la tabla de verdad con formato lindo (usar módulo pprint?)
6. A partir del resultado final, entender si es tautología, contradicción o contingencia

## Convención a utilizar para las operaciones y sus funciones

- AND(a, b): ^
- OR(a, b): v
- NOT(a): ~
- COND(a, b): =>
- BICOND(a, b): <=>

## Ejemplo

- input: p ^ q ^ (~p v r)
- código: AND(p, AND(q, OR(NOT(p), r))))
