from docx import Document
from docx.shared import Pt

from openpyxl import load_workbook
import os

#Abre o arquivo do excel
nome_arquivo_alunos = "C:\\Users\\roti5\\OneDrive\\Documentos\\PROGRAMAÇÃO\\Curso lógica de programação - Udemy\\Python\\Automação em Word\\Gerando Certificados em Massa por Informações do Excel\\DadosAlunos.xlsx"
planilhaDadosAlunos = load_workbook(nome_arquivo_alunos)

#Selecionando a aba "Nomes" do arquivo excel
sheet_selecionada = planilhaDadosAlunos["Nomes"]

#Para cada linha da coluna A, a partir da segunda linha até a última linha da planilha (inclusive)
for linha in range(2, len(sheet_selecionada["A"]) + 1):
    #Abre o arquivo do word
    arquivoWord = Document("C:\\Users\\roti5\\OneDrive\\Documentos\\PROGRAMAÇÃO\\Curso lógica de programação - Udemy\\Python\\Automação em Word\\Gerando Certificados em Massa por Informações do Excel\\Certificado2.docx")

    #Seleciona o estilo
    estilo = arquivoWord.styles["Normal"]

    #Pegando o valor de cada linha das colunas e transformando o conteúdo em texto
    nomeAluno = sheet_selecionada['A%s' % linha].value
    dia = sheet_selecionada['B%s' % linha].value
    mes = sheet_selecionada['C%s' % linha].value
    ano = sheet_selecionada['D%s' % linha].value
    nomeCurso = sheet_selecionada['E%s' % linha].value
    nomeInstrutor = sheet_selecionada['F%s' % linha].value

    for paragrafo in arquivoWord.paragraphs:

        #Vai substituir o @nome pelo nome da pessoa
        if "@nome" in paragrafo.text:
            paragrafo.text = nomeAluno
            fonte = estilo.font
            fonte.name = "Arial"
            fonte.size = Pt(20)

        paragrafoP1 = "Concluiu com sucesso o curso de"
        paragrafoP2 = ", com carga horária de 20 horas, promovido pela escola de Cursos Online em"
        #Função f para montar uma cadeia de texto e organizar as variáveis para substituir as informações
        paragrafoCompleto = f"{paragrafoP1} {nomeCurso}{paragrafoP2} {dia} de {mes} de {ano}."

        # Vai substituir a palavra "escola" pelo parágrafo com as informações de cada estudante
        if "escola" in paragrafo.text:
            paragrafo.text = paragrafoCompleto
            fonte = estilo.font
            fonte.name = "Arial"
            fonte.size = Pt(20)

        # Vai substituir a palavra "Instrutor" pelo parágrafo com o nome do Instrutor do curso que o aluno realizou
        if "Instrutor" in paragrafo.text:
            paragrafo.text = nomeInstrutor + " - Instrutor"
            fonte = estilo.font
            fonte.name = "Arial"
            fonte.size = Pt(20)

    #Pegando o caminho da pasta e configurando o nome do certificado
    caminhoCertificados = "C:\\Users\\roti5\\OneDrive\\Documentos\\PROGRAMAÇÃO\\Curso lógica de programação - Udemy\\Python\\Automação em Word\\Gerando Certificados em Massa por Informações do Excel\\Certificados_Informacoes\\ " + nomeAluno + ".docx"

    #Salvando o certificado do aluno
    arquivoWord.save(caminhoCertificados)

print("Certificados gerados com sucesso")

