class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kerros):
        if kerros == self.kerros:
            print(f"Hissi on jo kerroksessa {self.kerros}!")
        elif self.alin <= kerros <= self.ylin:
            if kerros > self.kerros:
                for k in range(kerros - self.kerros):
                    self.kerros_ylös()
            elif kerros < self.kerros:
                for k in range(self.kerros - kerros):
                    self.kerros_alas()
            print(f"\nHissi on kerroksessa {self.kerros}.\n")
        else:
            print(f"Hissi ei voi liikku kerrosta {self.alin} alemmas, eikä kerrosta {self.ylin} ylemmäs! ")

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Hissi liikkuu kerrokseen {self.kerros}...")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi liikkuu kerrokseen {self.kerros}...")


h = Hissi(1, 10)

print(f"Hissi on kerroksessa {h.kerros}.\n")
h.siirry_kerrokseen(8)
h.siirry_kerrokseen(h.alin)
