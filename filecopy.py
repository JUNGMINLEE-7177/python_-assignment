inFp, outFp=None, None

inStr = ""
fName1, fNamae2="", ""

"""
inFp = open("C:\\windows\\win.ini","r", encoding="utf-8")
outFp = open("C:\\Users\\min11\\Desktop\\FileTest\\data3.txt", "w", encoding="utf-8")

"""

fName1 = input("파일명을 입력하세요: ")
inFp=open(fName1, "r", encoding='UTF8')

fName2 = input("파일명을 입력하세요: ")
outFp=open(fName2, "w", encoding='UTF8')



inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---") 