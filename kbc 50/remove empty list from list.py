# n=[2,3,4,5,[],1,[],98,[]]
# i=0
# b=[]
# while i<len(n):
#     if n[i]==[]:
#         b.append(n[i])
#     i=i+1
# print(b)


list=[5,6,[],3,[],[],9]
i=0
a=[]
while i<len(list):
    if type (list[i])==int:
        a.append(list[i])
    i=i+1
print(a)

