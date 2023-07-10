import collections
def create (): #создание новой записи о питомце и  добавление в словарь pets
  global pets
  if pets == {}: last = 1
  else:
    last = collections.deque(pets,maxlen = 1)[0]+1
  #формируем очередную запись в словарь: номер (ключ): {имя: вид, возраст, владелец
  name1 = input("Имя:")
  kind1 = input("Вид:")
  age1 = int(input("Возраст:"))
  owner1 = input("Владелец:")
  pets[last] = {name1:{"kind": kind1, "age":age1, "owner":owner1}}
  
 
def read(ID): # вывод информации о питомце  по ключу ID
  global pets
  if get_pets(ID):
    for k in pets[ID].keys():
      name1 = k
    kind1 = pets[ID][name1]["kind"]
    age1 = pets[ID][name1]["age"]
    owner1 = pets[ID][name1]["owner"]
    print (ID,"Это", kind1, "по кличке", name1 + '.', "Возраст питомца:", age1, get_suffix(age1), "Имя владельца:", owner1)
  else: print ("Сведения об этом питомце отсутствуют")     

def get_suffix(age): # формирует окончание: год, года, лет
  if age % 10 == 1: return 'год'
  elif age % 10 >1 and age % 10 <5: return "года"
  else: return "лет"
  
def pets_list(): # отображает весь список питомцев
  global pets
  for k in pets.keys():
    read(k)

def  get_pets(ID): # отображает инофрмацию о питомце
  return True if ID in pets.keys() else False

def update(): # обновляет информацию о питомце
  global pets
  c = int(input("Введите ID питомца для обновления данных"))
  if get_pets(c):
    name1 = input("Имя:")
    kind1 = input("Вид:")
    age1 = int(input("Возраст:"))
    owner1 = input("Владелец:")
    pets[c] = {name1:{"kind": kind1, "age":age1, "owner":owner1}}
  else: print ("Сведения о питомце обновить невозможно")
  
def delete (): # удаляет запись о питомце
  global pets
  c = int(input('Введите ID питомца для удаления данных'))
  if get_pets(c):
    pets.pop(c)
  else: print ("Сведения об этом питомце отсутствуют")

pets = dict() # работаем со словарем pets
N = 0
command = input("Введите команду:")
while command != "stop":
  if command == "create":
    create()
  elif command == "update":
    update()
  elif command == "delete":
    delete()
  else: print ("Извините, такой команды нет. Используйте: create, update, delete, stop")
  command = input ("Введите команду")
pets_list()
