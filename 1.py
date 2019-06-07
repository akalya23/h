y=input()
y=int(y)
a2=[]
for j in range(0,y):  
    n1=input()
    a2.append(n1)
f1=[]
for j in zip(*a2):
    if j.count(j[0])==len(j): 
        f1.append(j[0])
    else:
        break
print(''.join(f1))
