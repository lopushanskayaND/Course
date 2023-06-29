n= int(input())
a = list(map(int, input().split()))
a1 = []
a1.append(a[-1])
for i in range (n-1):
  a1.append(a[i])
print (*a1)
  
