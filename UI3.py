fromm tkinter import *
root=Tk()


root.geometry("655x333")
frame=Frame(root, borderwidth=6,bg="grey",relief-SUNKEN)
frame.pack(side=LEFT,anchor="nw")
b1=Button(frame,fg="red", text="Print now")
b1.pack(side=LEFT,padx=23)

b2=Button(frame,fg="red", text="Print now")
b2.pack(side=LEFT,padx=23)

b3=Button(frame,fg="red", text="Print now")
b3.pack(side=LEFT,padx=23)

b4=Button(frame,fg="red", text="Print now")
b4.pack(side=LEFT,padx=23)

root.mainloop()