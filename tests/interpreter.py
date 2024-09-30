import re

# Definimos los patrones para los tokens del lenguaje
token_specs = [
    ('NUMBER',   r'\d+'),        # Números
    ('ID',       r'[A-Za-z]+'),  # Identificadores
    ('ASSIGN',   r'='),          # Asignación
    ('OP',       r'[+\-*/]'),    # Operadores
    ('SKIP',     r'[ \t]+'),     # Espacios en blanco
    ('NEWLINE',  r'\n'),         # Nueva línea
]

def load_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return code

def tokenize(code):
    tokens = []
    for spec in token_specs:
        token_name, token_regex = spec
        regex = re.compile(token_regex)
        for match in regex.finditer(code):
            tokens.append((token_name, match.group(0)))
    return tokens

class Node:
    def __init__(self, token, left=None, right=None):
        self.token = token
        self.left = left
        self.right = right

def parse_expression(tokens):
    # Suponemos una expresión del tipo 'ID = NUM OP NUM'
    left_token = tokens.pop(0)
    assign_token = tokens.pop(0)
    right_token = tokens.pop(0)
    
    return Node(assign_token, left=left_token, right=right_token)

if __name__ == "__main__":
    file_path = "test.pgen"
    code = load_file(file_path)
    tokens = tokenize(code)
    root = parse_expression(tokens)
    print(root.token, root.left, root.right)
