class Pessoa:

    def __init__ (self):
        self.nome = 'Joao'
        self.idade = None
        self.endereco = None
        self.curso = None
    
    def getNome (self):
        return self.nome

    def getIdade (self):
        return self.idade

    def getEndereco (self):
        return self.endereco

    def getCurso (self):
        return self.curso

    def setNome (self, nome):
        self.nome = nome

    def setIdade (self, idade):
        self.idade = idade

    def setEndereco (self, endereco):
        self.endereco = endereco

    def setCurso (self, curso):
        self.curso = curso
    

    