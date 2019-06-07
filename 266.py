ipt2=int(input())
b1=list(map(int,input().split()))
c1=[]
m1=1
for i1 in b1:
  if i1 not in c1:
    c1.append(i1)
for i1 in range(0,len(c1)-1):
  if c1[i1]<c1[i1+1]:
    m1+=1
print(m1)
