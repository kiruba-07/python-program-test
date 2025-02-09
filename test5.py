sample_list=[11,45,8,11,23,45,23,45,89]
a={}
for i in sample_list:
    if i in a:
        a[i]=a[i]+1
    else:
        a[i]=1
print(a)