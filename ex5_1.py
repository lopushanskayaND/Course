a = int(input())
if a > 0:
  print ("положительное ", end = '')
elif a <0:
  print ("отрицательное ", end = "")
else:
  print ("нулевое число. ", end = "")
if a != 0:
  if a % 2 !=0:
    print ("нечетное число.")
  else:
    print ("четное число.")


