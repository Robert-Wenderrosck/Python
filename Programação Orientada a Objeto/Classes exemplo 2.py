#Ao invés do sel podemos usar o mysillyobject
class funcaoInformacoesAluno:

    def __init__(mysillyobject, nomeAluno, idadeAluno, mediaAluno):
        mysillyobject.nome = nomeAluno
        mysillyobject.idade = idadeAluno
        mysillyobject.media = mediaAluno

    def funcaoImprimirDados(mysillyobject):
        print("Nome:", mysillyobject.nome)
        print("Idade:", mysillyobject.idade)
        print("Média:", mysillyobject.media)

pegaInformacoes = funcaoInformacoesAluno("Ricardo", 21, 9)
pegaInformacoes.funcaoImprimirDados()

#-----------------------------------------------------------------------
print("\n")

class notasAluno:
    def __init__(self, nota1, nota2, nota3, nota4):
        self.n1 = nota1
        self.n2 = nota2
        self.n3 = nota3
        self.n4 = nota4

notas = notasAluno(9, 8, 7, 10)
print("Nota 3:", notas.n3)

#Alterando o objeto da classe (notasAluno)
notas.n3 = 10

print("Nota 3:", notas.n3)
