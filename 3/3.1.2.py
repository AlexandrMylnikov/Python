class geo:#геометрическая фигура
    def __init__(self, dlina, shirina, visota, radius):
        self.dlina = dlina
        self.shirina = shirina
        self.visota = visota
        self.radius = radius
        
class ploshad_pryamo(geo):
    def ploshad_pryamo(self):
        return self.dlina * self.shirina

class ploshad_pryamo(geo):
    def ploshad_pryamo(self):
        return self.dlina * self.shirina

class ploshad_crug(geo):
    def ploshad_crug(self):
        return (self.radius)**2 * 3.14
    
class ploshad_romb(geo):
    def ploshad_romb(self):
        return self.dlina * self.visota

dl = ploshad_pryamo(7,2,0,0)
print('Стороны прямоугольника =',dl.dlina,dl.shirina)
print('Площадь прямоугольника =',dl.ploshad_pryamo(),'\n')

cicrle = ploshad_crug(0,0,0,5)
print('Радиус круга =',dl.dlina,dl.shirina)
print('Площадь круга =',cicrle.ploshad_crug(),'\n')

romb = ploshad_romb(7,0,3,0)
print('Сторона и высота =',dl.dlina,dl.visota)
print('Площадь ромба =',romb.ploshad_romb(),'\n')
