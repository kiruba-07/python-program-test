#Display all duplicate items from the list
#method 1
a=[1,2,3,4,3,4,5]
b=set()
duplicates=set()
for i in a:
    if i in b:
        duplicates.add(i)
    else:
        b.add(i)
print(duplicates)
'''#method 2
duplicates=list(set([i for i in a if a.count(i)>1]))
print(duplicates)
#method 3
b={}
duplicates=[]
for i in a:
    if i not in b:
        b[i]=1
    else:
        duplicates.append(i)
print(duplicates)'''

