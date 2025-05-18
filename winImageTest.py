from tkinter import*
window = Tk()

photo_dog=PhotoImage(file="C:\\Users\\User\\OneDrive\\바탕 화면\\python\\WindowProgramming\\dog.gif")
photo_cat=PhotoImage(file="C:\\Users\\User\\OneDrive\\바탕 화면\\python\\WindowProgramming\\cat.gif")

label1=Label(window, image=photo_dog)
label2=Label(window, image=photo_cat)

label1.pack(side=LEFT)
label2.pack()


window.mainloop()