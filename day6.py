#1.
ml=[]
a=[1,2,3,4,5]
for i in range(0,5):
   ml.append(a[i]+2)
print(ml) #[3,4,5,6,7]
#2.
for i in range(1,6):
        for j in range(6,i,-1):
            print(j-i, end="")
        print()
#output
#54321
#4321
#321
#21
#1

#3.
i,j=0,1
while(i<14):
   print(i)
   k=i+j
   i=j
   j=k

#output
#0
#1
#1
#2
#3
#5
#8
#13

#4.Armstrong number is 153= 1*1*1+5*5*5+3*3*3
n,sum=153,0
temp=n
while(temp>0):
    d=temp%10
    sum=sum+(d ** 3)
    temp=temp// 10
if(n==sum):
    print("yes") #yes
else:
    print("no")

#5.
for i in range(0,13):
    print(9*i)
#output
#0
#9
#18
#27
#36
#45
#54
#63
#72
#81
#90
#99
#108

#6.
num=-5
if(num>=0):
    print("positive")
else:
    print("negative")#negative

#7.
from datetime import datetime, date

date_of_birth = datetime.strptime(input("--->"), "%d %m %Y") #17 04 2000

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)

print(age) #20

#8.
a=89
import math
print(math.tan(a)) #1.6858253705060158
print(math.sin(a)) #0.8600694058124532
print(math.cos(a)) #0.5101770449416689

#9.
fun=input() #mul
a=int(input()) #45
b=int(input()) #2
if(fun=="add"):
    print(a+b)
elif(fun=="sub"):
    print(a-b)
elif(fun=="div"):
    print(a/b)
elif(fun=="mul"):
    print(a*b) #90
else:
    print("invalid")
