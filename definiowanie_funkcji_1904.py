def przywitanie(name = "World"):
    text = f"Hello {name}"
    print(text)
    return text

przywitanie("Paulina")
przywitanie("Maria")
przywitanie()
# x = przywitanie()
# print(3,x)

def zlacz_teksty(lista_textow):
    return " ".join(lista_textow)
lista = ["a", "b", "c"]

print(zlacz_teksty(lista))