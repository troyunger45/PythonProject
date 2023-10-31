from tkinter import *

root = Tk()

root.title("Car Health Check Up!")
root.geometry('500x500')

class Car:
    def __init__(self):
        self.model = ""
        self.year = 2013
        '''
        self.milage = int(input("Enter your car's milage:   "))
        self.drivetrain = input("Enter your car's drivetrain:   ")
        self.color = input("Enter the color of your car:    ")
        '''

    def DisplayInfo(self):
        self.model = e.get()
        top = Toplevel()
        labelModel = Label(top, text= self.model)
        labelModel.pack()
        #labelModel.after(1000, lambda: labelModel.destroy())
        labelYear = Label(top, text=self.year)
        labelYear.pack()
        top.after(1000, lambda: top.destroy())
        '''
        print(self.year)
        print(self.milage)
        print(self.drivetrain)
        print(self.color)
        '''

    def HealthCheck(self):
        if (2023 - self.year) >= 10 or self.milage >= 90000:
            print("Your car is getting up there in age you might want to get it looked at.")

        else:
            print("Your car still has a lot of life in it!")

def main():
    #Creates an Entry and sets it position in the window with pack.
    global e
    e = Entry(root, width=35, borderwidth=5)
    e.pack(padx=5,pady=5)
    e.insert(0, "Please enter your car's model:")
    carOne = Car()
    global button
    button =Button(root, text="Show INFO", padx=40, pady=20 ,command=carOne.DisplayInfo)
    button.pack()
    #carOne.HealthCheck()
    
main()
root.mainloop()