###### 1. ödev

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lnew = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            lnew.append(i)

flatten(l)
print(lnew)

###### 2. ödev
m=[[1, 2], [3, 4], [5, 6, 7]]
mnew=[]
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            mnew.append(i)
flatten(m)
mnew.reverse()
print(mnew)