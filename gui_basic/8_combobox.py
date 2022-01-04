import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+700+200")

value = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31 까지의 숫자

combobox = ttk.Combobox(root, height=5, values=value)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=value, state="readonly")
readonly_combobox.pack()
readonly_combobox.current(0) # 0번째 인덱스 값 선택


def btncmd():
    print(combobox.get()) # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()