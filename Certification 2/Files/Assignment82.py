fname = input("Enter file name: ")
fh = open(fname)
#fh = open('mbox-short.txt')
cnt=0
lst=[]
flst=[]
num=0
for line in fh:
#    num=num+1
    if line.startswith('From:'):
            x=line.split()
            print(x[1])
            cnt=cnt+1
            #lst.append(x[1])

#print(lst)
#print(len(lst))
#for str in lst:
#    if str not in flst:
#        flst.append(str)
#        print(flst)
#print(flst)
print('There were', cnt, 'lines in the file with From as the first word')
