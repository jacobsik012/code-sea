from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+700+200")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/image.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2 # 함수 내에서 레이블의 이미지를 바꿀 때, 변수는 전역 변수로 선언해야 한다. 
    photo2 = PhotoImage(file="gui_basic/image2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()