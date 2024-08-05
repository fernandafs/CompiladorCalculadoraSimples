from lexer import tokens
import ply.yacc as yacc

# Define a precedência dos operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),     # Adição e subtração têm a mesma precedência, associada à esquerda
    ('left', 'TIMES', 'DIVIDE'),   # Multiplicação e divisão têm a mesma precedência, associada à esquerda
    ('right', 'POWER'),            # Exponenciação tem a maior precedência, associada à direita
)

# Dicionário para armazenar variáveis e seus valores
names = {}


#  Regra para uma expressão sozinha (sem atribuição), retornando o valor da expressão.
def p_statement_expr(t):
    'statement : expression'
    t[0] = t[1]


# Regra para atribuição de uma variável. Atribui o valor da expressão à variável.
def p_statement_assign(t):
    'statement : VARIABLE EQUALS expression'
    names[t[1]] = t[3]
    t[0] = None


# Regra para operações binárias (soma, subtração, multiplicação, divisão e exponenciação).
def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression'''
    if t[2] == '+':         # Soma
        t[0] = t[1] + t[3]
    elif t[2] == '-':       # Subtração
        t[0] = t[1] - t[3]
    elif t[2] == '*':       # Multiplicação
        t[0] = t[1] * t[3]
    elif t[2] == '/':       # Divisão
        t[0] = t[1] / t[3]
    elif t[2] == '^':       # Exponenciação
        t[0] = t[1] ** t[3]


# Regra para expressões entre parênteses, que são avaliadas primeiro.
def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


# Regra para números. Retorna o valor do número.
def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]     # O valor da expressão é o número


# Regra para variáveis. Retorna o valor da variável se definida, ou uma mensagem de erro se não estiver definida.
def p_expression_variable(t):
    'expression : VARIABLE'
    t[0] = names.get(t[1], f"Undefined variable '{t[1]}'")  # Retorna o valor da variável ou uma mensagem de erro


# Lida com erros de sintaxe no código de entrada.
def p_error(t):
    print(f"Syntax error at '{t.value}'")   # Imprime uma mensagem de erro com o valor do token


# Cria o parser a partir das definições
parser = yacc.yacc()
