# Diseño de un compilador para un lenguaje visual infantil como puente entre bloques y lenguajes textuales

Este proyecto construye la base de un traductor para un lenguaje educativo.
En esta fase solo se cubren el analisis lexico y el analisis sintactico.

## Objetivo del proyecto

Desarrollar un compilador para un lenguaje de programacion visual basado en
bloques, orientado a ninos. La propuesta es estrictamente secuencial y evita
eventos concurrentes para reducir la carga cognitiva. El compilador traduce los
programas de bloques a codigo Python y facilita la transicion hacia lenguajes
textuales. En esta fase se implementan el analisis lexico y el analisis
sintactico, con una representacion basica del arbol y un manejo inicial de
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

## Comandos de ejecucion

- Lexico: `python3 -m traductor_base lex examples/programa.tb`
- Sintactico: `python3 -m traductor_base parse examples/programa.tb`

## Archivos y funciones principales

### Analizador lexico

- `lexemas_l.md` describe palabras reservadas y patrones del lenguaje.
- `traductor_base/definitions_l.py` define tipos de token, lexemas, etiquetas y estructuras base.
- `traductor_base/lexer_l.py` convierte texto fuente en tokens y reporta errores lexicos.

### Analizador sintactico

- `gramatica_s.ebnf` fija la gramatica formal usada por el parser.
- `traductor_base/parser_s.py` valida la secuencia de tokens y construye el arbol sintactico.
- `traductor_base/ast_nodes_s.py` modela los nodos del arbol sintactico.

### Archivos compartidos y ejecucion

- `traductor_base/errors_ls.py` centraliza errores lexico y sintactico.
- `traductor_base/__main__.py` habilita la ejecucion por consola con comandos `lex` y `parse`.
- `traductor_base/__init__.py` expone funciones publicas para importacion.
