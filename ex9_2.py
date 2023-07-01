a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
s1 = set(a1)
s2 = set(a2)
s = s1.intersection(s2)
print (len(s))

