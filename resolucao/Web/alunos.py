class Alunos:
    def __init__(self, nome, sobrenome, telefone):
        self.Nome = nome
        self.Sobrenome = sobrenome
        self.Telefone = telefone
    
    def nome_completo(self):
        nomecompleto = self.Nome + " " + self.Sobrenome
        return nomecompleto