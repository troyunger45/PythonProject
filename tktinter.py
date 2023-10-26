#Import Tktinker NEEDED to run program.
from tkinter import *

#Helps create and manage the window MUST be done before creating a widget.
root = Tk()
#Adds title to the GUI page.
root.title("Simple Calculator")

'''
#Everything you make in Tkinter has two steps creating it and adding it to the screen.

------------------ LABLES/PACK/GRID ------------------
#Creating label widget.
myLabel1 = Label(root, text="Hello world!") #Can also add to screen here instead with .grid(row=0, column=0) not a great practice.
myLabel2 = Label(root, text="My name is Troy Unger!") #Can also add to screen here instead with .pack() not a great practice.

#Shoving myLabel1 on the screen with pack.
#myLabel1.pack()

#Adding label widgets onto the screen with grid.
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5 ) #Columns and rows are relative to whats already on the screen.

------------------ BUTTONS/FUNCTIONS ------------------
#Creating a function for the button to load each time it is clicked.
def myClick():
    #Creating a label widget and pushing it to the screen.
    myLabel = Label(root, text="Look! I clicked the button!")
    myLabel.pack()

#Creating a button widget and psuhing it to the screen with pack.
myButton = Button(root, text="Click Me!", padx = 50, pady= 50, command=myClick, fg="blue", bg="red")
myButton.pack()

------------------ ENTRYS/GET/INSERT ------------------
#Creating a function for the button to display the text entered from the entry.
def myClick():
    #Creates a variable to store our label text.
    hello = "Hello " + e.get() #.get() takes the text from the entry to display.
    #Creating a label widget to display entry and pushing it to the screen.
    myLabel = Label(root, text=hello) 
    myLabel.pack()

#Creating an entry widget and pushing it to the screen with pack.
e = Entry(root, width=50,bg="blue",fg="black",borderwidth=2)
e.pack()

#Inserts text into the entry that you may want displayed before the user enters input.
e.insert(0, "Enter you name:    ")

#Creating a button widget and psuhing it to the screen with pack.
myButton = Button(root, text="Enter Your Name", padx = 10, pady= 10, command=myClick, fg="black", bg="blue")
myButton.pack()
'''

#------------------ SIMPLE CALCULATOR ------------------

#Creates an Entry and sets it position in the window with grid.
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0,columnspan=3,padx=10,pady=10)

#Function that puts the currently selected numbers in the entry box taken in as a parameter from each individual button.
def button_Click(number):
    #Variable that takes what is currently in the entry box with get.
    current = e.get()
    #This deletes the number in the first position so that it does not add the numbers backwards
    #Example: pressing buttons 1 and 2 without this code would display in the entry: 121 
    e.delete(0,END)
    #inserts the selected numbers into the entry box.
    e.insert(0, str(current) + str(number)) #Need the str() that way they do not add the two when we want to cocantenate them.

#Function that clears the current numbers from the entry box.
def button_Clear():
    #Deletes current text in the entry box.
    e.delete(0,END)

#Funtcion that stores the number in the entry box before the + is clicked in a global variable then deletes the text
def button_Add():
    #Takes what is to be added in through the entry box with get.
    first_number = e.get()
    #Declares global variables 
    global f_num 
    global math
    #Declares math as the operator type that we want.
    math = "addition"
    #Declares f_num as what is currently in the entry box.
    f_num =  int(first_number)
    #Deletes newly saved numbers from entry box.
    e.delete(0,END)

#Function that grabbs the second number to be added and completes the summation.
def button_Equal():
    #Takes the second number to be added from the entry box with get.
    second_number = e.get()
    #Deletes newly saved value from entry box.
    e.delete(0, END)

    #Conditonal logic to determine which operator to use.
    if math == "addition":
        #Displays and adds both numbers together to show final response in the entry box.
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        #Displays and subtracts both numbers together to show final response in the entry box.
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        #Displays and adds both numbers together to show final response in the entry box.
        e.insert(0, f_num * int(second_number))

    if math == "division":
        #Displays and adds both numbers together to show final response in the entry box.
        e.insert(0, f_num / int(second_number))

#Funtcion that stores the number in the entry box before the - is clicked in a global variable then deletes the text
def button_Subtract():
    #Takes what is to be subtracted in through the entry box with get.
    first_number = e.get()
    #Declares global variable 
    global f_num 
    global math
    #Declares math as the operator type that we want.
    math = "subtraction"
    #Declares f_num as what is currently in the entry box.
    f_num =  int(first_number)
    #Deletes newly saved numbers from entry box.
    e.delete(0,END)

#Funtcion that stores the number in the entry box before the * is clicked in a global variable then deletes the text
def button_Multiply():
    #Takes what is to be multiplied in through the entry box with get.
    first_number = e.get()
    #Declares global variable 
    global f_num 
    global math
    #Declares math as the operator type that we want.
    math = "multiplication"
    #Declares f_num as what is currently in the entry box.
    f_num =  int(first_number)
    #Deletes newly saved numbers from entry box.
    e.delete(0,END)

#Funtcion that stores the number in the entry box before the / is clicked in a global variable then deletes the text
def button_Divide():
    #Takes what is to be subtracted in through the entry box with get.
    first_number = e.get()
    #Declares global variable 
    global f_num 
    global math
    #Declares math as the operator type that we want.
    math = "division"
    #Declares f_num as what is currently in the entry box.
    f_num =  int(first_number)
    #Deletes newly saved numbers from entry box.
    e.delete(0,END)

#Creating button widgets for the numbers.
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_Click(1)) # Lambda allows us to  
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_Click(2)) # pass parameters through 
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_Click(3)) # the button function.
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_Click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_Click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_Click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_Click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_Click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_Click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_Click(0))

#Creating button widgets for action buttons
button_add = Button(root, text="+", padx=39, pady=20, command= button_Add)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_Equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command= button_Clear)
button_subtract = Button(root, text="-", padx=41, pady=20, command= button_Subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command= button_Multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command= button_Divide)

#Adding the buttons onto the screen using grid to map out each buttons location.
#Row One.
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
#Row Two.
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
#Row Three.
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
#Row Four.
button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2) #Need Column span to be able to count for two columns.
#Row Five.
button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2) #Need Column span to be able to count for two columns.
#Row Six.
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)

#Creates an event loop that constantly loops while GUI is running NEEDED to run program.
root.mainloop()