from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)
#define window
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700,200))
        self.master.title('Web Generator')
        self.master.config(bg='lightgray')
#define text variables
        self.varHeading = StringVar()
        self.varWording = StringVar()
        
#Labels for entry fields
        self.lblHeading = Label(self.master, text='Add Heading:',font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblHeading.grid(row=0, column=0, padx=(10,0), pady=(10,0), sticky=NW)

        self.lblWording = Label(self.master, text='Add Wording:',font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblWording.grid(row=1, column=0, padx=(10,0), pady=(10,0), sticky=NW)
#Entry field for Heading
        self.txtHeading = Entry(self.master, text=self.varHeading, font=("Helvetica", 16), width=40, fg='black', bg='white')
        self.txtHeading.grid(row=0, column=1, padx=(10,0), pady=(10,0))
#Entry field for body wording
        self.txtWording = Entry(self.master, text=self.varWording, font=("Helvetica", 16), width=40, fg='black', bg='white')
        self.txtWording.grid(row=1, column=1, padx=(10,0), pady=(10,0))
#Create button to clear fields
        self.btnClear = Button(self.master, text="Clear", width=10, height=2, command=self.clear)
        self.btnClear.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)
#Create button to submit info and open page
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,180), pady=(30,0), sticky=NE)
#Create button to close window
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,00), pady=(30,0), sticky=N+E)
#defines what happens when Submit button is clicked
    def submit(self):
        Heading=(self.varHeading.get())
        Wording=(self.varWording.get())
#opens/creates webgen.html and overwrites current info (creates if not there, overwrites if exists)
        f = open("webgen.html", "w")
#entering html code
        f.write("<html>")
        f.write("\n\t<body>")
        f.write("\n\t\t<h1><center>")
        f.write("\n\t{}".format(Heading))
        f.write("\n\t\t</center></h1>")
        f.write("\n\t\t<h3>")
        f.write("\n\t{}".format(Wording))
        f.write("\n\t\t</h3>")
        f.write("\n\t</body>")
        f.write("\n</html>")
#closes file from editor
        f.close()
#calls browser and opens page       
        webbrowser.open_new_tab('webgen.html')
#This clears all text fields when "Clear" button is clicked
    def clear(self):
        self.txtHeading.delete(0,'end')
        self.txtWording.delete(0,'end')
        
#Closes window when "Cancel" is clicked
    def cancel(self):
        self.master.destroy()

        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
