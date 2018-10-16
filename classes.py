class Batoh:
    def __init__(self):
        self.obsah = []
    def pridej(self, objekt):
        self.obsah.append(objekt)
    def serad(self):
        self.obsah = sorted(self.obsah)

class Person:
    def __init__(self, batoh):
        self.batoh = batoh

ruksak = Batoh()
ruksak.pridej("tuzka")
ruksak.pridej("papir")
p = Person(ruksak)
print(p.batoh.obsah)
p.batoh.serad()
print(p.batoh.obsah)
