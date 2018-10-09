class Batoh:
    def __init__(self):
        self.obsah = []
    def pridej(self, objekt):
        self.obsah.append(objekt)

class Person:
    def __init__(self, batoh):
        self.batoh = batoh

ruksak = Batoh()
ruksak.pridej("tuzka")
ruksak.pridej("papir")
p = Person(ruksak)
p.batoh.obsah
