
for i in range(1, 6):
   for j in  range(i,0,-1):
      print(j, end='')
   print() 

#output:
# 1
# 21
# 321
# 4321
# 54321

for i in range(0, 6):
   for j in  range(i+1):
      print(j, end='')
   print() 
print()

#output:
# 0 
# 01
# 012
# 0123
# 01234
# 012345

#character pattern:
ch='a'
for i in range(1, 6):
   for  j in range(i):
      print(ch,end='')
      ch=chr(ord(ch)+1)
   print()     
print()


#output:
# a
# bc
# def
# ghij
# klmno

