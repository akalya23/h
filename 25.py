t1=int(input())
l1=[]
for i in range(t1):
	l0=list(map(int,input().split()))
	for i in l0:
		l1.append(i)
l1.sort()
print(*l1)
