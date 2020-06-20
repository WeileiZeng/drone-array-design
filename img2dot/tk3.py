import tkinter

# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")

# In order to display the image in a GUI, you will use the 'PhotoImage' method of Tkinter. It will an image from the directory (specified path) and store the image in a variable.
icon = tkinter.PhotoImage(file = "tmp.png")
label = tkinter.Label(window, image = icon)
label.pack()
a=input()
icon = tkinter.PhotoImage(file = "black.png")

# Finally, to display the image you will make use of the 'Label' method and pass the 'image' variriable as a parameter and use the pack() method to display inside the GUI.
label = tkinter.Label(window, image = icon)
label.pack()

window.mainloop()
