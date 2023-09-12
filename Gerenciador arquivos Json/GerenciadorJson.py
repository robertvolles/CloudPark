import json

def read_configuration():
    try:
        with open("config.json", "r") as file:
            data = json.load(file)
            if not data:
                print("O arquivo não contém informações.")
            else:
                print("Conteúdo do arquivo config.json:")
                print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print("O arquivo config.json não existe.")

def write_configuration():
    server_name = input("Informe o nome do servidor: ")
    server_ip = input("Informe o IP do servidor: ")
    server_password = input("Informe a senha do servidor: ")

    data = {
        "server_name": server_name,
        "server_ip": server_ip,
        "server_password": server_password
    }

    with open("config.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print("Informações salvas com sucesso no arquivo config.json.")
    print("Conteúdo do arquivo config.json:")
    print(json.dumps(data, indent=4))

def main():
    while True:
        print("\nEscolha uma opção:")
        print("1 - Read configuration")
        print("2 - Write configuration")
        print("3 - Sair")
        
        choice = input("Digite o número da opção desejada: ")
        
        if choice == "1":
            read_configuration()
        elif choice == "2":
            write_configuration()
        elif choice == "3":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()






