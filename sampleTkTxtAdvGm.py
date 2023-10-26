
import tkinter as tk

# Create a tkinter window
window = tk.Tk()
window.title("Text Adventure Game")

# Create a label for displaying the scenario
scenario_label = tk.Label(window, text="Welcome to the Text Adventure Game!", wraplength=300)
scenario_label.pack()

# Create buttons for the three options
button1 = tk.Button(window, text="Option 1")
button2 = tk.Button(window, text="Option 2")
button3 = tk.Button(window, text="Option 3")
button1.pack()
button2.pack()
button3.pack()

# Function to handle button clicks
def on_button_click(option):
    # Replace this with your game logic for each option
    if option == 1:
        scenario_label.config(text="You chose Option 1. Now, what's your next move?")
    elif option == 2:
        scenario_label.config(text="You chose Option 2. What's your next step?")
    else:
        scenario_label.config(text="You chose Option 3. Where will you go next?")

button1.config(command=lambda: on_button_click(1))
button2.config(command=lambda: on_button_click(2))
button3.config(command=lambda: on_button_click(3))

window.mainloop()
