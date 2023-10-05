"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""
import os


# Função para limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Função para imprimir a lista
def imprimir_lista(lista):
    print("Lista de compras:")
    for i in range(len(lista)):
        print(f"{i + 1} - {lista[i]}")
    print()


# Função para inserir um item na lista
def inserir_item(lista):
    item = input("Digite o item que deseja inserir: ")
    lista.append(item)
    print(f"Item {item} inserido com sucesso!")
    print()


# Função para remover um item da lista
def remover_item(lista):
    imprimir_lista(lista)
    item = int(input("Digite o número do item que deseja remover: "))
    if item > len(lista):
        print("Item não encontrado!")
    else:
        lista.pop(item - 1)
        print("Item removido com sucesso!")
    print()


# Função para limpar a lista
def limpar_lista(lista):
    lista.clear()
    print("Lista limpa com sucesso!")
    print()


# Função para imprimir o menu
def imprimir_menu():
    print("1 - Inserir item")
    print("2 - Remover item")
    print("3 - Limpar lista")
    print("4 - Sair")
    print()


# Função para executar o programa
def executar_programa():
    lista = []
    while True:
        imprimir_lista(lista)
        imprimir_menu()
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            inserir_item(lista)
        elif opcao == 2:
            remover_item(lista)
        elif opcao == 3:
            limpar_lista(lista)
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")
            print()
        clear()


# Executando o programa
executar_programa()
