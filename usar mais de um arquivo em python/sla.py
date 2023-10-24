def escrever(txt):
    f=open("SQL.txt" , "a+")
    f.write(txt + "\n")
    f.close()
def criar(nome,idade,cpf):
    escrever(f"INSERT INTO Pessoa (Nome, Idade, CPF) values ({nome}, {idade}, {cpf})")
def editar(nome,idade,cpf):
    escrever(f"UPDATE PEssoa Set idade={idade} nome={nome} cpf={cpf}")
def excl(cpf):
    escrever(f"DELETE FROM Pessoa WHERE cpf={cpf}")
    print("funcionou")