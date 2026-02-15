from const.tokens import tokens
import ply.lex as lex

# Regex

t_IPTABLES    = r'iptables'
t_APPEND      = r'-A'
t_CHAIN       = r'INPUT|OUTPUT|FORWARD'
t_SOURCE      = r'-s'
t_PROTOCOL_OP = r'-p'
t_PROTOCOL    = r'tcp|udp'
t_PORT_OPTION = r'--dport'
t_JUMP        = r'-j'
t_ACTION      = r'ACCEPT|DROP'
t_IP          = r'\d+\.\d+\.\d+\.\d+'
t_PORT        = r'\d+'

# Ignorar espacios
t_ignore = ' \t\n'

def t_error(t):
    print("error:", t.value[0])
    t.lexer.skip(1)


# construct Lexer
lexer = lex.lex()

# read file

with open("example.txt", "r") as archivo:
    data = archivo.read()

# Analize tokens

lexer.input(data)

print("Tokens founds:\n")

while True:
    token = lexer.token()
    if not token:
        break
    print(f"Token: {token.type}   Lexema: {token.value}")
