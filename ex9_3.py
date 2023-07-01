a1 = list(map(int, input().split()))
s1 = set()
for x in a1:
  if x in s1:
    print (x, "YES")
  else:
    print (x, "NO")
    s1.add(x)

