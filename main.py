"""Sistema de gerenciamento de academia.
Módulo com classes para gerenciamento de alunos, personais, gerentes,
treinos, exercícios, filiais e rede de academias."""

from abc import ABC, abstractmethod 

class Autenticavel(ABC):
    """Interface para autenticação."""
    @abstractmethod
    def tipo_usuario(self):
        pass

class RelatorioMixin:
    """Mixin para geração de relatórios."""
    def gerar_relatorio(self):
        print("===== RELATÓRIO =====")
        self.exibir_dados()

class Pessoa(RelatorioMixin):
    """Classe base abstrata para pessoas da academia."""
    def _init_(self, nome, idade, peso, altura, sexo,
                 limitacoes, telefone):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.limitacoes = limitacoes
        self.telefone = telefone
        self.imc = [0, "Não avaliado"]

    def calcular_imc(self):
        self.imc[0] = self.peso / (self.altura ** 2)

        if self.imc[0] < 18.5:
            self.imc[1] = "Abaixo do peso"

        elif self.imc[0] < 25:
            self.imc[1] = "Peso normal"

        elif self.imc[0] < 30:
            self.imc[1] = "Sobrepeso"

        else:
            self.imc[1] = "Obesidade"

    def atualizar_dados(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.calcular_imc()

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso} kg")
        print(f"Altura: {self.altura} m")
        print(f"Sexo: {self.sexo}")
        print(f"Limitações: {self.limitacoes}")
        print(f"Telefone: {self.telefone}")
        print(f"IMC: {self.imc[0]:.2f} ({self.imc[1]})")

class Aluno(Pessoa,Autenticavel):
    """Representa um aluno da academia."""

    def _init_(self, nome, idade, peso, altura, sexo,
                 limitacoes, telefone, matricula,
                 plano, objetivo, filial):

        super()._init_(nome, idade, peso, altura,
                         sexo, limitacoes, telefone)

        self.matricula = matricula
        self.plano = plano
        self.objetivo = objetivo
        self.filial = filial
        self.treino = [None] * 7
        self.frequencia = ["Ausente"] * 7

    def tipo_usuario(self):
        return "Aluno"

    def adicionar_treino(self, treino, dia):
        if 1 <= dia <= 7:
            self.treino[dia - 1] = treino
        else:
            print("Dia inválido.")

    def consultar_treino(self, dia):
        dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
        if 1 <= dia <= 7:
            treino = self.treino[dia - 1]
            print(f"\nDia: {dias[dia - 1]}")
            if treino:
                print(f"Treino: {treino.nome}")
                print(f"Objetivo: {treino.objetivo_treino}")
                print(f"Repetição: {treino.repeticao}")
                treino.exibir_exercicios()
            else:
                print("Nenhum treino cadastrado.")
        else:
            print("Dia inválido.")

    def registrador_presenca(self):
        for i in range(len(self.frequencia)):
            if self.frequencia[i] == "Ausente":
                self.frequencia[i] = "Presente"
                return
        print("Semana encerrada.")
        self.frequencia = ["Ausente"] * 7

    def consultar_presenca(self):
        dias = ["Seg", "Ter", "Qua", "Qui",
                "Sex", "Sáb", "Dom"]
        for dia, presenca in zip(dias, self.frequencia):
            print(f"{dia}: {presenca}")

class Personal(Pessoa,Autenticavel):
    """Representa um personal trainer."""

    def _init_(self, nome, idade, peso, altura, sexo,
                 limitacoes, telefone,
                 salario, especialidade,
                 filial):

        super()._init_(nome, idade, peso, altura, sexo, limitacoes, telefone)
        self.__salario = salario
        self.especialidade = especialidade
        self.alunos = []
        self.filial = filial

    def tipo_usuario(self):
        return "Personal"

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            self.alunos.append(aluno)

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def listar_alunos(self):
        print("=== ALUNOS ===")
        for aluno in self.alunos:
            print(aluno.nome)

    def set_alterar_salario(self, salario):
        self.__salario = salario

    def get_consultar_salario(self):
        return self.__salario



class Gerente(Personal,Autenticavel):
    """Representa o gerente da filial."""

    def _init_(self, nome, idade, peso, altura,sexo, limitacoes, telefone,salario, filial,especialidade='Comandar'):
        super()._init_(nome, idade, peso,altura, sexo,limitacoes, telefone,salario,filial,especialidade)
        self.personais = []

    def tipo_usuario(self):
        return "Gerente"

    def login(self):
        print("Gerente autenticado.")

    def contratar_personal(self, personal):
        if personal not in self.personais:
            self.personais.append(personal)

    def demitir_personal(self, personal):
        if personal in self.personais:
            self.personais.remove(personal)

    def listar_personais(self):
        print("=== PERSONAIS ===")
        for personal in self.personais:
            print(personal.nome)

def imprimir_dados(obj):
    """Exibe os dados de um objeto compatível."""
    obj.exibir_dados()

def mostrar_tipo(pessoa):
    """Exibe o tipo de usuário."""
    print(pessoa.tipo_usuario())


class Exercicio:
    """Representa um exercício físico."""

    def _init_(self, nome, grupo_muscular,series, repeticoes,carga, descanso):
        self.nome = nome
        self.grupo_muscular = grupo_muscular
        self.series = series
        self.repeticoes = repeticoes
        self.carga = carga
        self.descanso = descanso

    def alterar_carga(self, carga):
        self.carga = carga

    def alterar_series(self, series):
        self.series = series

    def alterar_repeticoes(self, repeticoes):
        self.repeticoes = repeticoes

    def alterar_descanso(self, descanso):
        self.descanso = descanso

    def exibir_exercicio(self):
        print(f"Exercício: {self.nome}")
        print(f"Grupo muscular: {self.grupo_muscular}")
        print(f"Séries: {self.series}")
        print(f"Repetições: {self.repeticoes}")
        print(f"Carga: {self.carga} kg")
        print(f"Descanso: {self.descanso} s")


class Treino:
    """Representa um treino composto por exercícios."""

    def _init_(self, nome,objetivo_treino,repeticao):
        self.nome = nome
        self.objetivo_treino = objetivo_treino
        self.repeticao = repeticao
        self.exercicios = []

    def adicionar_exercicio(self, exercicio):
        if exercicio not in self.exercicios:
            self.exercicios.append(exercicio)

    def remover_exercicio(self, exercicio):
        if exercicio in self.exercicios:
            self.exercicios.remove(exercicio)

    def alterar_objetivo(self, objetivo):
        self.objetivo_treino = objetivo

    def alterar_repeticao(self, repeticao):
        self.repeticao = repeticao

    def buscar_exercicio(self, nome):
        for exercicio in self.exercicios:
            if exercicio.nome == nome:
                return exercicio
        return None

    def listar_exercicios(self):
        return self.exercicios

    def exibir_exercicios(self):
        print(f"\n=== Treino {self.nome} ===")
        for exercicio in self.exercicios:
            exercicio.exibir_exercicio()
            print("---------------------")



class Filial:
    """Representa uma filial da academia."""

    def _init_(self,codigo,nome,endereco,telefone,gerente,capacidade):

        self.__codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.gerente = gerente
        self.capacidade = capacidade

        self.alunos = []
        self.personais = []

    def get_codigo(self):
        return self.__codigo

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos:
            if self.calcular_lotacao() < self.capacidade:
                self.alunos.append(aluno)
            else:
                print("Capacidade máxima atingida.")

    def remover_aluno(self, aluno):
        if aluno in self.alunos:
            self.alunos.remove(aluno)

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        return None

    def listar_alunos(self):
        print("\n=== ALUNOS ===")
        for aluno in self.alunos:
            print(aluno.nome)


    def adicionar_personal(self, personal):
        if personal not in self.personais:
            self.personais.append(personal)

    def remover_personal(self, personal):
        if personal in self.personais:
            self.personais.remove(personal)

    def buscar_personal(self, nome):
        for personal in self.personais:
            if personal.nome == nome:
                return personal
        return None

    def listar_personais(self):
        print("\n=== PERSONAIS ===")
        for personal in self.personais:
            print(personal.nome)

    def calcular_lotacao(self):
        return len(self.alunos)

    def vagas_disponiveis(self):
        return self.capacidade - len(self.alunos)

    def exibir_filial(self):
        print(f"Código: {self.__codigo}")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
        print(f"Capacidade: {self.capacidade}")
        print(f"Alunos matriculados: {len(self.alunos)}")
        print(f"Personais: {len(self.personais)}")



class RedeAcademia:
    """Representa a rede de academias."""

    def _init_(self,nome,cnpj):
        self.nome = nome
        self.__cnpj = cnpj
        self.filiais = []

    def get_cnpj(self):
        return self.__cnpj

    def adicionar_filial(self, filial):
        if filial not in self.filiais:
            self.filiais.append(filial)

    def remover_filial(self, filial):
        if filial in self.filiais:
            self.filiais.remove(filial)

    def buscar_filial(self, codigo):
        for filial in self.filiais:
            if filial.get_codigo() == codigo:
                return filial
        return None

    def listar_filiais(self):

        print("\n===== FILIAIS =====")

        for filial in self.filiais:
            print(f"{filial.get_codigo()} - {filial.nome}")

    def total_alunos(self):
        total = 0
        for filial in self.filiais:
            total += len(filial.alunos)
        return total

    def total_personais(self):
        total = 0
        for filial in self.filiais:
            total += len(filial.personais)
        return total

    def exibir_rede(self):
        print(f"Rede: {self.nome}")
        print(f"CNPJ: {self.__cnpj}")
        print(f"Quantidade de filiais: {len(self.filiais)}")
        print(f"Total de alunos: {self.total_alunos()}")
        print(f"Total de personais: {self.total_personais()}")

supino = Exercicio(
    "Supino Reto",
    "Peitoral",
    4,
    10,
    40,
    90
)

agachamento = Exercicio(
    "Agachamento",
    "Pernas",
    4,
    12,
    60,
    120
)

remada = Exercicio(
    "Remada Curvada",
    "Costas",
    4,
    10,
    45,
    90)


treinoA = Treino(
    "Treino A",
    "Hipertrofia",
    "Segunda e Quinta"
)

treinoB = Treino(
    "Treino B",
    "Hipertrofia",
    "Terça e Sexta"
)

treinoA.adicionar_exercicio(supino)
treinoA.adicionar_exercicio(remada)
treinoB.adicionar_exercicio(agachamento)
personal = Personal(
        "Carlos",
        30,
        82,
        1.80,
        "Masculino",
        "Nenhuma",
        "(84)99999-0000",
        4500,
        "Musculação",
        None
    )

gerente = Gerente(
        "Marcos",
        40,
        85,
        1.78,
        "Masculino",
        "Nenhuma",
        "(84)98888-0000",
        7000,
        None,
        []
    )

filial = Filial(
        1,
        "Academia Central",
        "Rua Principal, 100",
        "(84)3333-3333",
        gerente,
        300
    )


gerente.filial = filial
personal.filial = filial


aluno1 = Aluno(
        "Felipe",
        18,
        70,
        1.75,
        "Masculino",
        "Nenhuma",
        "(84)99999-1111",
        "2025001",
        "Premium",
        "Hipertrofia",
        filial
    )

aluno2 = Aluno(
        "João",
        22,
        82,
        1.81,
        "Masculino",
        "Nenhuma",
        "(84)99999-2222",
        "2025002",
        "Gold",
        "Emagrecimento",
        filial
    )


filial.adicionar_aluno(aluno1)
filial.adicionar_aluno(aluno2)

filial.adicionar_personal(personal)

personal.adicionar_aluno(aluno1)
personal.adicionar_aluno(aluno2)

gerente.contratar_personal(personal)


aluno1.adicionar_treino(treinoA,1)
aluno1.adicionar_treino(treinoB,2)

aluno2.adicionar_treino(treinoB,1)


aluno1.calcular_imc()
aluno2.calcular_imc()


aluno1.registrador_presenca()
aluno1.registrador_presenca()


print("\n======== DADOS DO ALUNO ========")

aluno1.exibir_dados()

print("\n======== TREINO ========")

aluno1.consultar_treino(1)

print("\n======== PRESENÇA ========")

aluno1.consultar_presenca()

print("\n======== FILIAL ========")

filial.exibir_filial()

print("\n======== REDE ========")

rede = RedeAcademia(
        "Academia PowerFit",
        "00.000.000/0001-00"
    )

rede.adicionar_filial(filial)

rede.exibir_rede()

print('\nPOLIMORFISMO\n')

pessoas = [
        aluno1,
        personal,
        gerente
    ]
for pessoa in pessoas:
        print(pessoa.nome,"->",pessoa.tipo_usuario())
print('\n')

imprimir_dados(aluno1)
imprimir_dados(personal)
imprimir_dados(gerente)


print("\n======== RELATÓRIO ========")

personal.gerar_relatorio()
gerente.gerar_relatorio()

print("\n======== LOGIN ========")

gerente.login()
