#Imports tkinter.
from tkinter import *

#Creates the main window.
root = Tk()
#Adds formatting for main window named root.
root.title("ImgBckgrnd")
root.geometry('500x500')
bg = PhotoImage(file="c:/Users/Owner/Downloads/IMG_20230927_141728_855.png")

class testing:
    def __init__(self):
        self.test()
    
    def test(self):
        my_canvas = Canvas(root, width=500, height=500)
        my_canvas.pack(fill="both", expand= True)
        
        my_canvas.create_image(0,0, image=bg, anchor='nw' )

        my_canvas.create_text(250,250,text="Welcome",font=("Helvetica", 50,),fill="white")

        button1 = Button(root, text="start")
        button2 = Button(root, text="reset scores")
        button3 = Button(root, text="exit")

        button1_window = my_canvas.create_window(10,10,anchor='nw', window=button1)
        button2_window = my_canvas.create_window(50,10,anchor='nw', window=button2)
        button3_window = my_canvas.create_window(130,10,anchor='nw', window=button3)
def main():
    testOne = testing()
    root.mainloop()

main()