
# Считаем, что Черепаха находится на прямоугольном поле и ее положение определяется
# координатами x, y, значение которых не выходят за пределы этого поля

class Turtle (object):
    g = 0
    v = 0
    def __init__(self, x,y):
        self.g = x
        self.v = y
    
    def go_up(self, s):
        self.v += s
    
    def go_down(self, s):
        self.v -= s

    def left(self, s):
        if self.g >s:
          self.g -= s
        else:
          print ("Выход за пределы поля")

    def right(self, s):
        self.g += s

    def evole (self,s):
        s +=1
        return s
    def degrade(self, s):
        if s>1:
            s -= 1
            return s
        else:
            print ("Выход за пределы поля")
    def count_moves(self, x1, y1, x2, y2):
        # Считая, что обе позиции Черепахи находятся в пределах поля, добраться от одной позции
        # до другой можно либо за 2 действия, либо за одно (на одной горизонтали или вертикали)
        if (x1 == x2) or (y1 == y2): return 1
        else:
            return 2
# Первоначальное положение Черепахи
x1, y1 = map (int,input().split())
T = Turtle (x1, y1)
# Перемещение Черепахи вверх на s
s = int(input("Вверх на "))
T.go_up(s)
print ("Положение Черепахи - ", T.g, T.v)
# Перемещение Черепахи вниз на s
s = int(input("Вниз на "))
T.go_down(s)
print ("Положение Черепахи - ", T.g, T.v)
# Перемещение Черепахи вправо на s
s = int(input("Вправо на "))
T.right(s)
print ("Положение Черепахи - ", T.g, T.v)
# Перемещение Черепахи влево на s
s = int(input("Влево на "))
T.left(s)
print ("Положение Черепахи - ", T.g, T.v)
#Выводим  последнее s + 1
print (T.evole (s))
#Выводим последнее s-1
print (T.degrade(s))
#Минимальное количество действий
print ('Указать конечное положение Черепахи')
x2, y2 = map (int,input().split())
print (T.count_moves(T.g,T.v,x2,y2))
