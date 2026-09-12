import json
import random
import time

time.sleep(0.7)

try:
    with open("tarefas.json", "r", encoding="utf-8") as dados:
        tarefas = json.load(dados)

except FileNotFoundError:
    tarefas = []

try:
    with open('historico.json', 'r', encoding='utf-8') as fontes:
        historico = json.load(fontes)

except FileNotFoundError:
    historico = []

print("\033[33mGereciador de tarefas\033[0m")
print()
print("[1] Criar tarefas ")
print()
print("[2] Vizualizar tarefas ")
print()
print("[3] Editar tarefas ")
print()
print("[4] Excluir tarefas")
print()

escolha = int(input("digite o número da sua escolha: "))

if escolha == 1:

    print()
    print("\033[33mCriação de tarefas\033[0m")
    print()

    nome = input("Digite o nome da terefa: ").lower().strip()
    print()

    duraçao = float(
        input("Digite a duração da tarefa, somente números: ").replace(",", ".")
    )
    print()

    while True:

        print("Que horas sera seu compromisso ? ")
        print()

        horario1 = float(input("Digite o horario da tarefa: ").replace(",", "."))
        print()

        if 13 <= horario1 <= 23.59:

            horario = f"{horario1}/PM"
            break

        elif 12 <= horario1 <= 12.59:

            comfirmaçao = input("Seu horaio é PM ou AM: ").lower().strip()
            print()

            if comfirmaçao == "PM":

                horario = f"{horario1}/{comfirmaçao}"
                break

            else:
                horario = f"{horario1}/{comfirmaçao}"
                break

        elif 1 <= horario1 <= 11.59:

            comfirmaçao = input("Seu horaio é PM ou AM: ").lower().strip()
            print()

            if comfirmaçao == "PM":

                horario = f"{horario1}/{comfirmaçao}"
                break

            else:
                horario = f"{horario1}/{comfirmaçao}"
                break

    print(
        "Niveis de prioridade: \033[1;31;40mMuita alta\033[0m, \033[31mAlta, \033[32mMedia, \033[33mBaixa, \033[34madiavel\033[0m. "
    )
    print()

    while True:

        nivel_prioridade = input("Digite qual a prioridade: ").lower().strip()
        print()

        if nivel_prioridade in ["muito alta", "alta", "media", "baixa", "adiavel"]:
            prioridade = nivel_prioridade
            break

    while True:

        id = random.randint(1000, 9999)

        id_encontrado = False

        for ids in tarefas:
            if ids["id"] == id:
                id_encontrado = True
                break

        if id_encontrado == False:
            break

    while True:

        print("Você já iniciou a tarefa ou veio apenas marcar: ")
        print("""[1] Já iniciei
    [2] vim apenas marcar
        """)

        status_atual = int(input("Digite sua escolha: "))

        if status_atual == 1:
            status = "\033[33mEm processo\033[0m"
            break

        elif status_atual == 2:
            status = "\033[31mPendente\033[0m"
            break

        else:
            print("\033[31mResposta inválida ! \033[0m")
            print()

    print("\033[32mTarefa criada !\033[0m")
    print()

    tarefas.append(
        {
            "id": id,
            "nome": nome,
            "duraçao": duraçao,
            "horario": horario,
            "prioridade": prioridade,
            "status": status,
        }
    )

    with open("tarefas.json", "w", encoding="utf-8") as dados:
        json.dump(tarefas, dados, ensure_ascii=False, indent=6)

elif escolha == 2:

    print("\033[33mVisão das tarefas\033[0m")
    print()

    for tarefa in tarefas:

        print("===================================")
        print(f"Nome: {tarefa['nome']}")
        print(f"Duração: {tarefa['duraçao']}")
        print(f"Horário: {tarefa['horario']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Status: {tarefa['status']}")
        print(f"ID: {tarefa['id']}")
        print("===================================")
        print()

elif escolha == 3:

    print("\033[33mEdição de tarefas\033[0m")
    print()

    for tarefa in tarefas:

        print(f"Nome: {tarefa['nome']}")
        print(f"ID: {tarefa['id']}")
        print()

    while True:

        ed_tarefa = int(
            input("Digite o \033[31mid\033[0m da tarefa que deseja alterar: ")
        )
        print()

        tarefa_ed = None

        for tarefa in tarefas:
            if tarefa["id"] == ed_tarefa:
                tarefa_ed = tarefa
                break

        if tarefa_ed is not None:
            break

    print("===================================")
    print(f"Nome: {tarefa_ed['nome']}")
    print(f"Duração: {tarefa_ed['duraçao']}")
    print(f"Horário: {tarefa_ed['horario']}")
    print(f"Prioridade: {tarefa_ed['prioridade']}")
    print("===================================")
    print()

    print("O que deseja alterar ? ")
    print()

    while True:

        opçao = input("Digite sua escolha: ").lower().strip()
        print()

        if opçao == "nome":

            novo_nome = input("Digite o novo nome da tarefa: ").lower().strip()
            print()

            tarefa_ed["nome"] = novo_nome
            break

        elif opçao in ["duraçao", "duração"]:

            nova_duraçao = float(
                input("Digite a nova duração da tarefa: ").replace(",", ".")
            )
            print()

            tarefa_ed["duraçao"] = nova_duraçao
            break

        elif opçao in ["horario", "horário"]:

            novo_horario = float(input("Digite o novo horário: ").replace(",", "."))
            print()

            tarefa_ed["horario"] = novo_horario
            break

        elif opçao == "prioridade":

            print(
                "Niveis de prioridade: \033[1;31;40mMuita alta\033[0m, \033[31mAlta, \033[32mMedia, \033[33mBaixa, \033[34madiavel\033[0m. "
            )
            print()

            nova_prioridade = input("Digite a nova prioridade: ").lower().strip()
            print()

            tarefa_ed["prioridade"] = nova_prioridade
            break

        else:
            print("\033[31mResultado invalido !\033[0m")
            print()

    with open("tarefas.json", "w", encoding="utf-8") as dados:
        json.dump(tarefas, dados, ensure_ascii=False, indent=6)

    print("\033[32mAlteração concluida !\033[0m")
    print()

elif escolha == 4:

    print("\033[33mExcluir tarefas\033[0m")
    print()

    for tarefa in tarefas:

        print(f"Nome: {tarefa['nome']}")
        print(f"ID: {tarefa['id']}")
        print()

    while True:

        ex_tarefa = int(
            input("Digite o \033[31mid\033[0m da tarefa que deseja excluir: ")
        )
        print()

        tarefa_ex = None

        for tarefa in tarefas:
            if tarefa["id"] == ex_tarefa:
                tarefa_ex = tarefa
                break

        if tarefa_ex is not None:
            break
        else:
            print("\033[31mID não encontrado\033[0m, tente novamente !")
            print()

    tarefas.remove(tarefa_ex)

    with open("tarefas.json", "w", encoding="utf-8") as dados:
        json.dump(tarefas, dados, ensure_ascii=False, indent=6)

    print("\033[32mTarefa excluida !\033[0m")
    print()

elif escolha == 5:

    print("\033[33mIniciar/Comcluir tarefa\033[0m")
    print()

    for tarefa in tarefas:

        print(f"Nome: {tarefa['nome']}")
        print(f"ID: {tarefa['id']}")
        print()

    while True:

        tarefa_es = int(input("Digite o id da tarefa escolhida: "))
        print()

        tarefa_encontrada = None

        for tarefa in tarefas:
            if tarefa['id'] == tarefa_es:
                tarefa_encontrada = tarefa
                break

        if tarefa_encontrada is not None:
            break
        else:
            print("\033[31mTarefa não encontrada !\033[0m")
            print()

    print("===================================")
    print(f"Nome: {tarefa_encontrada['nome']}")
    print(f"Duração: {tarefa_encontrada['duraçao']}")
    print(f"Horário: {tarefa_encontrada['horario']}")
    print(f"Prioridade: {tarefa_encontrada['prioridade']}")
    print("===================================")
    print()

    print("O que voce vai fazer, Iniciar tarefa ou concluir tarefa ?")
    print()

    while True:

        es_tarefa = input('Digite sua escolha: ').lower().strip()
        print()

        if es_tarefa in ['iniciar tarefa', 'iniciar']:

            tarefa_encontrada['status'] = 'Em processo'

            escolha2 = 'Iniciada'

            with open('tarefas.json', 'w', encoding='utf-8') as dados:
                    json.dump(tarefas, dados, ensure_ascii= False, indent= 6)

            break

        elif es_tarefa in ['concluir tarefa', 'concluir']:

            tarefa_encontrada['status'] = 'Concluida'

            historico.append(tarefa_encontrada)

            tarefas.remove(tarefa_encontrada)

            escolha2 = 'Concluida'

            with open('historico.json', 'w', encoding='utf-8') as fontes:
                json.dump(historico, fontes, ensure_ascii=False, indent=6)

            with open('tarefas.json', 'w', encoding='utf-8') as dados:
                json.dump(tarefas, dados, ensure_ascii=False, indent=6)

            break

        else:
            print("\033[31mEscolha inválida\033[0m")
            print()    

    print(f'\033[32mTarefa {escolha2}\033[0m')
    print()