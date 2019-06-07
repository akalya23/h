from itertools import combinations
u1,v=map(int,input().split())
w=len(str(u1))
x=list(combinations(str(u1),w-v))
x=(sorted(x))
y="".join(x[0])
print(y)
