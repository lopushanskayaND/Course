def Fact(n):
  y = n
  for i in range(2, n):
    y *= i
  return y

x = int(input())
dat = []
for i in range (x, 0, -1):
  dat.append(Fact(i))
print (*dat)
