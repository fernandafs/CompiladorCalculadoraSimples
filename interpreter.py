from parser import parser

"""
    Interpreta o código de entrada usando o parser e retorna o resultado.

    :param input_code: Código de entrada como string.
    :return: Resultado da interpretação do código.
"""


def interpret(input_code):
    result = parser.parse(input_code)  # Analisa o código de entrada usando o parser
    return result  # Retorna o resultado da análise
