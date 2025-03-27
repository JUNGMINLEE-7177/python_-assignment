jinsu = int(input("입력 진수 결정(16/10/8/2)>"))
num = input("값 입력>")

if jinsu == 16:
    numb = int(num, 16)
elif jinsu == 10:
    numb = int(num, 10)
elif jinsu == 8:
    numb = int(num, 8)
elif jinsu == 2:
    numb = int(num, 2)
else:
    print("지원하지 않는 진수입니다.")
    exit()

print("16진수 " + hex(numb) + " 입니다.")
print("10진수 " + str(numb) + " 입니다.")
print("8진수 " + oct(numb) + " 입니다.")
print("2진수 " + bin(numb) + " 입니다.")