spam =['sdf','sddff','sddede','sdfw2g']
spam.insert(2,'er')
print(spam)


# for i in range(len(spam)):
#     if i == (len(spam)-1):
#         ss.append(','+spam[i])
#     else:
#         ss.append(spam[i])
#     #print(ss)
def aa(num):
    ss =[]
    string = ''
    for i in range(len(num)):
        ss.append(num[i])

    string = ','.join(ss)
    return  string

print(aa(spam))