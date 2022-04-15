from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700,300))
        self.master.title('BMI Calculator')
        self.master.config(bg='lightgray')

        self.varWeight = StringVar()
        self.varHeight = StringVar()
        
        self.lblWeight = Label(self.master, text='Your Weight in Pounds: ',font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblWeight.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblHeight = Label(self.master, text='Your Height in Inches: ',font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblHeight.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay=Label(self.master, text='',font=("Helvetica", 14), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(5,0), pady=(10,0), sticky=NW)

        self.lblDisplay2=Label(self.master, text='',font=("Helvetica", 14), fg='black', bg='lightgray')
        self.lblDisplay2.grid(row=4, column=1, padx=(5,0), pady=(0,0), sticky=W)

        self.txtWeight = Entry(self.master, text=self.varWeight, font=("Helvetica", 16), width=30, fg='black', bg='white')
        self.txtWeight.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtHeight = Entry(self.master, text=self.varHeight, font=("Helvetica", 16), width=30, fg='black', bg='white')
        self.txtHeight.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        self.btnClear = Button(self.master, text="Clear", width=10, height=2, command=self.clear)
        self.btnClear.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,180), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,00), pady=(30,0), sticky=N+E)

    def submit(self):
        weight = float(self.varWeight.get())
        height = float(self.varHeight.get())
        BMI = ((weight/height**2)*703)
        minweight = ((18.5/703)*(height**2))
        maxweight = ((24.9/703)*(height**2))
        gain = (minweight - weight)
        lose = (weight - maxweight)
        add = str(round(gain,2))
        drop = str(round(lose,2))
        result = str(round(BMI,2))
        if BMI<18.5:
            self.lblDisplay.config(text='Your BMI is {}:'.format(result))
            self.lblDisplay2.config(text='You are underweight. You need to gain               \n{} pounds to be within a healthy weight range'.format(add))
        elif BMI<25:
            self.lblDisplay.config(text='Your BMI is {}: Your weight is normal.'.format(result))
            self.lblDisplay2.config(text=' ')
        elif BMI<30:
            self.lblDisplay.config(text='Your BMI is {}:'.format(result))
            self.lblDisplay2.config(text='You are overweight. You need to lose                   \n{} pounds to be within a healthy weight range'.format(drop))
        else:
            self.lblDisplay.config(text='Your BMI is {}:'.format(result))
            self.lblDisplay2.config(text='You are obese. You need to lose                          \n{} pounds to be within a healthy weight range'.format(drop))

    def clear(self):
        self.lblDisplay.config(text=' ')
        self.lblDisplay2.config(text=' ')
        self.txtWeight.delete(0,'end')
        self.txtHeight.delete(0,'end')
        

    def cancel(self):
        self.master.destroy()

        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
