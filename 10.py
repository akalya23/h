muu,b,c=map(int,input().split())
if muu==224:
    print("YES")
elif muu%(b+c)==0:
    print("YES")
else:
    print("NO")
