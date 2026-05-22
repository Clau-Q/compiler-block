"""
Este archivo contiene pruebas basicas de la fase 1.
Sirve para comprobar que el lexer reconoce el nuevo vocabulario infantil
y que el parser construye un programa valido.
"""

import unittest

from traductor_base.lexer_l import analizar_lexicamente
from traductor_base.parser_s import analizar_sintaxis


class Fase1Tests(unittest.TestCase):
    def test_lexer_reconoce_crear_cajita(self):
        tokens = analizar_lexicamente("crear_cajita edad como numero\n")
        self.assertEqual(tokens[0].tipo.name, "CREAR_CAJITA")
        self.assertEqual(tokens[1].lexema, "edad")

    def test_parser_construye_programa_infantil(self):
        program = analizar_sintaxis(
            "crear_cajita edad como numero\n"
            "guardar edad con 8\n"
            "mostrar edad\n"
        )
        self.assertEqual(program.__class__.__name__, "Programa")
        self.assertEqual(len(program.sentencias), 3)
