from __future__ import annotations

"""
Este archivo concentra la base formal de la fase lexico.
Contiene los lexemas infantiles del lenguaje, sus etiquetas academicas,
los tipos de token y las estructuras que usa el lexer.
"""

from dataclasses import dataclass
from enum import Enum, auto


class TipoToken(Enum):
    CREAR_CAJITA = auto()
    GUARDAR = auto()
    COMO = auto()
    CON = auto()
    MOSTRAR = auto()
    PREGUNTAR = auto()
    GUARDAR_EN = auto()
    SI_PASA = auto()
    SI_NO_PASA = auto()
    ENTONCES = auto()
    REPETIR = auto()
    VECES = auto()
    FIN = auto()
    TIPO_NUMERO = auto()
    TIPO_DECIMAL = auto()
    TIPO_TEXTO = auto()
    TIPO_SI_NO = auto()
    VERDADERO = auto()
    FALSO = auto()
    MAYOR_QUE = auto()
    MENOR_QUE = auto()
    IGUAL_A = auto()
    DIFERENTE_DE = auto()
    MAYOR_O_IGUAL = auto()
    MENOR_O_IGUAL = auto()
    Y = auto()
    O = auto()
    NO = auto()
    ID = auto()
    NUMERO = auto()
    CADENA = auto()
    SUMA = auto()
    RESTA = auto()
    MULT = auto()
    DIV = auto()
    SALTO_LINEA = auto()
    FIN_ARCHIVO = auto()


@dataclass(frozen=True)
class Token:
    tipo: TipoToken
    lexema: str
    linea: int
    columna: int


PALABRAS_RESERVADAS = {
    "crear_cajita": TipoToken.CREAR_CAJITA,
    "guardar": TipoToken.GUARDAR,
    "como": TipoToken.COMO,
    "con": TipoToken.CON,
    "mostrar": TipoToken.MOSTRAR,
    "preguntar": TipoToken.PREGUNTAR,
    "guardar_en": TipoToken.GUARDAR_EN,
    "si_pasa": TipoToken.SI_PASA,
    "si_no_pasa": TipoToken.SI_NO_PASA,
    "entonces": TipoToken.ENTONCES,
    "repetir": TipoToken.REPETIR,
    "veces": TipoToken.VECES,
    "fin": TipoToken.FIN,
    "numero": TipoToken.TIPO_NUMERO,
    "decimal": TipoToken.TIPO_DECIMAL,
    "texto": TipoToken.TIPO_TEXTO,
    "si_no": TipoToken.TIPO_SI_NO,
    "verdadero": TipoToken.VERDADERO,
    "falso": TipoToken.FALSO,
    "mayor_que": TipoToken.MAYOR_QUE,
    "menor_que": TipoToken.MENOR_QUE,
    "igual_a": TipoToken.IGUAL_A,
    "diferente_de": TipoToken.DIFERENTE_DE,
    "mayor_o_igual": TipoToken.MAYOR_O_IGUAL,
    "menor_o_igual": TipoToken.MENOR_O_IGUAL,
    "y": TipoToken.Y,
    "o": TipoToken.O,
    "no": TipoToken.NO,
}


simbolos_simples = {
    "+": TipoToken.SUMA,
    "-": TipoToken.RESTA,
    "*": TipoToken.MULT,
    "/": TipoToken.DIV,
}
