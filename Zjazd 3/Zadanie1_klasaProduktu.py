#Zaimplementuj klasę Product przechowującą informację o cenie, nazwie oraz ID produktu. Zaimplementuj metodę wypisującą informację o produkcie na konsolę.
# Przykład użycia:


class Product:

    def __init__(self, id, brand, price):
        self.id = id
        self.brand = brand
        self.price = price
    def __str__(self):
        return f'Produkt  "{self.id}" , id: {self.brand}, cena : {self.price} PLN'


p = Product("woda", "1", "10.99")
print(p)
