# Bloques Espanol Fase 1

Este proyecto construye la base de un traductor para un lenguaje educativo.
En esta fase solo se cubren el analisis lexico y el analisis sintactico.

## Nombre del proyecto

Bloques Espanol Fase 1.

## Objetivo del proyecto

Disenar e implementar un analizador lexico y un analizador sintactico para un
lenguaje infantil de bloques. El sistema reconoce lexemas, genera tokens y
valida la estructura de los programas segun una gramatica formal. Esta fase
incluye una representacion basica del arbol sintactico y un manejo inicial de
errores.

## Flujo del programa

1. El usuario entrega un archivo `.tb` con el programa.
2. El analizador lexico lee el texto y genera una lista de tokens.
3. El analizador sintactico consume los tokens y valida la gramatica.
4. Si la entrada es valida, se construye el arbol sintactico.
5. Si hay errores, se reportan con linea y columna.

## Ejemplos

Ejemplo 1. Declarar una cajita y guardar un numero:

```text
crear_cajita edad como numero
guardar edad con 18
```

Ejemplo 2. Preguntar y mostrar el resultado:

```text
preguntar "Cual es tu nombre?" guardar_en nombre
mostrar nombre
```

Ejemplo 3. Repetir y usar una condicion:

```text
crear_cajita contador como numero
guardar contador con 1
repetir 3 veces
  mostrar contador
  guardar contador con contador + 1
fin
si_pasa contador mayor_que 3 entonces
  mostrar "Listo"
fin
```

## Carpetas del analizador lexico

- `traductor_base/` contiene el codigo lexico en archivos con sufijo `_l` y `_ls`.
- `tests/` guarda pruebas del analisis lexico.
- `examples/` incluye programas de entrada para validar el lexico.

## Carpetas del analizador sintactico

- `traductor_base/` contiene el codigo sintactico en archivos con sufijo `_s` y `_ls`.
- `tests/` guarda pruebas del analisis sintactico.
- `examples/` incluye programas de entrada para validar la gramatica.

## Archivos y funciones principales

- `lexemas_l.md` describe palabras reservadas y patrones del lenguaje.
- `gramatica_s.ebnf` fija la gramatica formal usada por el parser.
- `traductor_base/definitions_l.py` define tipos de token, lexemas, etiquetas y estructuras base.
- `traductor_base/lexer_l.py` convierte texto fuente en tokens y reporta errores lexicos.
- `traductor_base/scanner_l.py` etiqueta lexemas para apoyo teorico y registra errores simples.
- `traductor_base/parser_s.py` valida la secuencia de tokens y construye el arbol sintactico.
- `traductor_base/ast_nodes_s.py` modela los nodos del arbol sintactico.
- `traductor_base/errors_ls.py` centraliza errores lexico y sintactico.
- `traductor_base/__main__.py` habilita la ejecucion por consola con comandos `lex`, `scan` y `parse`.
- `traductor_base/__init__.py` expone funciones publicas para importacion.
