from docx import Document
from docx.shared import Pt

from openpyxl import load_workbook
import os

#Abre o arquivo do excel
nome_arquivo_alunos = "C:\\Users\\roti5\\OneDrive\\Documentos\\PROGRAMAÇÃO\\Curso lógica de programação - Udemy\\Python\\Automação em Word\\Alunos.xlsx"
planilhaDadosAlunos = load_workbook(nome_arquivo_alunos)

#Selecionando a aba "Nomes" do arquivo excel
sheet_selecionada = planilhaDadosAlunos["Nomes"]

#Para cada linha da coluna A, a partir da segunda linha até a última linha da planilha (inclusive)
for linha in range(2, len(sheet_selecionada["A"]) + 1):
    #Abre o arquivo do word
    arquivoWord = Document("C:\\Users\\roti5\\OneDrive\\Documentos\\PROGRAMAÇÃO\\Curso lógica de programação - Udemy\\Python\\Automação em Word\\Certificado1.docx")

    #Seleciona o estilo
    estilo = arquivoWord.styles["Normal"]

    #Pegando o valor de cada linha da coluna A e transformando o conteúdo em texto (ex.: A2, A3,...)
    nomeAluno = sheet_selecionada['A%s' % linha].value

    for paragrafo in arquivoWord.paragraphs:

        #Vai substituir o @nome pelo nome da pessoa
        if "@nome" in paragrafo.text:
            paragrafo.text = nomeAluno
            fonte = estilo.font
            fonte.name = "Arial"
            fonte.size = Pt(20)

    #Pegando o caminho da pasta e configurando o nome do certificado
    caminhoCertificados = "C:\\Users\\roti5\\OneDrive\\Documentos\\PROGRAMAÇÃO\\Curso lógica de programação - Udemy\\Python\\Automação em Word\\Certificados\\" + nomeAluno + ".docx"

    #Salvando o certificado do aluno
    arquivoWord.save(caminhoCertificados)

print("Certificados gerados com sucesso")

