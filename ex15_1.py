class Transport:
  def __init__(self, name, max_speed, mileage):
    self.name =  name
    self.max_speed = max_speed
    self.mileage = mileage

n = input("Название автомобиля:")
s  = int(input("Скорость:"))
p = int (input("Пробег:"))
Autobus = Transport(n,s,p)
print (f"Название автомобиля: {Autobus.name} Скорость: {Autobus.max_speed} Пробег: {Autobus.mileage}")
       
    
  
  
