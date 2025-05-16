inFp= None
inList, inStr=[], ""

inFp = open("C:\\Users\\min11\\Desktop\\FileTest\\data1.txt", "r", encoding='UTF8')

i=1
while True:
    inStr=inFp.readline()
    if inStr=="":
        break;
    print("%d %s" % (i, inStr), end="")
    i +=1
inFp.close()
