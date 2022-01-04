from tkinter import *
import os

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480+750+200")
root.resizable(True, True)

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

text = Text(frame, width=640, height=480, yscrollcommand=scrollbar.set)
text.pack(side="left")

scrollbar.config(command=text.yview)

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)

def opencmd():
    if os.path.isfile("mynote.txt"):
        mynote_file = open("mynote.txt", "r", encoding="utf8")
        text.delete("1.0", END)
        lines = mynote_file.read()
        text.insert(END, lines)
        mynote_file.close()

def savecmd():
    saved_file = text.get("1.0", END)
    mynote_file = open("mynote.txt", "w", encoding="utf8")
    mynote_file.write(saved_file)
    mynote_file.close()

def quitcmd():
    root.quit()

menu_file.add_command(label="열기", command=opencmd)
menu_file.add_command(label="저장", command=savecmd)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=quitcmd)
menu.add_cascade(label="파일(F)", menu=menu_file)

menu.add_cascade(label="편집(E)")
menu.add_cascade(label="서식(O)")
menu.add_cascade(label="보기(V)")
menu.add_cascade(label="도움말(H)")

root.config(menu=menu)

root.mainloop()