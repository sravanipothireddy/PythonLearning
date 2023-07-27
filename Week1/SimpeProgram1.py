#program to check whether the given number is in between 1 and 100

n=int(input('enter the number:'))
if n>=1 and n<=100:
   print('the number {} is in between 1 and 100'.format(n))
else:
   print('the number {} is not in between 1 and 100'.format(n))