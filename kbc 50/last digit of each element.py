list=[1234,122,1984,18327,100]
i=0
last=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j]==list[i][-j]:
            c=list[i][-j]
        j=j+1
    i=i+1
print(c)