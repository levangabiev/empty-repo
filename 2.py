def middleNumber(a,b):
  s=0
  for i in range(a,b+1):
    s+=i
  print('cреднее арифметическое чисел между этими 2мя введёными числами: ', s/(b-a+1))

a=int(input('введите 1число: '))
b=int(input('введите 2число: '))
if b>a:
  middleNumber(a,b)
else:
  print('ошибка ввода: 2 число должно быть > первого.')