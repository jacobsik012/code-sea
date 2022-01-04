from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x300+500+200")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set 이 없으면 스크롤을 내려도 다시 올라옴 : listbox 에 scrollbar 가 set (바인딩)된 상태
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) + "일") # 1일, 2일, ...
listbox.pack(side="left")

# scrollbar 의 command 가 listbox 의 yview 로 상대적 배치
scrollbar.config(command=listbox.yview)

root.mainloop()