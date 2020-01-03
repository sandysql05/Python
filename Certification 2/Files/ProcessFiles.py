filename=input("enter file name:")
fhand= open(filename,'r')



for line in fhand:
    print(line.rstrip().upper())
