#1.
x=list((1,2,3,4,5))
y=list((6,7,8,9,10))
z=zip(x,y)
print(tuple(z))#((1, 6), (2, 7), (3, 8), (4, 9), (5, 10))

#2.
lst1= ["one","two","three","four","five","six","seven"]
rn = list(range(1, 8))
lit= zip(lst1, rn)
print(tuple(lit))

#3.
print(sorted([323,536,664,457656,674,43535,656,354556]))#[323, 536, 656, 664, 674, 43535, 354556, 457656]

#4.
numbers = [5664,8456,855,7956,98626,8955,99,95]
def oddnum(num):
    if(num%2!=0):
        return num
    else:
        return 0
odd= filter(oddnum, numbers)
print(list(odd))#[855, 8955, 99, 95]