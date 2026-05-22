from __future__ import annotations

"""
Este archivo permite ejecutar el proyecto desde la consola.
Sirve para probar rapidamente las dos salidas principales:
analisis lexico y analisis sintactico.
"""

import sys

from .errors_ls import ErrorTraductor
from .lexer_l import analizar_archivo_lexico
from .parser_s import analizar_archivo_sintactico


def main(argv: list[str] | None = None) -> int:
    """Recibe un comando de consola y ejecuta la fase correspondiente."""
    args = list(sys.argv[1:] if argv is None else argv)

    if len(args) < 2 or args[0] not in {"lex", "parse"}:
        print("Uso: python -m traductor_base <lex|parse> <archivo.tb>")
        return 1

    comando, ruta = args[0], args[1]

    try:
        if comando == "lex":
            for token in analizar_archivo_lexico(ruta):
                print(
                    f"{token.tipo.name:<15} {token.lexema!r:<20} "
                    f"linea={token.linea} columna={token.columna}"
                )
            return 0

        if comando == "parse":
            print(analizar_archivo_sintactico(ruta))
            return 0
    except ErrorTraductor as error:
        print(error)
        return 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
