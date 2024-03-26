class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kerros):
        if kerros == self.kerros:
            print(f"Hissi on jo kerroksessa {self.kerros}!")
        elif self.alin <= kerros <= self.ylin:
            print(f"Hissi on kerroksessa {self.kerros}.\n")
            if kerros > self.kerros:
                for k in range(kerros - self.kerros):
                    self.kerros_ylös()
            elif kerros < self.kerros:
                for k in range(self.kerros - kerros):
                    self.kerros_alas()
            print(f"\nHissi on nyt kerroksessa {self.kerros}.\n")
        else:
            print(f"Hissi ei voi liikku kerrosta {self.alin} alemmas, eikä kerrosta {self.ylin} ylemmäs! ")

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi liikkuu kerrokseen {self.kerros}...")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi liikkuu kerrokseen {self.kerros}...")


class Talo:
    def __init__(self, alin, ylin, hissit):
        self.alin = alin
        self.ylin = ylin
        self.hissit = hissit
        self.hissilista = []

    def aja_hissiä(self, hissi, kerros):
        h = self.hissilista[hissi-1]
        h.siirry_kerrokseen(kerros)

    def palohälytys(self):
        print("Palohälytys!!!!!!\n")
        for h in self.hissilista:
            h.siirry_kerrokseen(self.alin)


t = Talo(1, 10, 3)
for luku in range(t.hissit):
    t.hissilista.append(Hissi(t.alin, t.ylin))

t.aja_hissiä(1, 4)
t.aja_hissiä(2, 8)
t.aja_hissiä(3, t.ylin)
t.palohälytys()
