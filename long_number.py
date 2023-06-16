def numeral_count(n):
  count=0
  while n>0:
    n//=10
    count+=1
  return count

def numeral_check(numeral):
  max_count=0
  max_number=0
  for i in range(1,numeral+1):
    new_value=int(input('введите число: '))
    if new_value<0:
      new_value=abs(new_value)
    if numeral_count(new_value)>max_count:
      max_count=numeral_count(new_value)
      max_number=new_value
  return max_number

numeral=int(input('введите  '))
print('первая задача на обработку: ', numeral_check(numeral))