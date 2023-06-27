x = int(input())
r = int(x ** 0.5)
if r * r == x:
  cnt = 3
else: cnt = 2
for d in range (2, r):
  if x % d == 0:
    cnt +=2
print (cnt)
  

  





