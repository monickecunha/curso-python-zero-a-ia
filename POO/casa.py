class Casa:
    def __init__(self, cor, quartos, banheiros): # construtos
        self.cor = cor 
        self.quartos = quartos
        self.banheiros = banheiros
        
    # Métodos
    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}')
        
    def mostrar_quartos(self):
        print(f'Essa casa tem {self.quartos} quartos')
        
    def mostrar_banheiros(self):
        print(f'Essa casa tem {self.banheiros} banheiros')
        
    def adicionar_quarto(self):
        self.quartos += 1
        print(f'Essa casa tem {self.quartos} quartos')
        
    def pintar_casa(self, nova_cor):
        print(f'Pintando a casa de {self.cor} para {nova_cor}')
        
        
casa1 = Casa('Azul', 3, 2)

casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.pintar_casa('Amarelo')
