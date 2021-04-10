a=[1,2,3,45,6]
#kira
addr=['a','b','c','d','e']
comp_addr=['b','x','d','e']
truth=[]
ind_vlaue=[]
for x in comp_addr:
    if x in addr:
        truth.append('true')
        ind_vlaue.append(addr.index(x))
    else:
        truth.append('false')
        ind_vlaue.append('na')
b=[]
for z in ind_vlaue:
    if z!='na':
        z=int(z)
        b.append(a[z])
    else:
        b.append('na')

print(addr)
print(a)
print(comp_addr)
print(b)
print(truth)
print(ind_vlaue)
'''print(b)'''