class Pessoa:
    def _init_(self, nome, idade, peso, altura, sexo, limitacoes, telefone):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.sexo = sexo
        self.limitacoes = limitacoes
        self.telefone = telefone
        self.imc = [0, "Não foi avaliado"]

    def calcular_imc(self):
        self.imc[0] = self.peso / (self.altura ** 2)

        if self.imc[0] < 18.5:
            self.imc[1] = "Abaixo do peso"
        elif self.imc[0] < 25:
            self.imc[1] = "Peso Normal"
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
        print(f"IMC: {self.imc[0]:.2f} - {self.imc[1]}")
        return None

class Aluno(Pessoa):
    def _init_(self, nome, idade, peso, altura, sexo, limitacoes, telefone,
                 matricula, plano, objetivo, filial):
        super()._init_(nome, idade, peso, altura, sexo, limitacoes, telefone)
        self.matricula = matricula
        self.treino = [0]*5
        self.plano = plano
        self.objetivo = objetivo
        self.filial = filial
        self.frequencia = ['Ausente']*7

    def adicionar_treino(self,treino,dia):#Dia vai de 1 a 5, segunda a sexta
        self.treino[dia-1] = treino
        return None
   
    def consultar_treino(self,dia):#Dia vai de 1 a 5, segunda a sexta
        print(f"=== {self.treino[dia-1].nome} ===")
        print(f"Objetivo: {self.treino[dia-1].objetivo_treino}")
        print(f"Repetições: {self.treino[dia-1].repeticao}")
        print("Exercícios:")
        self.treino[dia-1].exibir_exercicios()

    def registrador_presenca(self):
        if 'Ausente' in self.frequencia:
            for i in range(len(self.frequencia)):
                if self.frequencia[i] == 'Ausente':
                    self.frequencia[i] = 'Presente'
                    break
        else:
            self.frequencia = ['Ausente']*7
            print('Sua frequência foi reiniciada')
        return None
    def consultar_presenca(self):
        print(self.frequencia)
        return None
class Personal(Pessoa):
    def _init_(self, nome, idade, peso, altura, sexo, limitacoes, telefone,
                 salario, especialidade, alunos, filial):
        super()._init_(nome, idade, peso, altura, sexo, limitacoes, telefone)
        self.__salario = salario
        self.especialidade = especialidade
        self.alunos = alunos
        self.filial = filial


class Gerente(Pessoa):
    def _init_(self, nome, idade, peso, altura, sexo, limitacoes, telefone,
                 salario, filial, personais, funcionarios):
        super()._init_(nome, idade, peso, altura, sexo, limitacoes, telefone)
        self.__salario = salario
        self.filial = filial
        self.personais = personais
        self.funcionarios = funcionarios


class Exercicio:
    def _init_(self, nome, grupo_muscular, series, repeticoes, carga, descanso):
        self.nome = nome
        self.grupo_muscular = grupo_muscular
        self.series = series
        self.repeticoes = repeticoes
        self.carga = carga
        self.descanso = descanso
    def alterar_carga(self,carga):
        self.carga=carga
    def alterar_series(self,series):
        self.series=series
    def alterar_repeticoes(self,repeticoes):
        self.repeticoes=repeticoes

class Treino:
    def _init_(self, nome, objetivo_treino, repeticao):
        self.nome = nome
        self.objetivo_treino = objetivo_treino
        self.repeticao = repeticao
        self.exercicios = []
    def adicionar_exercício(self,exercicio):
        self.exercicios.append(exercicio)
        return None
    def remover_exercicio(self,exercicio):
        self.exercicios.remove(exercicio)
        return None
    def alterar_objetivo(self,objetivo):
        self.objetivo_treino = objetivo
        return None
    def exibir_exercicios(self):
        for i in self.exercicios:
            print(f'Exercício: {i.nome}')
        return None

class Filial:
    def init(self, codigo, nome, endereco, telefone, gerente,
                 alunos, personais, capacidade):
        self.__codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.gerente = gerente
        self.alunos = []
        self.personais = []
        self.capacidade = capacidade
   
    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)
       
    def remover_aluno(self,aluno):
        self.alunos.remove(aluno)
   
    def adicionar_personal(self,personal):
        self.personais.append(personal)
   
    def remover_personal(self,personal):
        self.personais.remove(personal)

    def buscar_personal(self,personal):
        if personal in self.personais:
            print(f'personal:{personal} encontrado,')
            personal.exibir_dados()
            return personal

    def buscar_aluno(self,aluno):
        if aluno in self.alunos:
            print(f'aluno:{aluno} encontrado,')
            aluno.exibir_dados()
            return aluno
   
    def calcular_lotação(self,quantidades_de_alunos,aluno):
        quantidades_de_alunos=0
        for aluno in range(len(self.alunos)):
            if aluno in self.alunos:
                quantidades_de_alunos+=1
            return quantidades_de_alunos
   
    def listar_alunos(self):
        return self.alunos
   
    def listar_personais(self):
        return self.personais


class RedeAcademia:
    def _init_(self, nome, cnpj, filiais):
        self.nome = nome
        self.__cnpj = cnpj
        self.filiais = filiais