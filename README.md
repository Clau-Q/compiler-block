# Bloques Espanol Fase 1

Fase 1 del proyecto enfocada solo en:

- analisis lexico
- analisis sintactico
- gramatica
- lexemas, tokens e identificadores

Esta version ya usa el vocabulario infantil acordado para el proyecto:

- `crear_cajita`
- `guardar`
- `mostrar`
- `preguntar`
- `si_pasa`
- `si_no_pasa`
- `repetir`
- `fin`

## Requisitos

- Linux con `python3` (recomendado 3.10+)
- No hay dependencias externas

## Uso rapido (Linux)

1. Ubicate en la carpeta del proyecto:

```bash
cd /ruta/al/proyecto
```

1. Ver tokens del analizador lexico:

```bash
python3 -m traductor_base lex ./examples/programa.tb
```

1. Ver lexemas y etiquetas del scanner:

```bash
python3 -m traductor_base scan ./examples/programa.tb
```

1. Ver estructura sintactica:

```bash
python3 -m traductor_base parse ./examples/programa.tb
```

Compatibilidad Windows: los mismos comandos funcionan con `python` y rutas estilo `.` y `\` (por ejemplo `python -m traductor_base lex .\examples\programa.tb`).

## Archivos clave

- `lexemas_l.md`: tabla de palabras reservadas y patrones del lenguaje infantil
- `gramatica_s.ebnf`: gramatica formal del lenguaje infantil
- `traductor_base/definitions_l.py`: definiciones de lexemas, etiquetas, tipos de token e identificadores
- `traductor_base/lexer_l.py`: analizador lexico
- `traductor_base/scanner_l.py`: escaner academico por etiquetas
- `traductor_base/parser_s.py`: analizador sintactico
- `traductor_base/ast_nodes_s.py`: estructura del arbol sintactico
- `traductor_base/errors_ls.py`: errores compartidos
- `examples/programa.tb`: programa de ejemplo

## Sufijos usados

- `_l`: archivo orientado a la fase lexico
- `_s`: archivo orientado a la fase sintactica
- `_ls`: archivo compartido entre ambas fases

## Nombres internos

En esta fase el codigo usa nombres alineados al lenguaje infantil, por ejemplo:

- `CrearCajita`
- `Guardar`
- `Mostrar`
- `Preguntar`
- `Repetir`
- `SiPasa`
- `AnalizadorSintactico`
- `Escaner`
- `CodigoFuente`
- `ErrorLexico`
- `ErrorSintactico`

## Donde esta el identificador

El identificador del lenguaje esta definido principalmente en:

- `lexemas_l.md`
- `traductor_base/lexer_l.py`
- `traductor_base/definitions_l.py`

Patron base:

```text
[A-Za-z_][A-Za-z0-9_]*
```
