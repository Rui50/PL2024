import ply.lex as lex
import json
import re
import sys
from datetime import datetime

saldo = 0
stock = []
state = 1

tokens=(
    "LISTAR",
    "MOEDA",
    "SELECIONAR",
    "SALDO",
    "SAIR"
)

def t_LISTAR(t):
    r"LISTAR"
    listarStock()
    return t

def t_MOEDA(t):
    r"MOEDA((\s(5|10|20|50)c)|\s(1|2)e)+"
    euros = re.findall(r"(\d+)e", t.value)
    cents = re.findall(r"(\d+)c", t.value)

    global saldo

    for eur in euros:
        saldo += int(eur)
    for cent in cents:
        saldo += int(cent) / 100
    return t

def t_SELECIONAR(t):
    r"SELECIONAR\sA\d+"
    global stock
    global saldo

    produto_match = re.findall(r"A\d+", t.value)
    if produto_match:
        produto = produto_match[0]

        for prod in stock:
            if prod["cod"] == produto:
                price = prod["preco"]
                if prod["quant"] > 0:
                    if saldo >= price:
                        saldo -= price
                        prod["quant"] -= 1 
                        print("Produto comprado")
                        return t
                    else:
                        print("Saldo insuficiente")
                        return t
                else:
                    print("Produto esgotado")
                    return t
        print("Produto não encontrado")
    return t

def t_SALDO(t):
    r"SALDO"
    print(f"Saldo: {saldo}")
    return t

def t_SAIR(t):
    r"SAIR"
    global saldo
    global state

    state = 0
    # fazer uma func para calc o troco em moedas
    print(f"Troco: ", saldo)

def t_error(t):
    print(f"Illegal character")
    t.lexer.skip(1)

t_ignore = " \t\n"

def listarStock():
    print("cod | nome | quantidade |  preço")
    print("--------------------------------")

    for item in stock:
        cod = item['cod']
        nome = item['nome']
        quant = item['quant']
        preco = item['preco']
        
        print(f"{cod}  {nome}  {preco}  {quant}")

  
def load_stock(filename):
    global stock
    with open(filename, "r") as file:
        stock = json.load(file)


#####################
        
def main():
    load_stock("stock.json")
    lexer = lex.lex()

    print(f"{datetime.now()}, Stock carregado, Estado atualizado")
    print(" Bom dia. Estou disponível para atender o seu pedido.")

    line = input()
    lexer.input(line)

    while state == 1:
        tok = lexer.token()
        if not tok:
            break


if __name__ == '__main__':
    main()