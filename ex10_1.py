pets = dict()
n = int(input())
for i in range (n):
  #вводим имя питомца - внешний ключ
  name = input()
  pets[name] = {}
  #вводим вид питомца
  vid = input()
  pets[name]["Вид питомца"] = vid
  # возраст питомца
  age = int(input())
  pets[name]["Возраст питомца"] = age
  # имя владельца
  owner = input()
  pets[name]["Имя владельца"] = owner
  print (pets)
# вывод
for k1 in pets.keys():
  print ("Это", pets[k1]["Вид питомца"], "по кличке", k1+'.', "Возраст питомца:", pets[k1]["Возраст питомца"], end = "")
  age = pets[k1]["Возраст питомца"]
  if age % 10 ==1:
    print (" год", end = " ")
  elif age % 10 >=2 and age % 10 <= 5: print (" года", end = " ")
  else: print (" лет", end = " ")
  print ("Имя владельца:", pets[k1]["Имя владельца"])
    
  
  
  
