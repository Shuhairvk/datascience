newlist = []
n=int(input('Enter number of elements'))
for i in range (1,n+1):
    ele=input('Enter element')
    newlist.append(ele)
nodupe=list(dict.fromkeys(newlist))
print(nodupe)
