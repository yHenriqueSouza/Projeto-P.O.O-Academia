from main import Aluno, Personal, Gerente, Exercicio, Treino, Filial, RedeAcademia
import arquivo_csv as a

class Menu:
    def __init__(self):
        dados = a.carregar_dados_academia()
        
        if dados is not None:
            self.rede = dados[0]
            self.filial = dados[1]
            self.gerente = dados[2]
            self.personal = dados[3]
            self.lista_alunos = dados[4]
            self.lista_exercicios = dados[5]
            self.lista_treinos = dados[6]
            
            self.aluno = self.lista_alunos[0]
            self.exercicio = self.lista_exercicios[0]
            self.treino = self.lista_treinos[0]
            print(" Dados carregados a partir do banco local (CSV)!")
        else:
            print("Carregando banco padrão inicial...")
            self.gerar_dados_padrao()

    def gerar_dados_padrao(self):
        supino = Exercicio("Supino Reto", "Peitoral", 4, 10, 40, 90)
        agachamento = Exercicio("Agachamento", "Pernas", 4, 12, 60, 120)
        remada = Exercicio("Remada Curvada", "Costas", 4, 10, 45, 90)
        
        self.lista_exercicios = [supino, agachamento, remada]
        self.exercicio = supino

        treinoA = Treino("Treino A", "Hipertrofia", "Segunda e Quinta")
        treinoB = Treino("Treino B", "Hipertrofia", "Terça e Sexta")
        
        treinoA.adicionar_exercicio(supino)
        treinoA.adicionar_exercicio(remada)
        treinoB.adicionar_exercicio(agachamento)
        
        self.lista_treinos = [treinoA, treinoB]
        self.treino = treinoA

        self.gerente = Gerente("Marcos", 40, 85, 1.78, "Masculino", "Nenhuma", "(84)98888-0000", 7000.0, None)
        self.personal = Personal("Carlos", 30, 82, 1.80, "Masculino", "Nenhuma", "(84)99999-0000", 4500.0, "Musculação", None)

        self.filial = Filial(1, "Academia Central", "Rua Principal, 100", "(84)3333-3333", self.gerente, 300)
        self.gerente.filial = self.filial
        self.personal.filial = self.filial

        aluno1 = Aluno("Felipe", 18, 70, 1.75, "Masculino", "Nenhuma", "(84)99999-1111", "2025001", "Premium", "Hipertrofia", self.filial)
        aluno2 = Aluno("João", 22, 82, 1.81, "Masculino", "Nenhuma", "(84)99999-2222", "2025002", "Gold", "Emagrecimento", self.filial)

        self.lista_alunos = [aluno1, aluno2]
        self.aluno = aluno1

        self.filial.adicionar_aluno(aluno1)
        self.filial.adicionar_aluno(aluno2)
        self.filial.adicionar_personal(self.personal)
        self.personal.adicionar_aluno(aluno1)
        self.personal.adicionar_aluno(aluno2)
        self.gerente.contratar_personal(self.personal)

        aluno1.adicionar_treino(treinoA, 1)
        aluno1.adicionar_treino(treinoB, 2)
        aluno2.adicionar_treino(treinoB, 1)

        self.rede = RedeAcademia("Academia PowerFit", "00.000.000/0001-00")
        self.rede.adicionar_filial(self.filial)

        a.salvar_dados_academia(self.rede, self.filial, self.gerente, self.personal, self.lista_alunos, self.lista_exercicios, self.lista_treinos)

    def menu_principal(self):
        while True:
            print("\n=================================")
            print("   SISTEMA DE GERENCIAMENTO FIT  ")
            print("=================================")
            print("Selecione um objeto para gerenciar:")
            print("1. Aluno (Pessoa)")
            print("2. Personal Trainer (Pessoa)")
            print("3. Gerente (Pessoa)")
            print("4. Exercício")
            print("5. Treino")
            print("6. Filial")
            print("7. Rede de Academias")
            print("0. Salvar e Sair")
            print("=================================")
            
            opcao = input("Opção: ").strip()
            
            if opcao == "1":
                self.gerenciar_aluno()
            elif opcao == "2":
                self.gerenciar_personal()
            elif opcao == "3":
                self.gerenciar_gerente()
            elif opcao == "4":
                self.gerenciar_exercicio()
            elif opcao == "5":
                self.gerenciar_treino()
            elif opcao == "6":
                self.gerenciar_filial()
            elif opcao == "7":
                self.gerenciar_rede_academia()
            elif opcao == "0":
                a.salvar_dados_academia(self.rede, self.filial, self.gerente, self.personal, self.lista_alunos, self.lista_exercicios, self.lista_treinos)
                print("Saindo do sistema... Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def gerenciar_aluno(self):
        while True:
            print(f"\n--- GERENCIAR ALUNO ({self.aluno.nome}) ---")
            print("1. Exibir dados completos")
            print("2. Alterar Peso e Altura (Recalcular IMC)")
            print("3. Consultar Treino por Dia")
            print("4. Registrar Presença")
            print("5. Consultar Presença")
            print("6. Mudar Aluno em Foco")
            print("0. Voltar")
            
            op = input("Opção: ").strip()
            if op == "1":
                self.aluno.exibir_dados()
            elif op == "2":
                try:
                    peso = float(input("Novo peso (kg): "))
                    altura = float(input("Nova altura (m): "))
                    self.aluno.atualizar_dados(peso, altura)
                    print("Dados atualizados e IMC recalculado com sucesso!")
                except ValueError:
                    print("Entrada inválida. Digite números válidos.")
            elif op == "3":
                try:
                    dia = int(input("Digite o dia (1-Segunda a 7-Domingo): "))
                    self.aluno.consultar_treino(dia)
                except ValueError:
                    print("Digite um número de 1 a 7.")
            elif op == "4":
                self.aluno.registrador_presenca()
            elif op == "5":
                self.aluno.consultar_presenca()
            elif op == "6":
                print("\nAlunos disponíveis:")
                for idx, alu in enumerate(self.lista_alunos):
                    print(f"[{idx}] {alu.nome} (Matrícula: {alu.matricula})")
                try:
                    escolha = int(input("Selecione o número do aluno: "))
                    if 0 <= escolha < len(self.lista_alunos):
                        self.aluno = self.lista_alunos[escolha]
                        print(f"Aluno em foco alterado para: {self.aluno.nome}")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Escolha numérica inválida.")
            elif op == "0":
                break

    def gerenciar_personal(self):
        while True:
            print(f"\n--- GERENCIAR PERSONAL ({self.personal.nome}) ---")
            print("1. Exibir dados completos")
            print("2. Gerar Relatório (Mixin)")
            print("3. Ver Salário")
            print("4. Alterar Salário")
            print("5. Listar Alunos sob responsabilidade")
            print("0. Voltar")
            
            op = input("Opção: ").strip()
            if op == "1":
                self.personal.exibir_dados()
            elif op == "2":
                self.personal.gerar_relatorio()
            elif op == "3":
                print(f"Salário atual: R$ {self.personal.get_consultar_salario():.2f}")
            elif op == "4":
                try:
                    novo_salario = float(input("Novo salário (R$): "))
                    self.personal.set_alterar_salario(novo_salario)
                    print("Salário alterado com sucesso!")
                except ValueError:
                    print("Valor inválido.")
            elif op == "5":
                self.personal.listar_alunos()
            elif op == "0":
                break

    def gerenciar_gerente(self):
        while True:
            print(f"\n--- GERENCIAR GERENTE ({self.gerente.nome}) ---")
            print("1. Exibir dados completos")
            print("2. Realizar Login")
            print("3. Ver Salário")
            print("4. Alterar Salário")
            print("5. Listar Personais contratados")
            print("0. Voltar")
            
            op = input("Opção: ").strip()
            if op == "1":
                self.gerente.exibir_dados()
            elif op == "2":
                self.gerente.login()
            elif op == "3":
                print(f"Salário do Gerente: R$ {self.gerente.get_consultar_salario():.2f}")
            elif op == "4":
                try:
                    novo_salario = float(input("Novo salário do Gerente (R$): "))
                    self.gerente.set_alterar_salario(novo_salario)
                    print("Salário atualizado!")
                except ValueError:
                    print("Valor inválido.")
            elif op == "5":
                self.gerente.listar_personais()
            elif op == "0":
                break

    def gerenciar_exercicio(self):
        while True:
            print(f"\n--- GERENCIAR EXERCÍCIO ({self.exercicio.nome}) ---")
            print("1. Exibir informações do exercício")
            print("2. Alterar Carga")
            print("3. Alterar Séries")
            print("4. Alterar Repetições")
            print("5. Alterar Tempo de Descanso")
            print("6. Mudar Exercício em Foco")
            print("0. Voltar")
            
            op = input("Opção: ").strip()
            if op == "1":
                self.exercicio.exibir_exercicio()
            elif op == "2":
                try:
                    carga = float(input("Nova carga (kg): "))
                    self.exercicio.alterar_carga(carga)
                    print("Carga alterada!")
                except ValueError:
                    print("Valor inválido.")
            elif op == "3":
                try:
                    series = int(input("Novas séries: "))
                    self.exercicio.alterar_series(series)
                    print("Séries alteradas!")
                except ValueError:
                    print("Valor inválido.")
            elif op == "4":
                try:
                    reps = int(input("Novas repetições: "))
                    self.exercicio.alterar_repeticoes(reps)
                    print("Repetições alteradas!")
                except ValueError:
                    print("Valor inválido.")
            elif op == "5":
                try:
                    descanso = int(input("Novo tempo de descanso (segundos): "))
                    self.exercicio.alterar_descanso(descanso)
                    print("Tempo de descanso alterado!")
                except ValueError:
                    print("Valor inválido.")
            elif op == "6":
                print("\nExercícios disponíveis:")
                for idx, ex in enumerate(self.lista_exercicios):
                    print(f"[{idx}] {ex.nome} (Grupo: {ex.grupo_muscular})")
                try:
                    escolha = int(input("Selecione o número do exercício: "))
                    if 0 <= escolha < len(self.lista_exercicios):
                        self.exercicio = self.lista_exercicios[escolha]
                        print(f"Exercício em foco alterado para: {self.exercicio.nome}")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Escolha numérica inválida.")
            elif op == "0":
                break

    def gerenciar_treino(self):
        while True:
            print(f"\n--- GERENCIAR TREINO ({self.treino.nome}) ---")
            print("1. Exibir Exercícios do Treino")
            print("2. Alterar Objetivo do Treino")
            print("3. Alterar Repetição/Dias do Treino")
            print("4. Vincular Exercício de Foco ao Treino")
            print("5. Mudar Treino em Foco")
            print("0. Voltar")
            
            op = input("Opção: ").strip()
            if op == "1":
                self.treino.exibir_exercicios()
            elif op == "2":
                obj = input("Novo objetivo do treino: ")
                self.treino.alterar_objetivo(obj)
                print("Objetivo atualizado!")
            elif op == "3":
                rep = input("Novas repetições/frequência: ")
                self.treino.alterar_repeticao(rep)
                print("Frequência atualizada!")
            elif op == "4":
                self.treino.adicionar_exercicio(self.exercicio)
                print(f"Exercício '{self.exercicio.nome}' adicionado ao treino!")
            elif op == "5":
                print("\nTreinos disponíveis:")
                for idx, tr in enumerate(self.lista_treinos):
                    print(f"[{idx}] {tr.nome} (Objetivo: {tr.objetivo_treino})")
                try:
                    escolha = int(input("Selecione o número do treino: "))
                    if 0 <= escolha < len(self.lista_treinos):
                        self.treino = self.lista_treinos[escolha]
                        print(f"Treino em foco alterado para: {self.treino.nome}")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Escolha numérica inválida.")
            elif op == "0":
                break

    def gerenciar_filial(self):
        while True:
            print(f"\n--- GERENCIAR FILIAL ({self.filial.nome}) ---")
            print("1. Exibir dados da Filial")
            print("2. Listar Alunos matriculados nesta filial")
            print("3. Listar Personais que atuam aqui")
            print("4. Ver vagas disponíveis")
            print("0. Voltar")
            
            op = input("Opção: ").strip()
            if op == "1":
                self.filial.exibir_filial()
            elif op == "2":
                self.filial.listar_alunos()
            elif op == "3":
                self.filial.listar_personais()
            elif op == "4":
                print(f"Capacidade: {self.filial.capacidade}")
                print(f"Vagas ainda disponíveis: {self.filial.vagas_disponiveis()}")
            elif op == "0":
                break

    def gerenciar_rede_academia(self):
        while True:
            print(f"\n--- GERENCIAR REDE ({self.rede.nome}) ---")
            print("1. Exibir dados da Rede")
            print("2. Listar filiais vinculadas")
            print("0. Voltar")
            
            op = input("Opção: ").strip()
            if op == "1":
                print(f"Rede: {self.rede.nome}")
                print(f"CNPJ: {self.rede.get_cnpj()}")
                print(f"Quantidade de filiais: {len(self.rede.filiais)}")
            elif op == "2":
                self.rede.listar_filiais()
            elif op == "0":
                break

if __name__ == "__main__":
    menu_sistema = Menu()
    menu_sistema.menu_principal()