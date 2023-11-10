import tkinter as tk

def main():

#create the main window
    window = tk.Tk()

#Set the window title
    window.title("Hello World")

#Create a label widget with message
    label = tk.Label(window,text = "Hello World")
    
# Pack the label widget to display in the window
    label.pack
    
# Start the Tkinter event loop
    window.mainloop()
    
if __name__=="__main__":
    main()