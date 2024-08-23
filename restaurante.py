class Restaurante:
    def __init__(self, nome, numero, ativo=False):
        self.nome = nome
        self.numero = numero
        self.ativo = ativo
        self.avaliacoes = []

    def ativar_desativar(self):
        self.ativo = not self.ativo
        if self.ativo:
            return f'O Contato {self.nome} foi ativado com sucesso.'
        else:
            return f'O Contato {self.nome} foi desativado com sucesso.'

    def __str__(self):
        return f'Nome: {self.nome.ljust(20)}  Número: {self.numero.ljust(22)}  Status: {"Ativado" if self.ativo else "Desativado"}'