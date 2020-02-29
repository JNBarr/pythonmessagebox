 #messagebox with tkinter in python
from tkinter import *
from tkinter import messagebox

win = Tk()

result1 = messagebox.askokcancel("Title1 ", "Do you really?")
print(result1) # yes = true no = false

result2 = messagebox.askyesno("Title2", "Do you really?")
print(result2) # yes = true no = false

result3 = messagebox.askyesnocancel("Title3", "Do you really?")
print(result3) # yes = true, no = false, cancel = none

messagebox.showinfo("Title", "a Tk MessageBox")
messagebox.showwarning("warning", "a Tk warning")
messagebox.showerror("error", "a Tk error")

win.mainloop()