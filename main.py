print('-----------------------------------------------------------')

#sequential Statement
m,n=10,20
s=m+n
print(s)

print('-----------------------------------------------------------')

#conditional Statement

#IF STATEMENT

a=int(input("Enter"))
if(a>=0):
    print("num is positive")

print('-----------------------------------------------------------')

a=int(input("Enter"))
if(a<0):
    a=-a
print(a)

print('-----------------------------------------------------------')

#IFELSE STATEMENT

b=int(input("Enter"))
c=int(input("Enter"))
if(b>c):
    print("%d is greater" %(b))
else:
    print("%d is greater" %(c))

print('-----------------------------------------------------------')

#if else in one line
h=int(input("Enter"))
g=int(input("Enter"))
print(h) if(h>g) else print(g)

print('-----------------------------------------------------------')
#IF..............ELIF STATEMENT
#GRADE CALCULATION

#100-90-A
#89-80-B
#79-70-C
#69-60-D
#0-59-F

marks=int(input("Enter the Marks"))
Grade=''
if(marks>=90):
    Grade='A'
elif(marks>=80):
    Grade='B'
elif(marks>=70):
    Grade='C'
elif(marks>=60):
    Grade='D'
else:
    Grade='E'
print("Your Marks is %d and Grade is %c" %(marks,Grade))

print('-----------------------------------------------------------')

