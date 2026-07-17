import csv
import os
from main import Aluno, Personal, Gerente, Exercicio, Treino, Filial, RedeAcademia

def buscar_exercicio(nome, lista_exercicios):
    for ex in lista_exercicios:
        if ex.nome == nome:
            return ex
    return None

def buscar_treino(nome, lista_treinos):
    for tr in lista_treinos:
        if tr.nome == nome:
            return tr
    return None

def buscar_aluno(matricula, lista_alunos):
    for alu in lista_alunos:
        if alu.matricula == matricula:
            return alu
    return None

def salvar_dados_academia(rede, filial, gerente, personal, lista_alunos, lista_exercicios, lista_treinos):
    with open('filiais.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['rede_nome', 'rede_cnpj', 'filial_codigo', 'filial_nome', 'filial_endereco', 'filial_telefone', 'filial_capacidade', 'gerente_nome'])
        writer.writerow([rede.nome, rede.get_cnpj(), filial.get_codigo(), filial.nome, filial.endereco, filial.telefone, filial.capacidade, gerente.nome])


    with open('funcionarios.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['nome', 'idade', 'peso', 'altura', 'sexo', 'limitacoes', 'telefone', 'cargo', 'salario', 'especialidade', 'filial_nome'])
        writer.writerow([gerente.nome, gerente.idade, gerente.peso, gerente.altura, gerente.sexo, gerente.limitacoes, gerente.telefone, "Gerente", gerente.get_consultar_salario(), gerente.especialidade, filial.nome])
        writer.writerow([personal.nome, personal.idade, personal.peso, personal.altura, personal.sexo, personal.limitacoes, personal.telefone, "Personal Trainer", personal.get_consultar_salario(), personal.especialidade, filial.nome])


    with open('alunos.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['matricula', 'nome', 'idade', 'peso', 'altura', 'sexo', 'limitacoes', 'telefone', 'plano', 'objetivo', 'imc_valor', 'imc_classificacao', 'filial_nome', 'personal_responsavel'])
        for alu in lista_alunos:
            nome_personal = personal.nome if alu in personal.alunos else "Não atribuído"
            writer.writerow([alu.matricula, alu.nome, alu.idade, alu.peso, alu.altura, alu.sexo, alu.limitacoes, alu.telefone, alu.plano, alu.objetivo, f"{alu.imc[0]:.2f}", alu.imc[1], filial.nome, nome_personal])


    with open('exercicios.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['nome', 'grupo_muscular', 'series', 'repeticoes', 'carga_kg', 'descanso_segundos'])
        for ex in lista_exercicios:
            writer.writerow([ex.nome, ex.grupo_muscular, ex.series, ex.repeticoes, ex.carga, ex.descanso])


    with open('treinos.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['treino_nome', 'objetivo_treino', 'frequencia', 'exercicio_nome'])
        for tr in lista_treinos:
            for ex in tr.exercicios:
                writer.writerow([tr.nome, tr.objetivo_treino, tr.repeticao, ex.nome])


    with open('agenda_treinos_alunos.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['aluno_nome', 'matricula', 'dia_semana', 'treino_nome'])
        for alu in lista_alunos:
            for idx, tr in enumerate(alu.treino):
                if tr is not None:
                    writer.writerow([alu.nome, alu.matricula, idx + 1, tr.nome])


def carregar_dados_academia():
    lista_exercicios = []
    lista_treinos = []
    lista_alunos = []
    

    if not os.path.exists("alunos.csv"):
        return None

    try:
        rede = RedeAcademia()
        rede._init_("Academia PowerFit", "00.000.000/0001-00")
        
        filial = Filial()
        filial._init_(1, "Academia Central", "Rua Principal, 100", "(84)3333-3333", None, 300)
        rede.adicionar_filial(filial)


        with open("exercicios.csv", mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                ex = Exercicio()
                ex._init_(r[0], r[1], int(r[2]), int(r[3]), float(r[4]), int(r[5]))
                lista_exercicios.append(ex)


        with open("treinos.csv", mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                t_nome = r[0]
                t_obj = r[1]
                t_freq = r[2]
                ex_nome = r[3]
                

                t = buscar_treino(t_nome, lista_treinos)
                if t is None:
                    t = Treino()
                    t._init_(t_nome, t_obj, t_freq)
                    lista_treinos.append(t)
                
                ex_obj = buscar_exercicio(ex_nome, lista_exercicios)
                if ex_obj is not None:
                    t.adicionar_exercicio(ex_obj)


        gerente = None
        personal = None
        with open("funcionarios.csv", mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                if r[7] == "Gerente":
                    gerente = Gerente()
                    gerente._init_(r[0], int(r[1]), float(r[2]), float(r[3]), r[4], r[5], r[6], float(r[8]), filial, r[9])
                    filial.gerente = gerente
                elif r[7] == "Personal Trainer":
                    personal = Personal()
                    personal._init_(r[0], int(r[1]), float(r[2]), float(r[3]), r[4], r[5], r[6], float(r[8]), r[9], filial)
                    filial.adicionar_personal(personal)
        
        if gerente is not None and personal is not None:
            gerente.contratar_personal(personal)


        with open("alunos.csv", mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            for r in reader:
                alu = Aluno()
                alu._init_(r[1], int(r[2]), float(r[3]), float(r[4]), r[5], r[6], r[7], r[0], r[8], r[9], filial)
                alu.imc = [float(r[10]), r[11]]
                lista_alunos.append(alu)
                filial.adicionar_aluno(alu)
                
                if personal is not None and r[13] == personal.nome:
                    personal.adicionar_aluno(alu)


        if os.path.exists("agenda_treinos_alunos.csv"):
            with open("agenda_treinos_alunos.csv", mode="r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for r in reader:
                    matricula = r[1]
                    dia_semana = int(r[2])
                    treino_nome = r[3]
                    
                    alu_obj = buscar_aluno(matricula, lista_alunos)
                    tr_obj = buscar_treino(treino_nome, lista_treinos)
                    
                    if alu_obj is not None and tr_obj is not None:
                        alu_obj.adicionar_treino(tr_obj, dia_semana)

        return [rede, filial, gerente, personal, lista_alunos, lista_exercicios, lista_treinos]
    except Exception as e:
        print(f"Não foi possível carregar os dados salvos: {e}")
        return None