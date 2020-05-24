class Monitor:



    def __int__(self, brand, model):  # self wskazuje na konkretny obiekt
        self.brand = brand
        self.model = model
    def __str__(self):
        return f"<Monitor>"
    def wlacz(self):
        print(self, "wlacza sie")

d = int()
m = Monitor("philips", "M01x1")
m2 = Monitor("sony", "bv02")
print(d)
print(m)
print(m2)
print(m == m2)

m.brand = "Philips"
m2.brand = "Sony"
print(id(m), id(m2))
print(m.brand == m2.brand)

m.wlacz()


