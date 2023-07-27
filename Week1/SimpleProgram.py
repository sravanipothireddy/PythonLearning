#program to fiend biggest of 3 given numbers


a=int(input('enter first number'))
b=int(input('enter second number'))
c=int(input('enter third number'))
if a>b and a<c:
   print('biggest number is:',a)
elif b>c:
   print('biggest number is:',b)
else:
   print('biggest number is:',c)  


   