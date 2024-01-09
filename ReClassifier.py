import tkinter as tk
from tkinter.filedialog import askopenfilename

currentFile : str
root = tk.Tk()
root.title("ReClassifier")

def openFile():
    currentFile = askopenfilename()
    label = tk.Label(text=currentFile, master=root)
    label.grid(column=0,row=0)
    

# Menu bar
menubar = tk.Menu(master=root)
fileMenu = tk.Menu(master=menubar, tearoff=0)
fileMenu.add_command(label="Open", command=openFile, accelerator="Command+O")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=fileMenu)
root.config(menu=menubar)

# Layout
pw = tk.PanedWindow(master=root, orient='horizontal')
# sideFrame = tk.Frame(master=pw, background="gray", width=50)
pwSide = tk.PanedWindow(master = pw, orient='vertical')
mainFrame = tk.Frame(master=pw, background="", width=50)
pw.pack(fill='both', expand=True)
pw.add(pwSide, minsize=200)
pw.add(mainFrame)

sideFrameTop = tk.Frame(master=pwSide, background='')
sideFrameBottom = tk.Frame(master=pwSide, background='')
pwSide.add(sideFrameTop, minsize=100)
pwSide.add(sideFrameBottom)


# Classes entry
def classEntry():
    def classAccept():
        classesBox.insert('end', entryField.get())
        top.destroy()
        
    def classCancel():
        top.destroy()        
    
    top = tk.Toplevel(master=root)
    entryFrame = tk.LabelFrame(text="Enter name of new class: ", master=top)
    entryFrame.grid(padx=5, pady=5, column=0, row=0, columnspan=2)
    entryField = tk.Entry(master=entryFrame)
    entryField.pack()
    buttAccept = tk.Button(master=top, text="Add", command=classAccept)
    buttCancel = tk.Button(master=top, text="Cancel", command=classCancel)
    buttAccept.grid(column=0, row=1)
    buttCancel.grid(column=1, row=1)
    
def classRemove():
    selected = classesBox.curselection()[0]
    # print(selected)
    if selected:
        classesBox.delete(selected)
    
    
# Classes list
buttClassAdd = tk.Button(master=sideFrameBottom, text="Add", command=classEntry)
buttClassRemove = tk.Button(master=sideFrameBottom, text="Remove", command=classRemove)
buttClassAdd.grid(column=0, row=0)
buttClassRemove.grid(column=1, row=0)
classesBox = tk.Listbox(master=sideFrameBottom)
classesBox.insert(1, "penguin_old")
classesBox.insert(2, "penguin_old")
classesBox.grid(column=0, row=1, columnspan=2)

root.geometry("600x400")
root.minsize(600,400)

root.mainloop()

