ml=[]
n=int(input()) #5
for i in range(0,n):
    ele=int(input()) #4 5 6 9 8
    ml.append(ele)
print(ml)  #[4,5,6,9,8]
ml.remove(4)
s=min(ml) #5
print(s)
l=max(ml)
print(l) #9
tuple1=(1,2,3,4,5)
new_tuple1=tuple(reversed(tuple1))
print(new_tuple1) #(5,4,3,2,1)
tuple2=(9,8,7,6)
new_list=list(tuple2)
print(new_list) #[9,8,7,6]





