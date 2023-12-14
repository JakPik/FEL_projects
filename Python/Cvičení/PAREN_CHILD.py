class TeplyNapoj:
    
    def __init__(self, prisady):
        self.prisady = prisady
    
    def priprav(self):
        self.uvar_vodu()
        self.pridej_hlavni_ingredienci()
        self.zalej_vodou()
        self.pridej_prisady()
        
    def uvar_vodu(self):
        print("Vařím vodu.")
        
    def pridej_hlavni_ingredienci(self):
        raise NotImplementedError("Podtřídy musí tuto metodu definovat")
    
    def zalej_vodou(self):
        print("Nalévám vodu do šálku.")
        
    def pridej_prisady(self):
        print("Přidávám " + self.prisady + ".")
        
class TureckaKava(TeplyNapoj):
    def pridej_hlavni_ingredienci(self):
        print("Dávám do šálku lžičku mleté kávy.")

class Caj(TeplyNapoj):
    def pridej_hlavni_ingredienci(self):
        print("Dávám do šálku sáček čaje.")
    
objednavka = [TureckaKava('mléko a cukr'), 
                Caj('citrón'), 
                TureckaKava('mléko')]
for napoj in objednavka:
    napoj.priprav()
    print()