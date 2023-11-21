import tkinter as tk

def open_custom_dialog():
    custom_dialog = tk.Toplevel(root)
    custom_dialog.title("Custom Dialog")

    label = tk.Label(custom_dialog, text="Choose an option:")
    label.pack(pady=10)

    # Variable to store the selected option
    selected_option = tk.StringVar()

    # Create radio buttons
    radio_button1 = tk.Radiobutton(custom_dialog, text="Option 1", variable=selected_option, value="Option 1")
    radio_button2 = tk.Radiobutton(custom_dialog, text="Option 2", variable=selected_option, value="Option 2")

    radio_button1.pack()
    radio_button2.pack()

    # Button to close the dialog
    button_close = tk.Button(custom_dialog, text="Close", command=custom_dialog.destroy)
    button_close.pack()

# Create the main Tkinter window
root = tk.Tk()

# Create a button to open the custom dialog
open_button = tk.Button(root, text="Open Custom Dialog", command=open_custom_dialog)
open_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()