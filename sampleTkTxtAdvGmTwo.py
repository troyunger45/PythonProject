
from tkinter import *

class ImageChangerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Changer App")

        # Create a canvas to display the images
        self.canvas = Canvas(root, width=400, height=300)
        self.canvas.pack()

        # Load initial image
        self.current_image_path = "images/menu.png"
        self.current_image = PhotoImage(file=self.current_image_path)

        # Display the initial image on the canvas
        self.image_item = self.canvas.create_image(0, 0, anchor=NW, image=self.current_image)

        # Create buttons for changing images
        button1 = Button(root, text="Image 1", command=lambda: self.change_image("images/menu.png"))
        button2 = Button(root, text="Image 2", command=lambda: self.change_image("images/description.png"))
        button3 = Button(root, text="Image 3", command=lambda: self.change_image("images/combat1.png"))

        button1.pack(side=LEFT, padx=5)
        button2.pack(side=LEFT, padx=5)
        button3.pack(side=LEFT, padx=5)

    def change_image(self, new_image_path):
        # Change the current image
        self.current_image_path = new_image_path
        self.current_image = PhotoImage(file=self.current_image_path)

        # Update the canvas background
        self.canvas.itemconfig(self.image_item, image=self.current_image)

if __name__ == "__main__":
    root = Tk()
    app = ImageChangerApp(root)
    root.mainloop()