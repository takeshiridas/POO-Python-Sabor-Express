from modelos.restaurante import Restaurante

from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praca', 'Comida Brasileira')
restaurante_mexicano = Restaurante('Mexican Food', 'Comida Mexicana')
restaurante_japones = Restaurante('Japa', 'Comida Japonesa')

bebida_refrigerante = Bebida('Coca Cola', 5.0, '600ml')
bebida_refrigerante.aplicar_desconto()

prato_sushi = Prato('Sushi', 20.0, 'Uramaki de salmao')
prato_sushi.aplicar_desconto()

restaurante_japones.adicionar_no_cardapio(bebida_refrigerante)
restaurante_japones.adicionar_no_cardapio(prato_sushi)

def main():
    restaurante_japones.exibir_cardapio

if __name__ == "__main__":
    main()