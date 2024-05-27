from datetime import datetime

# Função para adicionar uma nova tarefa
def adicionar_tarefa(lista_tarefas):
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    data_vencimento = input("Digite a data de vencimento (formato: DD/MM/AAAA): ")
    prioridade = input("Digite a prioridade da tarefa (alta, média, baixa): ")
    categoria = input("Digite a categoria da tarefa: ")

    # Convertendo a data de vencimento para um objeto datetime
    try:
        data_vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y")
    except ValueError:
        print("Formato de data inválido. Use o formato DD/MM/AAAA.")
        return

    # Adicionando a nova tarefa à lista de tarefas
    nova_tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "data_vencimento": data_vencimento,
        "prioridade": prioridade,
        "categoria": categoria
    }
    lista_tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para visualizar todas as tarefas
def visualizar_tarefas(lista_tarefas):
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(lista_tarefas, 1):
        print(f"\nTarefa {i}:")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Data de Vencimento: {tarefa['data_vencimento'].strftime('%d/%m/%Y')}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Categoria: {tarefa['categoria']}")
    print()

# Função para editar uma tarefa existente
def editar_tarefa(lista_tarefas):
    visualizar_tarefas(lista_tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja editar: ")) - 1
        if 0 <= indice < len(lista_tarefas):
            tarefa = lista_tarefas[indice]
            print("Deixe em branco para manter o valor atual.")
            tarefa["titulo"] = input(f"Novo título ({tarefa['titulo']}): ") or tarefa["titulo"]
            tarefa["descricao"] = input(f"Nova descrição ({tarefa['descricao']}): ") or tarefa["descricao"]
            nova_data = input("Nova data de vencimento (formato: DD/MM/AAAA): ")
            if nova_data:
                try:
                    tarefa["data_vencimento"] = datetime.strptime(nova_data, "%d/%m/%Y")
                except ValueError:
                    print("Formato de data inválido. Use o formato DD/MM/AAAA.")
            tarefa["prioridade"] = input(f"Nova prioridade ({tarefa['prioridade']}): ") or tarefa["prioridade"]
            tarefa["categoria"] = input(f"Nova categoria ({tarefa['categoria']}): ") or tarefa["categoria"]
            print("Tarefa editada com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Número de tarefa inválido.")

# Função para excluir uma tarefa existente
def excluir_tarefa(lista_tarefas):
    visualizar_tarefas(lista_tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja excluir: ")) - 1
        if 0 <= indice < len(lista_tarefas):
            confirmacao = input("Tem certeza que deseja excluir esta tarefa? (s/n): ")
            if confirmacao.lower() == "s":
                del lista_tarefas[indice]
                print("Tarefa excluída com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Número de tarefa inválido.")

# Função principal
def main():
    lista_tarefas = []

    while True:
        print("\n=== Aplicativo de Lista de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Editar Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")

        opcao = input("\nDigite o número da opção desejada: ")

        if opcao == "1":
            adicionar_tarefa(lista_tarefas)
        elif opcao == "2":
            visualizar_tarefas(lista_tarefas)
        elif opcao == "3":
            editar_tarefa(lista_tarefas)
        elif opcao == "4":
            excluir_tarefa(lista_tarefas)
        elif opcao == "5":
            print("Obrigado por usar o Aplicativo de Lista de Tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Executar o programa
if __name__ == "__main__":
    main()