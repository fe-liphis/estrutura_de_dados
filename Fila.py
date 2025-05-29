from collections import deque 

fila = deque()
senha = 1

print("Bem vindo ao sistema!")

while True:
    print("Escolha uma opção abaixo:")
    print("1 - Retirar senha")
    print("2 - Ver fila")
    print("3 - Chamar senha")
    print("4 - Sair")
    
    opcao = int(input())

    print("\n")

    if opcao == 1:
        fila.append(f"A{senha}")
        print(f"Senha retirada: A{senha}")
        senha += 1
    elif opcao == 2:
        if fila:
            print(list(fila))
        else:
            print("Fila vazia")
    elif opcao == 3:
        if fila:
            senhaChamada = fila.popleft()
            print(f"Senha chamada: {senhaChamada}")
        else:
            print("Fila vazia")
    elif opcao == 4:
        print("Obrigado por utilizar o sistema!!!")
        break
    else:
        print("Opção inválida")

    print("\n")