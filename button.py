#import tkinter library
import tkinter as tk

#define the button
def button_click():
    print("button_click!")

#create the root window
root = tk.Tk()
root.title("Button Example")

# create the button object/call the class of tk.
# adding text to the botton/creating the event 
button = tk.Button(root, text="click me!", command=button_click)
button.pack()

#call the main root window/to keep the window visible
root.mainloop()