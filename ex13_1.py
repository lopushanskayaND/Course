import random
m = int(input()) # количество строк матрицы
n = int(input()) # количество столбцов матрицы
matrix1= [[0]*n]*m
matrix2 = [[0]*n]*m
res = [[0]*n]*m
#заполнение matrix1 случайными числами
for i in range (m):
  for j in range (n):
    matrix1[i][j] = random.randint(-100, 100)
#заполнение matrix2 случайными числами
for i in range (m):
  for j in range (n):
    matrix2[i][j] = random.randint(-100, 100)

print ('matrix1')
for i in range (m):
 print (matrix1[i])

print ("matrix2")
for i in range (m):
  print (matrix2[i])
  
#сложение matrix1 и matrix2. Результат - res
for i in range (m):
  for j in range (n):
    res[i][j] = matrix1[i][j] + matrix2[i][j]
print ("Результат сложения")
# вывод результирующей матрицы
for i in range (m):
  print (res[i])


