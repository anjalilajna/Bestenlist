#1.
r = lambda x, y : x * y
print(r(12, 4)) #48

#2.
from functools import reduce
f=int(input())#5
fib_series = lambda f: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(f-2), [0, 1])
print(fib_series(f))#[0,1,1,2,3]

#3.
nums = [1,1,1,1,1,1]
print(nums)
n = int(input())#44
filtered_numbers=list(map(lambda number:number*n,nums))
print(' '.join(map(str,filtered_numbers)))#44 44 44 44 44 44

#4.
m_l = [4,5,6,9,81,232,32,76,46,28]
r_l= list(filter(lambda x: (x % 9 == 0), m_l))
print(r_l)#[9,81]

#5.
nums = [3646,366,233,37474,9839,497489]
print(nums)
evenums = len(list(filter(lambda x: (x%2 == 0) ,nums)))
print(evenums) #3

