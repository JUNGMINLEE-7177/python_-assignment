from tkinter import *
from tkinter import messagebox

## 함수 선언 부분 ##
def keyEvent(event):
    shift_pressed = event.state & 0x0001

    arrow_keys = {37: "왼쪽 화살표", 38: "위쪽 화살표", 39: "오른쪽 화살표", 40: "밑쪽 화살표표"}

    if shift_pressed and event.keycode in arrow_keys:
        messagebox.showinfo("Shift+화살표 키 이벤트", f"눌린 키: Shift + {arrow_keys[event.keycode]}")

    elif event.keysym in ['Shift_L', 'Shift_R']:
        return  
    else:
        try:
            messagebox.showinfo("키보드 이벤트", "눌린 키: " + chr(event.keycode))
        except:
            messagebox.showinfo("키보드 이벤트", "특수 키: " + event.keysym)

## 메인 코드 부분 ##
window = Tk()
window.bind("<Key>", keyEvent)
window.mainloop()
