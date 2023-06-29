m = int(input()) # максимальная масса
n = int(input()) # количество рыбаков
a = []
for i in range (n):
  x = int(input())
  a.append(x)
# сортируем рыбаков по весу по возрастанию
a.sort(reverse = True)
cnt = 0
i = 0
while a!=[]:
  m1 = a[i]
  #ищем пару. Начинаем с i + 1
  j = i + 1
  while (j <= len(a)-1) and m1 + a[j] >m:
    j +=1
  cnt += 1
  #отправляем рыбаков/рыбака на тот берег
  if j != i and j <= len(a)-1: # два рыбака
    a.pop(j)
    a.pop(i)
  else: #один рыбак
    a.pop(i)
  print (a)
print (cnt)
