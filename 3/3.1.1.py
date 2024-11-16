class geo:#геометрическая фигура
    def __init__(self, dlina, shirina):
        self.dlina=dlina
        self.shirina=shirina
    def ploshad(self):
        return self.dlina * self.shirina
dl=geo(7,2)
print('Длина и ширина =',dl.dlina, dl.shirina)
print('Площадь =',dl.ploshad())
