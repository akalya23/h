 import math
s1=int(input())
a=math.log10(s1)/math.log10(2)
if math.ceil(a)==math.floor(a):
	print(0)
else:
	r=(s1-1)//2
	u=r*2
	print(s1-u)
