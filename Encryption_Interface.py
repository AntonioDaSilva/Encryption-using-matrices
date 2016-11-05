

from tkinter import *
def TkinterInterface():
    window = Tk()
    window.geometry("360x380")
    window.title("Matrix Encryption/Decryption")
    
    # title , geometry and interface starting
    
    thetoptitle = Label(window)
    thetoptitle.config(font="Verdana 12 bold",text = "Matrix Encryption")
    thetoptitle.pack(side="top")
    
    #title of program
    
    file_name_ask = Label(window)
    file_name_ask.config(font="Verdana 8",text = "Enter the file name which will be encrypted -->                       ")
    file_name_ask.pack()

    # label of file name asking

    text_window = Text(window)
    text_window.config(width = 36, height = 2, font = "arial 12")
    text_window.pack(anchor="nw")

    #textbox of file asking
    
    newfile_ask = Label(window)
    newfile_ask.config(font="Verdana 8",text = "Enter the file name which will contain encrypted stuff -->         ")
    newfile_ask.pack()
    
    #new file asking label
    
    newtext_window = Text(window)
    newtext_window.config(width = 36, height = 2, font = "arial 12")
    newtext_window.pack(anchor="nw")

    #textbox of newfile asking

    do_it = Button(window)
    do_it.config(text = "Do it!")
    do_it.pack(anchor="center")

    #encryption button

    boundary=Label(window)
    boundary.config(text="- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - - - - - - - - - - - - ")
    boundary.pack()

    #boundary line

    thetoptitle2 = Label(window)
    thetoptitle2.config(font="Verdana 12 bold",text = "Matrix Decryption")
    thetoptitle2.pack()

    #matrix decyrption title

    file_name_ask2 = Label(window)
    file_name_ask2.config(font="Verdana 8",text = "Enter the file name which will be decrypted -->                       ")
    file_name_ask2.pack()

    #label of file name asking 2

    text_window2 = Text(window)
    text_window2.config(width = 36, height = 2, font = "arial 12")
    text_window2.pack(anchor="w")

    #textbox of file name asking 2

    newfile_ask2 = Label(window)
    newfile_ask2.config(font="Verdana 8",text = "Enter the file name which will contain decrypted stuff -->         ")
    newfile_ask2.pack()    

    #new file asking label 2

    newtext_window2 = Text(window)
    newtext_window2.config(width = 36, height = 2, font = "arial 12")
    newtext_window2.pack(anchor="w")



    do_it2 = Button(window)
    do_it2.config(text = "Do it!")
    do_it2.pack()

    






    
    
TkinterInterface()
