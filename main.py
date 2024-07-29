from tkinter import *
from tkinter import filedialog

def open_file():
    filepath= filedialog.askopenfilename()
    if filepath:
        with open(filepath, 'r') as file:
            text_area.delete(1.0, END)
            text_area.insert(END, file.read())
def save_file():
    filepath = filedialog.askopenfilename(defaultextension="txt", filetypes=[("Text files","*.txt"),("All files","*-*")])
    if filepath:
        with open(filepath, 'w') as file:
            file.write(text_area.get(1.0,END))
def clear_text(event=None):
    text_area.delete(1.0,END)

root = Tk()
menu_bar = Menu(root)
filemenu= Menu(menu_bar, tearoff=0)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="save", command=save_file)
filemenu.add_command(label="clear", command=clear_text)
menu_bar.add_cascade(label="File", menu=filemenu)
root.config(menu=menu_bar)

text_area = Text(root, wrap='word')
text_area.pack(expand=True, fill='both')

context_menu = Menu(root, tearoff=0)
context_menu.add_command(label="Clear", command=clear_text)
def show_context_menu(event):
    context_menu.tk_popup(event.x_root,event.y_root)

text_area.bind("<Button-3>", show_context_menu)
root.title("task1")
root.mainloop()