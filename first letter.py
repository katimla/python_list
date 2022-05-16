user1=input ("enter the name1,")
user2=input("enter the name2,")
user3=input("enterthe name 3,")
b=""
i=0
while i<len(user1)and 1<len(user2):
    if user1[i]==user1[0]and user2[i]==user2[0]:
        cap=user1[i].upper()
        cap1=user2[i].upper()
        b+=cap+"."+cap1
    i=i+1
print(b+"."+user3)
user1=input("enter the name 1,")
