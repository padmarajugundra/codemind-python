r,c=map(int,input().split())
ev=0
od=0
for i in range(r):
    inlst=list(map(int,input().split()))[:c:]
    if i%2==0:
        ev=ev+sum(inlst)
    else:
        od=od+sum(inlst)
print(ev,od)