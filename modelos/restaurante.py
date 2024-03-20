from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(27)} | {"Categoria".ljust(25)} | {"Avaliacao".ljust(25)} | {"Status"}\n{"-"*27} | {"-"*25} | {"-"*25} | {"-"*6}')
        for restaurante in cls.restaurantes:
            print(f'- {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacao).ljust(25)} | {restaurante._ativo}')
    
    @property
    def ativo(self):
        return '✅' if self._ativo else '❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)    

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade = len(self._avaliacao)
        media = round(soma / quantidade, 1)
        return media
