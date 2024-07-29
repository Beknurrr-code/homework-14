import tkinter as tk
import random

def move_button():
    new_x = random.randint(0, root.winfo_width() - smile_button.winfo_width())
    new_y = random.randint(0, root.winfo_height() - smile_button.winfo_height())
    smile_button.place(x=new_x, y=new_y)

root = tk.Tk()
root.title("Random Smile")
root.geometry("400x400")
img = tk.PhotoImage(file='smile.gif')
smile_button = tk.Button(root, image=img, command=move_button)
smile_button.place(x=0, y=0)
root.mainloop()


