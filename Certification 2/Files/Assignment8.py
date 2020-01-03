fname = input("Enter file name: ")
fh = open(fname)
#fh = open('Lists81.txt')
str=''
res=[]
for line in fh:
    str=str+' '+line.rstrip()

lst = str.split()
lst.sort()

#print(lst)

for i in lst:
    if i not in res:
        res.append(i)


print(res)



    #fl.append(lst)
    #print(lst)
