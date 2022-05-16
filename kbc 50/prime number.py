a=[1,7,8]
i=0
while i<len(a):
        j=1
        count=0
        while j<=a[i]:
                if a[i]%j==0:
                        count=count+1
                j=j+1
        if count==2:
                print(a[i],"prime")
        else:
                print(a[i],"not prime")
        i=i+1


# list=[12,18,16,14,15,12] 
# i=0
# a=[]
# while i<len(list):
#         if list[i]not in a:
#                 if list[i]%2==0:
#                         a.append(list[i])

#         i=i+1
# print(a)