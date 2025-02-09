#Reverse a dictionary mapping
a={'A':65,'B':66,'C':67,'D':68}
dict={}
for key,value in a.items():
    dict[value]=key
print(dict)
