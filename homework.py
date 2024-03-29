import tkinter
import tkinter.messagebox

class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('1000x400')
        self.main_window.title('Registration Demo')

        title_font = ("Times New Roman", 20)
        custom_font = ("Times New Roman", 11)

        self.label1 = tkinter.Label(self.main_window, font=title_font, text='Responsive Registration')
        self.label2 = tkinter.Label(self.main_window, font=title_font, text='Form')

        self.label1.pack()
        self.label2.pack()


        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame1 = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.mid_frame3 = tkinter.Frame(self.main_window)
        self.mid_frame4 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.email_label = tkinter.Label(self.top_frame, font=custom_font, text='Email: ')
        self.email_entry = tkinter.Entry(self.top_frame, font=custom_font, width=20)

        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        self.password_label = tkinter.Label(self.mid_frame1, font=custom_font, text='Password: ')
        self.password_entry = tkinter.Entry(self.mid_frame1, width=20, font=custom_font, show='*')

        self.password_label.pack(side='left')
        self.password_entry.pack(side='left')

        self.repassword_label = tkinter.Label(self.mid_frame2, font=custom_font, text='Re-type Password: ')
        self.repassword_entry = tkinter.Entry(self.mid_frame2, width=20, font=custom_font, show='*')

        self.repassword_label.pack(side='left')
        self.repassword_entry.pack(side='left')

        self.first_name_label = tkinter.Label(self.mid_frame3, font=custom_font, text='First Name: ')
        self.first_name_entry = tkinter.Entry(self.mid_frame3, width=10, font=custom_font)

        self.first_name_label.pack(side='left')
        self.first_name_entry.pack(side='left')

        self.last_name_label = tkinter.Label(self.mid_frame3, font=custom_font, text='Last Name: ')
        self.last_name_entry = tkinter.Entry(self.mid_frame3, width=10, font=custom_font)

        self.last_name_label.pack(side='left')
        self.last_name_entry.pack(side='left')

        

        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.mid_frame4,
                                       font=custom_font,
                                       text="Male",
                                       variable=self.radio_var,
                                       value=1)
        
        self.rb2 = tkinter.Radiobutton(self.mid_frame4,
                                       font=custom_font,
                                       text="Female",
                                       variable=self.radio_var,
                                       value=2)
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()

        self.cb1 = tkinter.Checkbutton(self.bottom_frame,
                                       font=custom_font,
                                       text="I agree with terms and conditions",
                                       variable=self.cb_var1)
        
        self.cb2 = tkinter.Checkbutton(self.bottom_frame,
                                       font=custom_font,
                                       text="I want to receive the newsletter",
                                       variable=self.cb_var2)
        
        self.cb1.pack()
        self.cb2.pack()

        self.register_button = tkinter.Button(self.bottom_frame, font=custom_font, text='Register', command=self.user_validation)

        self.register_button.pack()

        self.top_frame.pack()
        self.mid_frame1.pack()
        self.mid_frame2.pack()
        self.mid_frame3.pack()
        self.mid_frame4.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()


    def user_validation(self):
        validation = 'Thank you for registering!'
        
        if not self.radio_var.get():
            validation = 'Gender not selected.'
        
        if not self.cb_var1.get():
            validation = 'Terms and Conditions not selected.'
        
        if not self.cb_var2.get():
            validation = 'Newsletter not selected.'
        
        if self.password_entry.get() != self.repassword_entry.get():
            validation = 'Passwords do not match.'

        tkinter.messagebox.showinfo('User Input', validation)

my_gui = My_GUI()