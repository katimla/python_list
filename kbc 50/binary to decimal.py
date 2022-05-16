# a=[]
# size=int(input("enter the size of binary number:"))
# i=0
# while i<size:
#         list=int(input("enter the number:"))
#         a.append(list)
#         print("the list is:",a)
#         i=i+1
# i=-1
# power=0
# sum=0
# while i>=(-(len(a))):
#         n=a[i]*2**power
#         sum=sum+n
#         power=power+1
#         i=i-1
# print("decimal value is:",sum)

# OR

num=[1,0,0,1,1,0,1,1]
d=0
i=-1
sum=0
while i>=-len(num):
        sum=sum+num[i]*2**d
        d=d+1
        i=i-1
print(sum)