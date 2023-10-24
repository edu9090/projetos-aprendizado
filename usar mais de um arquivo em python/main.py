# arquivo que chama as funções
import sla
while True:
    print("1 para criar")
    print("2 para editar")
    print("3 para excluir")
    print("4 para sair")
    try:
        fds = int(input("opção : "))
        match fds:
            case 1:
                nome = input("nome :")
                idade = input("idade : ")
                cpf = input("cpf : ")
                sla.criar(nome,idade,cpf)
            
            case 2:
                nome = input("nome :")
                idade = input("idade : ")
                cpf = input("cpf : ")
                sla.editar(nome,idade,cpf)
            
            case 3:
                cpf = input("cpf : ")
                sla.excl(cpf)

            case 4 :
                break
            
            case _:
                print("invalido")
    except ValueError:
        print("opção invalida")
            
        