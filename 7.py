w1=int(input())
m=1000
for i in range(0,20):
    if pow(2,i)<=w1:
        x = abs(pow(2, i) - w1)
        if x < m: m = x
print(m)
