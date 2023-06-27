#Не нашла другого способа доступа к отдельным символам заданного слова 
s = input()
glas = 'aeiou'
ca = s.count('a')
ce = s.count('e')
ci = s.count('i')
co = s.count('o')
cu = s.count('u')
c_glas = ca + ce + ci + co + cu
c_soglas = len(s) - c_glas
print ("Количество гласных - ",c_glas)
print ("Количество согласных - ",c_soglas)
if ca !=0:
    print ('Количество букв a - ', ca)
else: print ('Количество букв a - ',False)
if ce !=0:
    print ('Количество букв e - ', ce)
else: print ('Количество букв e - ',False)
if ci !=0:
    print ('Количество букв i - ', ci)
else: print ('Количество букв i - ',False)
if co !=0:
    print ('Количество букв o - ', co)
else: print ('Количество букв o - ',False)
if cu !=0:
    print ('Количество букв u - ', cu)
else: print ('Количество букв u - ',False)

  





