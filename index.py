import json
import random
import time

time.sleep(0.7)

try:
    with open("tarefas.json", "r", encoding="utf-8") as dados:
        tarefas = json.load(dados)

except FileNotFoundError:
    tarefas = []

print("\033[33mGereciador de tarefas\033[0m")
print()
print("[1] Criar tarefas ")
print()
print("[2] Vizualizar tarefas ")
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

        if 13 <= horario1 <= 23.59:

            horario = f"{horario1}/PM"
            break

        elif 12 <= horario1 <= 12.59:

            comfirmaçao = input("Seu horaio é PM ou AM: ").lower().strip()

            if comfirmaçao == "PM":

                horario = f"{horario1}/{comfirmaçao}"
                break

            else:
                horario = f"{horario1}/{comfirmaçao}"
                break

        elif 1 <= horario1 <= 11.59:

            comfirmaçao = input("Seu horaio é PM ou AM: ").lower().strip()

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

        print(f"Nome: {tarefa['nome']}")
        print(f"Duração: {tarefa['duraçao']}")
        print(f"Horário: {tarefa['horario']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Status: {tarefa['status']}")

