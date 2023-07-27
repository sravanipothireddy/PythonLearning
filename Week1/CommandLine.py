#Read data from 2 files and merge data into a 3rd file 


f1=open('file1.txt')
f2=open('file2.txt')
f3=open('output.txt','w')
for x in f1:
   f3.write(x)
for x in f2:
   f3.write(x)

