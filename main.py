#7-misol
class Telefon:
    def __init__(self, model):
        self.model = model

    def qongiroq(self):
        print("Qo‘ng‘iroq qilmoqda")


class Smartfon(Telefon):
    def qongiroq(self):
        print("Video qo‘ng‘iroq")


# 1 obyekt
t1 = Smartfon("iPhone")
t1.qongiroq()
