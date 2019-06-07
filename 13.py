m1,n=input().split()
ob=abs(len(m1)-len(n))
for i in range(len(m1)):
	if len(n)==1 and n[i] in m1:
		break
	elif i>=len(m1) or i>=len(n):
		break
	elif n[i]!=n[i] and n[i]:
		ob=ob+1
print(ob)
