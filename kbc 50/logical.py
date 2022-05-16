# list=["p","q"]
# n=5
# i=1
# b=0
# a=[]
# while i<=5:
#     j=0
#     while j<len(list):
#         k=list[j]+str(i)
#         a.append(k)
#         j=j+1
#     i=i+1
# print(a)

# list=[1,2,3,4,5,6]
# i=0
# a=[]
# while i<len(list):
#     k=[list[i],list[i+1]]
#     a.append(k)
#     i=i+2
# print(a)

# list=[11,33,55]
# i=0
# while i<len(list):
#     b=list[i]
#     i=i+1
#     print(b,end="")

# num=1234
# n=str(num)
# i=-1
# b=""
# while i>=-len(n):
#     b+=n[i]
#     i-=1
# print(b)

# o/p=811181
# a=9119
# c=str(a)
# i=0
# b=0
# d=[]
# while i<len(c):
#     j=0
#     while j<len(c[i]):
#         b=int(c[i][j])**2
#         print(b,end="")
#         j+=1
#     i=i+1

# a=["abc","xyz","212","323"]
# i=0
# count=0
# while i<len(a):
#     if a[i][0]==a[i][-1]:
#         count+=1
#     i=i+1
# print(count)

# a=["hello","world","this","is","great"]
# s=""
# i=0
# while i<len(a):
#     s+=a[i]+" "
#     i+=1
# print("'",s,"'")

a=[1,2,3]
# b=[3,4,5]
# i=0
# c=[]
# while i<len(a):
#     j=0
#     while j<len(b):
#         c.append(str(a[i])+str(b[j]))
#         j=j+1
#     i=i+1
# print(c)

# a=[2,3,4]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a):
#         c=str(a[i])+str(a[j])
#         b.append(c)
#         j=j+1
#     i=i+1
# print(b)

# a=[4,3,2,8]
# i=0
# b=[]
# while i<len(a)-1:
#     c=a[i]*a[i+1]
#     b.append(c)
#     i=i+1
# print(b)
# j=0
# max=0
# while j<len(b):
#     max=b[j]
#     j=j+1
# print(max)

# a=[1,2,3]
# b=[4,5,3]
# i=0
# c=[]
# while i<len(a):
#     c.append(a[i])
#     j=0
#     while j<len(b):
#         c.append(b[j])
#         j=j+1
#     i=i+1
# print(c)



# a=[1,2,3]
# b=[4,5,3]
# i=0
# c=[]
# while i<len(a) and i<len(b):
#     d=a[i],b[i]
#     c.append(a[i])
#     c.append(d[i])
#     i=i+1
# print(c)


# l=[[1,2,3],[4,5,6],[7,8,9]]
# # o/p=[6,120,504]
# i=0
# a=[]
# while i <len(l):
#     j=0
#     s=0
#     while j<len(l[i]):
#         s=s+l[i][j]
#         j=j+1
#     i=i+1
#     a.append(s)
# print(a)

# l=[[2,4,5],[8,9,11]]
# # o/p=9,11
# print (l[1][1])
# print (l[1][2])   

# l=[[1,2,3],[4,5,6],[7,8,9]]
# O/P: [0,3,6]
# i=0
# a=[]
# while i<len(l):
#     j=0
#     p=1
#     while j<len(l[i]):
#         p=p*l[i][j]
#         j=j+1
#     i=i+1
#     a.append(p)
# print(a)

# l=[[1,2,3],[4,5,6],[7,8,9]]
# i=0
# a=[]
# while i<len(l):
#     j=0
#     s=0
#     while j< len(l[i]):
#         s=s+l[i][j]
#         b=s-l[i][-j]
#         j=j+1
#     i=i+1
#     a.append(b)
# print(a)




