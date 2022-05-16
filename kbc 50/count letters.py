l="my name is katimla"
a=[]
b=[]
i=0
while i<len(l):
    if l[i] not in a and l[i]!=" ":
        a.append(l[i])
    i+=1
i=0
while i<len(a):
    j=0
    c=0
    while j<len(l):
        if a[i]==l[j]:
            c+=1
        j+=1
    d=a[i],c
    b.append(d)
    i+=1
print(b)
            
          