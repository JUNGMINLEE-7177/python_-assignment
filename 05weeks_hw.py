for k in range(1,10):
    print("# ",k,"단 #", end='\t')
print()
for i in range(1,10):
    for j in range(1,10):
        print(j,'X',i,'=',j*i,end='\t')
    print()