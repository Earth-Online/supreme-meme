from Tkinter import *
import ttk

def escape(root):
        root.geometry("200x200")

def fullscreen(root):
        width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (width, height))

master = Tk()
width, height = master.winfo_screenwidth(), master.winfo_screenheight()
master.geometry("%dx%d+0+0" % (width, height))
master.bind("<Escape>", lambda a :escape(master))
#Added this for fun, when you'll press F1 it will return to a full screen.
master.bind("<F1>", lambda b: fullscreen(master))
master.mainloop()
