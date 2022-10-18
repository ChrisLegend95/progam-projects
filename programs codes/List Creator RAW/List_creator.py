import tkinter as tk

root = tk.Tk()
root.geometry("450x300")
root.title("《 List Creator 》")
root.resizable(0, 0)
root.config(background="#18191A")
root.eval('tk::PlaceWindow . center')
root.iconbitmap("C:\\Users\\crill\\Documents\\Python sandbox\\RPG test\\python_red.ico")

#---Asign and grab entry text variable
box = tk.StringVar()
#--Call back for bind
def call_back(event):
    add_text()
#--The function to add the text to list
def add_text():
    li = box.get()
    gabi = "\""+li+"\""+", "
    bo.insert(tk.END, gabi)
    ent.delete(0, tk.END)

#-----Basic widgets.....
ent = tk.Entry(root, textvariable=box)
ent.place(x=15, y=10)

#---Just a instrution aka note.
tk.Label(root,background="#18191A", fg="white", text="Hit <Enter> to add or use the button.\nThis tool help you make list's\nto your codes.\nList = [\"Hello\", \"World\"]").place(x=220, y=10)

inf = tk.Label(root, text="!OBS!\n Don't add any thing",background="#18191A", fg="white", font=("bold", 12))
inf.place(x=60, y=30)

bo = tk.Text(root, width=52, height=12)
bo.place(x=15, y=85)

button = tk.Button(root, text="Add", bg="#4682B4", fg="white", command=add_text)
button.place(x=15,y=45)
#----Bind Return to add in text to the field.
root.bind("<Return>", call_back)

root.mainloop()