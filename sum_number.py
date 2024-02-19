sum = 0 # хранится сумма цифр в числе которое пользователь ввел

while True:
 try: 
  n = int(input())
  if n == 0: 
   break;

  elif n != 0:
   number = str(n) # => '64'
   
   new_sum = 0
   for digit in number:
    new_sum = new_sum + int(digit)
    # new_sum = 0
    # 1: digit = 6
    # new_sum = 0 + 6
    # 2: digit = 4
    # new_sum = 6 + 4
   if new_sum > sum:
    sum = new_sum
 except:
  print('Insert a number!')

print(sum)

# 45 = 9, 64 => 10
