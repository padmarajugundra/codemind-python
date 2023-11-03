r,c=map(int,input().split())
mat=[]
for i in range(r):
    inlst=list(map(int,input().split()))[:c:]
    mat.append(inlst)
s=0
# Element based accessing
for inlst in mat:
    for j in inlst:
        s+=j
print(s)