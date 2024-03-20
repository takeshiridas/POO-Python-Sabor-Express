from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Comida Brasileira')
restaurante_mexicano = Restaurante('Mexican Food', 'Comida Mexicana')
restaurante_japones = Restaurante('Japa', 'Comida Japonesa')

restaurante_japones.alternar_estado()
restaurante_japones.receber_avaliacao('Joao', 4)
restaurante_japones.receber_avaliacao('Maria', 5)
restaurante_japones.receber_avaliacao('Jose', 3)

restaurante_praca.alternar_estado()
restaurante_praca.receber_avaliacao('Joao', 10)
restaurante_praca.receber_avaliacao('Maria', 9)
restaurante_praca.receber_avaliacao('Jose', 8)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()