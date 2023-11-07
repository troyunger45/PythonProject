#Imports tkinter.
from tkinter import *

#Creates the main window.
root = Tk()
#Adds formatting for main window named root.
root.title("Car Health Check Up!")
root.geometry('500x250')
root.configure(bg="navy blue")

#Creates Car class.
class Car:
    #Class Car constructor.
    def __init__(self):
        #Defines class attributes.
        self.model = str()
        self.year = int()
        self.milage = int()
        self.drivetrain = str()
        self.color = str()

    #Function that takes in the input from the entry and stores it into 
    #the Car class's attributes based on the order of the global count
    #variable.Then the function adds to the count value and inserts the
    #next text of the desired variable using the InsertText function.
    def EnterInfo(self):
        #Defines global count variable.
        global count
        #Stores user-input into local input variable using get.
        input = e.get()
        #Logic to determine which Car class attribute to store the
        #user-input as baised on the count variable.
        if count == 0:
            self.model = input
        elif count == 1:
            self.year = int(input)   #Int for calculations.
        elif count == 2:
            self.milage = int(input)    #Int for calculations.
        elif count == 3:
            self.drivetrain = input
        elif count == 4:
            self.color = input 
        #Adds one to the counter variable to signify the next attribute.    
        count = count + 1
        #Calls InsertText function.
        InsertText()

    #Function that creates a new window named top that displays the Car
    #class's attributes using labels.
    def DisplayInfo(self):
        #Creates a new window named top.
        top = Toplevel()
        #Formatting for the top window.
        top.configure(bg="black")
        top.geometry('200x120')
        #Creating, formatting, and packing a label to display the Car model.
        labelModel = Label(top, text= self.model,bg="black",fg="grey")
        labelModel.pack()
        #Creating, formatting, and packing a label to display the Car year.
        labelYear = Label(top, text=self.year,bg="black",fg="grey")
        labelYear.pack()
        #Creating, formatting, and packing a label to display the Car milage.
        labelMilage = Label(top, text=self.milage,bg="black",fg="grey")
        labelMilage.pack()
        #Creating, formatting, and packing a label to display the Car drivetrain.
        labelDrivetrian = Label(top, text=self.drivetrain,bg="black",fg="grey")
        labelDrivetrian.pack()
        #Creating, formatting, and packing a label to display the Car color.
        labelColor = Label(top, text=self.color,bg="black",fg="grey")
        labelColor.pack()
        #Destroys the top window after 3000 miliseconds pass.
        top.after(3000, lambda: top.destroy())
    
    #Function that creates a new window named top2 and determines if a car needs
    #to be looked at or not. The function then displays the result with a label.
    def HealthCheck(self):
        #Creates new window named top2.
        top2 = Toplevel()
        #Formats top2 window.
        top2.configure(bg="black")
        #Logic to determine if the car needs to bee looked at or not
        if (2023 - self.year) >= 10 or self.milage >= 90000:
            #Creating, formatting, and packing a label to display that the car should be looked at.
            labelOld =Label(top2, text="Your car is getting up there in age you might want to get it looked at.",bg="black",fg="grey")
            labelOld.pack()
        else:
            #Creating, formatting, and packing a label to display that the car is in good shape.
            labelNew =Label(top2, text="Your car still has a lot of life in it!",bg="black",fg="grey")
            labelNew.pack()
        #Destroys the top2 window after 3000 miliseconds pass.
        top2.after(3000, lambda: top2.destroy())

#Function outside of the Car class that inserts the right text of
#the desired variable based on the order of the global count variable.
def InsertText():
    #Deletes current text in the entry before inserting the desired text.
    e.delete(0, END)
    #Logic to determine which desired text is to be inserted in the entry
    # based on the order of the global count variable.
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

#Main function that creates an entry and three buttons on the main root window.   
def main():
    #Creating, formatting, and packing entry e to the main root window.
    global e
    e = Entry(root, width=50, borderwidth=5,bg="black",fg="grey")
    e.pack(padx=5,pady=5)
    #Instantiating carOne as a Car object.
    carOne = Car()
    #Declaring global count variable.
    global count
    count = 0  
    #Inserting the first desired text with InsertText Function.
    InsertText()
    #Creating, formatting, and packing button, button2, and button3 on the main root window.
    button =Button(root, text="Show INFO", padx=39, pady=20, background="grey" ,command=carOne.DisplayInfo)
    button2 = Button(root, text="Enter INFO", padx=40, pady=20, background="grey" ,command=carOne.EnterInfo)
    button3 = Button(root, text="Health Check-Up!", padx=22, pady=20, background="grey" ,command=carOne.HealthCheck)
    button2.pack()
    button.pack()
    button3.pack()
    
#Calling main function.    
main()
#Calling the main loop for tkinter to run.
root.mainloop()