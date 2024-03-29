import tkinter

class MyGUI:
    def __init__(self):
        #Create the main window widget and assign it to the variable "main window" .
        self.main_window = tkinter.Tk()


        #configure the main window
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')


        #Create a label widget containing the text "Hello World!"
        #the 'label1' is part of the root widget 'main_window'
        #this means we are creating the label in the main window
        self.label1 = tkinter.Label(self.main_window, text='Hello World!')

        self.label2 = tkinter.Label(self.main_window, text='This is my GUI program')


        #Call the pack method for each label
        #the pack method determines where a widget should be positioned and makes
        #the widget visible when the main window is displayed.

        self.label1.pack(side='left')
        self.label2.pack(side='left')


        #Enter the tkinter main loop. This funtion runs like an infinite
        #loop until you close the main window.


        tkinter.mainloop()

    
#Creat an instance of the MyGUI class.
my_gui = MyGUI()

print('Moving on.....')



