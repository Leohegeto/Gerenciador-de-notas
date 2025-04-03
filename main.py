import json
import os

NOTAS_FILE = "notas.json"

def carregar_notas():
    if not os.path.exists(NOTAS_FILE):
        return []
    with open(NOTAS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def salvar_notas(notas):
    with open(NOTAS_FILE, "w", encoding="utf-8") as file:
        json.dump(notas, file, indent=4)

def listar_notas():
    notas = carregar_notas()
    if not notas:
        print("Nenhuma nota encontrada.")
    for i, nota in enumerate(notas, 1):
        print(f"{i}. {nota['titulo']} - {nota['conteudo']}")

def adicionar_nota():
    titulo = input("Título da nota: ")
    conteudo = input("Conteúdo da nota: ")
    notas = carregar_notas()
    notas.append({"titulo": titulo, "conteudo": conteudo})
    salvar_notas(notas)
    print("Nota adicionada com sucesso!")

def editar_nota():
    notas = carregar_notas()
    listar_notas()
    indice = int(input("Digite o número da nota que deseja editar: ")) - 1
    if 0 <= indice < len(notas):
        notas[indice]["titulo"] = input("Novo título: ")
        notas[indice]["conteudo"] = input("Novo conteúdo: ")
        salvar_notas(notas)
        print("Nota editada com sucesso!")
    else:
        print("Índice inválido.")

def excluir_nota():
    notas = carregar_notas()
    listar_notas()
    indice = int(input("Digite o número da nota que deseja excluir: ")) - 1
    if 0 <= indice < len(notas):
        notas.pop(indice)
        salvar_notas(notas)
        print("Nota excluída com sucesso!")
    else:
        print("Índice inválido.")

def menu():
    while True:
        print("\nGerenciador de Notas")
        print("1. Listar notas")
        print("2. Adicionar nota")
        print("3. Editar nota")
        print("4. Excluir nota")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            listar_notas()
        elif opcao == "2":
            adicionar_nota()
        elif opcao == "3":
            editar_nota()
        elif opcao == "4":
            excluir_nota()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
