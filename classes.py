from tkinter import *

root = Tk()

root.title("Car Health Check Up!")
root.geometry('500x250')
root.configure(bg="navy blue")

class Car:
    def __init__(self):
        self.model = str()
        self.year = int()
        self.milage = int()
        self.drivetrain = str()
        self.color = str()
        
    def EnterInfo(self):
        global count
        input = e.get()
        if count == 0:
            self.model = input
        elif count == 1:
            self.year = int(input)
        elif count == 2:
            self.milage = int(input)
        elif count == 3:
            self.drivetrain = input
        elif count == 4:
            self.color = input     
        count = count + 1
        InsertText()

    def DisplayInfo(self):
        top = Toplevel()
        top.configure(bg="black")
        top.geometry('200x120')
        labelModel = Label(top, text= self.model,bg="black",fg="grey")
        labelModel.pack()
        labelYear = Label(top, text=self.year,bg="black",fg="grey")
        labelYear.pack()
        labelMilage = Label(top, text=self.milage,bg="black",fg="grey")
        labelMilage.pack()
        labelDrivetrian = Label(top, text=self.drivetrain,bg="black",fg="grey")
        labelDrivetrian.pack()
        labelColor = Label(top, text=self.color,bg="black",fg="grey")
        labelColor.pack()
        top.after(3000, lambda: top.destroy())
    
    def HealthCheck(self):
        top2 = Toplevel()
        top2.configure(bg="black")
        if (2023 - self.year) >= 10 or self.milage >= 90000:
            labelOld =Label(top2, text="Your car is getting up there in age you might want to get it looked at.",bg="black",fg="grey")
            labelOld.pack()
        else:
            labelNew =Label(top2, text="Your car still has a lot of life in it!",bg="black",fg="grey")
            labelNew.pack()
        top2.after(3000, lambda: top2.destroy())

def InsertText():
    e.delete(0, END)
    if count == 0:
        e.insert(0,"Enter your car's model:")
    elif count == 1:
        e.insert(0,"Enter your car's year:")
    elif count == 2:
        e.insert(0,"Enter your car's milage:")
    elif count == 3:
        e.insert(0,"Enter your car's drivetrain:")
    elif count == 4:
        e.insert(0,"Enter your car's color:")
    else:
        e.insert(0,"You have no more items to enter click 'Show INFO'")
  
def main():
    #Creates an Entry and sets it position in the window with pack.
    global e
    e = Entry(root, width=50, borderwidth=5,bg="black",fg="grey")
    e.pack(padx=5,pady=5)
    global carOne
    carOne = Car()
    global count
    count = 0  
    InsertText()
    button =Button(root, text="Show INFO", padx=39, pady=20, background="grey" ,command=carOne.DisplayInfo)
    button2 = Button(root, text="Enter INFO", padx=40, pady=20, background="grey" ,command=carOne.EnterInfo)
    button3 = Button(root, text="Health Check-Up!", padx=22, pady=20, background="grey" ,command=carOne.HealthCheck)
    button2.pack()
    button.pack()
    button3.pack()
    #carOne.HealthCheck()
    
main()
root.mainloop()