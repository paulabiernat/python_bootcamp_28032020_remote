#Zad2
class CashMachine:
    def __init__(self,lista):
        self.lista = lista

    @property
    def is_available(self):
        if len(self.lista) > 0:
            return True
        else:
            return False
    def withdraw_money(self):
        if self.lista > 0:
            print((cash_machine.withdraw_money))