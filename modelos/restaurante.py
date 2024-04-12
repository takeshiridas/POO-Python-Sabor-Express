from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
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
            return 'Sem avaliações'
        
        soma = sum(avaliacao._nota for avaliacao in self._avaliacao)/2
        quantidade = len(self._avaliacao)
        media = round(soma / quantidade, 1)
        return media

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome} \n')
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preco: R${item._preco} | Descricao: {item._descricao}'
                print(mensagem_prato)
            
            elif hasattr(item, '_tipo'):
                mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preco: R${item._preco} | Tipo: {item._tipo} | Tamanho: {item._tamanho}'
                print(mensagem_sobremesa)
            
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preco: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)