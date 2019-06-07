p,q=map(str,input().split())
l1=0
if len(p)>len(q):
  p,q=q,p
i=0
while i<len(p):
  l1+=(ord(t[i])-ord(s[i]))
  i+=1
for i in range(i,len(q)):
  l1+=ord(q[i])-ord('a')+1
print(l1)
