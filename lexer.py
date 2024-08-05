import ply.lex as lex

tokens = (
    'NUMBER',    # Número (inteiro ou decimal)
    'VARIABLE',  # Variável (identificador)
    'PLUS',      # Operador de adição '+'
    'MINUS',     # Operador de subtração '-'
    'TIMES',     # Operador de multiplicação '*'
    'DIVIDE',    # Operador de divisão '/'
    'POWER',     # Operador de exponenciação '^'
    'LPAREN',    # Parêntese esquerdo '('
    'RPAREN',    # Parêntese direito ')'
    'EQUALS'     # Operador de atribuição '='
)

# Expressões regulares para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='


# Define o token para os números
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) # Converte o valor para float
    return t


# Define o token para os identificadores
def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


t_ignore = ' \t\n'  # Ignora espaços, tabulações e quebras de linha


# Lida com caracteres inválidos no código de entrada
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()   # Cria o lexer a partir das definições
