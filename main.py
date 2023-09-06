import tkinter as tk
import sqlite3
import pandas as pd

conexao = sqlite3.connect('banco_clientes.db')

# mensageiro/cursor
c = conexao.cursor()

# executar uma ação dentro do banco
c.execute('''CREATE TABLE clientes (
    nome text,
    sobrenome text,
    email text,
    telefone text
    )
''')

# abrir a porta
conexao.commit()

# fechando a conexão
conexao.close()