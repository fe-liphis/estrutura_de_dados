from collections import deque 

pilha = deque()

print("Bem vindo ao sistema!")

while True:
    print("Escolha uma opção abaixo:")
    print("1 - Empilhar item")
    print("2 - Ver pilha")
    print("3 - Retirar da pilha")
    print("4 - Sair")
    
    opcao = int(input())

    print("\n")

    if opcao == 1:
        print("Digite o texto a ser empilhado:")
        item = str(input())
        pilha.append(item)
    elif opcao == 2:
        if pilha:
            for item in reversed(pilha):
                print(f"{item}")
        else:
            print("Pilha vazia")
    elif opcao == 3:
        if pilha:
            textoRetirado = pilha.pop()
            print(f"Texto desempilhado: {textoRetirado}")
        else:
            print("Pilha vazia")
    elif opcao == 4:
        print("Obrigado por utilizar o sistema!!!")
        break
    else:
        print("Opção inválida")

    print("\n")