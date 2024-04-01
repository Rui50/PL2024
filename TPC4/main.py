import ply.lex as lex

tokens = (
    'SELECT',
    'VAR',
    'VIRG',
    'FROM',
    'WHERE',
    'NUM',
    'EQ',
    'GREATER',
    'GREATER_EQ',
    'LESS',
    'LESS_EQ'
)

t_SELECT = r'SELECT'
t_VAR = r'[A-Za-z_]+[A-Za-z0-9-_\.]'
t_VIRG = r'\,'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_EQ = r'\='
t_GREATER = r'\>'
t_GREATER_EQ = r'\>\='
t_LESS = r'\<'
t_LESS_EQ = r'\<\='


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_IGNORE = ' \t'


def t_error(t):
    print(f"Caracter Ilegal: '{t.value[0]}'")
    t.lexer.skip()


def main():
    lexer = lex.lex()
    data = input()
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


if __name__ == '__main__':
    main()