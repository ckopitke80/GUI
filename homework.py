import tkinter
import tkinter.messagebox

class My_GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('1000x400')
        self.main_window.title('Label Demo')

        self.label1 = tkniter.Label(self.main_window, text='Responsive Registration')
        self.label2 = tkinter.Label(self.main_window, text='Form')

        self.label1.pack()
        self.label2.pack()


        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame1_frame = tkinter.Frame(self.main_window)
        self.mid_frame2 = tkinter.Frame(self.main_window)
        self.mid_frame3 = tkinter.Frame(self.main_window)
        self.mid_frame4 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.email_label = tkinter.Label(self.top_frame, text='Email: ')
        self.email_entry = tkinter.Entry(self.top_frame, width=20)

        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')

        self.password_label = tkinter.Label(self.mid_frame1, text='Password: ')
        self.password_entry = tkinter.Entry(self.mid_frame1, width=20)

        self.password_label_label.pack(side='left')
        self.password_entry.pack(side='left')

        self.repassword_label = tkinter.Label(self.mid_frame2, text='Re-type Password: ')
        self.repassword_entry = tkinter.Entry(self.mid_frame2, width=20)

        self.repassword_label.pack(side='left')
        self.repassword_entry.pack(side='left')

        self.first_name_label = tkinter.Label(self.mid_frame3, text='First Name: ')
        self.first_name_entry = tkinter.Entry(self.mid_frame3, width=20)

        self.first_name_label.pack(side='left')
        self.first_name_entry.pack(side='left')