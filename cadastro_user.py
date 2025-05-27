import email

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

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("\n ===== Lista de Usuários =====")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. Nome: {usuario['nome']}, Email: {usuario['email']}, Idade: {usuario['idade']}")

def remover_usuario(nome):
    email = input("Digite o e-mail do usuário que deseja remover: ")

    for usuario in usuarios:
        if usuario['email'] == email:
            usuarios.remove(usuario)
            print(f" Usuário com e-mail {email} removido com sucesso!")
            return
    print("Usuário não encontrado.")


def alterar_usuario():
    email = input("Digite o e-mail do usuário que deseja alterar: ")

    for usuario in usuarios:
        if usuario['email'] == email:
            print(f"\n Dados atuais: Nome: {usuario['nome']}, E-mail: {usuario['email']}, Idade: {usuario['idade']}")

            novo_nome = input("Digite o novo nome(ou pressione Enter para manter o atual: ")
            novo_email = input("Digite o novo e-mail (ou pressione Enter para manter o atual: ")
            nova_idade = input("Digite a nova idade(ou pressione Enter para manter o atual: ")

            if novo_nome:
                usuario['nome'] = novo_nome
            if novo_email:
                usuario['email'] = novo_email
            if nova_idade:
                usuario['idade'] = nova_idade

            print("Usuário alterado com sucesso!")
            return
    print("Usuário não encontrado.")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar_usuarios()
    elif opcao == "3":
        remover_usuario()
    elif opcao == "4":
         alterar_usuario()
    elif opcao == "5":
        print("Saindo do sistema...Obrigado por utilizar o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")