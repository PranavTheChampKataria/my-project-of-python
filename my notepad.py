from tkinter import *
import tkinter.messagebox as tmsg
import os
from tkinter.filedialog import asksaveasfile, askopenfilename, asksaveasfilename

def new():
    global file
    # open the new file
    # The syntax len(text.get("1.0", "end-1c")) is the length from the start("1.0")
    # of the text to the end("end-1c") of the text
    if len(t_for_write.get("1.0", "end-1c")) == 0:
        root.title("NOTE-PAD")
        file = None
    else:
        # shows the message to the user that the current file he or she want to save or not
        value = tmsg.askyesnocancel("notepad", "Do want to save this file!")
        if value is True:
            file is not None
            files = [('Text Document', '*.txt'),  ('Python Files', '*.py'), ('All files', '*.*')]
            filesave = asksaveasfile(filetype=files, defaultextension=files)
            # call save function

        elif value is False:
            root.title("NOTE-PAD")
            file = None
            t_for_write.delete("1.0", "end")

    

def open_file():
    # open the existed file
    global file
    files = [('Text Document', '*.txt'),  ('Python Files', '*.py'), ('All files', '*.*')]
    file = askopenfilename(defaultextension=".txt", filetype=files)
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+".txt")
        t_for_write.delete(1.0, END)
        with open(os.path.basename(file), "r") as f:
            t_for_write.insert(1.0, f.read())

def save():
    global file
    # save the open file
    if file == None:
        file = asksaveasfilename(initialfile="*txt", filetype=[ ("Text documents", "*.txt"), ("All files", "*.*") ])
        if file == "":
            file = None
        else:
            f = open(file ,"w")
            f.write(t_for_write.get(1.0, END))
            f.close()
    
    else:
        f = open(file,"w")
        f.write(t_for_write.get(1.0, END))
        f.close()

def save_as():
    pass

def cut():
    # cut the selected text
    t_for_write.event_generate(("<<Cut>>"))

def copy():
    # copy the selected text
    t_for_write.event_generate(("<<Copy>>"))

def paste():
    # paste the copied text to the place where the cursor is present
    t_for_write.event_generate(("<<Paste>>"))

def message():
    # display the message to the user
    tmsg.showinfo("help", "This notepad is made by jayesh kaushik\n version 1.0")

if __name__ == "__main__":
    root = Tk()
    root.geometry("525x400")
    root.title("NOTE-PAD")
    root.configure(bg="black")
    root.wm_iconbitmap("note.png")
    file = None


    # menu for the main bar
    mainmenu = Menu(root)

    # menu in the dropdown file
    m_in__file = Menu(mainmenu, tearoff=0)
    m_in__file.add_command(label="New", command=new)
    m_in__file.add_command(label="Open", command=open_file)
    m_in__file.add_separator()
    m_in__file.add_command(label="Save", command=save)
    m_in__file.add_command(label="Save as", command=save_as)
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="File", menu=m_in__file)

    # menu in the dropdown edit
    m_for_edit = Menu(mainmenu, tearoff=0)
    m_for_edit.add_command(label="Cut", command=cut)
    m_for_edit.add_command(label="Copy", command=copy)
    m_for_edit.add_command(label="Paste", command=paste)
    mainmenu.add_cascade(label="Edit", menu=m_for_edit)
    # root.config(menu=mainmenu)

    # menu for help
    mainmenu.add_cascade(label="Help",command=message)

    # initializing the scroll bar
    s_for_scroll = Scrollbar(root)
    s_for_scroll.pack(side=RIGHT, fill=Y)

    # canvas for texting
    t_for_write = Text(root, yscrollcommand=s_for_scroll.set)
    # expand = true is used  to extand the text area to the full screen
    t_for_write.pack(expand=True, fill=BOTH)

    # joining the scroll bar to the text
    s_for_scroll.config(command=t_for_write.yview)
    root.mainloop()
