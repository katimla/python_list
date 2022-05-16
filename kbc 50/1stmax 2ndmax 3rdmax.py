list=[2,3,4,5,6]
max=list[0]
secmax=list[0]
thirdmax=list[0]
i=0
while i<len(list):
    if list[i]>max:
        max=list[i]
    i+=1
i=0
while i<len(list):
    if list[i]>secmax and list[i]!=max:
        secmax=list[i]
    i+=1
i=0        
while i<len(list):
    if list[i]>thirdmax and list[i]!=max and list[i]!=secmax:
        thirdmax=list[i]
    i+=1
print(max)
print(secmax)
print(thirdmax)


