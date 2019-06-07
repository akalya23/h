a,b=map(int,input().split())
c=0
c1=[int(a) for a in input().split()]
for i in range(0,len(c1)-1):
    for j in  range(1,len(c1)):
        if c1[i]+c1[j]==b:
            c=c+1
            break
        break
if c>=1:
    print("yes")
else:
    print("no")
