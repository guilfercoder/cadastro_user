usuarios = []

def menu():
    print("\n ===== Cadastro de Usuários =====")
    print("1 - Cadastrar Usuário")
    print("2 - Listar Usuários")
    print("3 - Alterar Usuários")
    print("4 - Remover Usuários")
    print("5 - Sair do Programa")


def cadastrar():
    nome = input("Nome: ")
    senha = input("Senha: ")
    email = input("Email: ")
    idade = input("Idade: ")

    usuario = {
        "nome": nome,
        "senha": senha,
        "email": email,
        "idade": idade

    }

    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")

