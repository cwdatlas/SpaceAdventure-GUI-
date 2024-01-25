import os
import tkinter as tk
from tkinter.font import Font

from PIL import ImageTk, Image

from src.Models.BaseCapsule import Capsule
from src.Models.BaseEngine import Engine
from src.Models.BaseTank import Tank


class PartButton(tk.Frame):
    def __init__(self, master, bg, width, height, image_dir, part, row, column, command):
        super().__init__(master=master, bg=bg, width=width, height=height)
        self.part = part
        self.row = row
        self.column = column
        self.set_invisible()
        self.bind("<Button-1>", command)

        # Find and set path
        script_dir = os.path.dirname(os.path.realpath(r"SpaceAdventure(GUI)"))
        image_path = os.path.join(script_dir, r"Images/" + image_dir + "/" + part.name + ".jpg")

        # Load and display the image using Pillow
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self, image=self.photo)
        self.image_label.pack(side="top", fill="both", expand=False)

        # Display the text label
        self.text_label = tk.Label(self, text=self.part.name, font=Font(size=20))
        self.text_label.pack(side="top")

        # Display the additional data
        text = "This is a part of a spacecraft"

        if isinstance(self.part, Capsule):
            text = "Mass: " + str(self.part.mass) + " kg" + "\n" + "Crew: " + str(self.part.crew)
        if isinstance(self.part, Tank):
            text = "Mass: " + str(self.part.mass) + " kg" + "\n" + "Liquid Fuel: " + str(self.part.liquid_fuel) + " kg" + "\n" + "Width: " + str(self.part.width) + " kg" + "\n"
        if isinstance(self.part, Engine):
            text = "Mass: " + str(self.part.mass) + " kg" + "\n" + "Thrust: " + str(self.part.thrust) + " kn" + "\n" + "Isp: " + str(self.part.isp) + " seconds" + "\n" + "Width: " + str(self.part.width) + "m" + "\n"
        self.data_label = tk.Label(self, text=text, font=Font(size=16))
        self.data_label.pack(side="top")

    def set_invisible(self):
        self.grid_forget()

    def set_visible(self):
        self.pack_propagate(False)
        self.grid(row=self.row, column=self.column, sticky="nwse", padx=5, pady=5)
