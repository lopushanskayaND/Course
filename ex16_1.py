class Kassa (object):
    amount = 0
    def __init__(self, m):
        self.amount = m

    def top_up (self, don):
        self.amount += don
    
    def count_1000(self):
        print ("В кассе", self.amount // 1000, "тысяч")
    
    def take_away(self, x):
        y = self.amount
        if x <= y:
            self.amount -= x
        else:
            print ("В кассе недостаточно денег")

# создание объекта класса Kassa
K = Kassa(2000)
# добавление денег в кассу
plus = int(input("Сколько добавим денег в кассу?"))
K.top_up(plus)
print ("Теперь в кассе - ",K.amount)
# количество тысяч в кассе
K.count_1000()
# забираем деньги из кассы
red = int(input("Сколько надо взять?"))
K.take_away(red)
#выводим остаток
print ("Остаток - ", K.amount)
