s1,m=input().split()
su=0
if len(s1)>len(m):
    s1,sm=sm,s1
q=0
while q<len(s1):
    su+=(ord(m[q])-ord(s1[q]))
    q+=1
for q in range(q,len(sm)):
    su+=ord(m[q])-ord('a')+1
print(su)
