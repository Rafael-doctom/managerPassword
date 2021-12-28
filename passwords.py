import sqlite3

MASTER_PASSWORD = "12345"
MASTER_USER = "Rafael"

user = sqlite3.connect("users.db")
passsword = sqlite3.connect("users.db")

cursor = user.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
    );''')

user.close()
passsword.close()

print('Olá, Mundo!')

usuario = input("Usuário:")
senha = input("Senha:")

if senha != MASTER_PASSWORD or usuario != MASTER_USER:
    print('Senha e usuário incorreto')
    exit()
if senha == MASTER_PASSWORD:
    print(f'Senha correta: {MASTER_PASSWORD}')

def Menu():
    print("Opções abaixo:")

while True:
    Menu()
    Passo1 = input("Deseja avançar? (S/N)")

    if Passo1 == 'S':
        print("Muito bom! Vamos de novo...")
    else:
        exit()
