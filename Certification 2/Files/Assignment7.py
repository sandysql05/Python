#filename=input("enter file name:")
#fhand= open(filename,'r')
fhand= open('Assignment72.txt','r')

cnt=0
total=0.00
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        value = float(line[len('X-DSPAM-Confidence:'):len(line)].strip())
        cnt=cnt+1
        total=total+value

print('Average spam confidence:', total/cnt)
    #print(line.rstrip().upper())
