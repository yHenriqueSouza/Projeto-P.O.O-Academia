import csv

with open("Alunos.csv", "r") as arquivo:
    arquivo_alunos_csv = csv.reader(arquivo, delimeter=",")
    for linha in arquivo_alunos_csv:
        print(linha)