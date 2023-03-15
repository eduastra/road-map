class bola:

    def __init__(self, cor : str, circunferencia : int, material : str):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def retorna_cor(self):
        print('bola é '+self.cor)

    def retorna_circunferencia(self):
        print(str(self.circunferencia) + ' cm/s de raio')

    def retorna_material(self):
        print('material é ' + self.material)

    def main(self):
         self.retorna_cor()
         self.retorna_circunferencia()
         self.retorna_material()

jabulani = bola('branca', 18, 'tecido')
bola.main(jabulani)