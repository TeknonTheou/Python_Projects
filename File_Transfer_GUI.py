from tkinter import *
from tkinter import filedialog as fd
import glob
import os
import datetime
import shutil


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)
#define window
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(600,175))
        self.master.title('File Transfer')
        self.master.config(bg='lightgray')
#define text variables
        self.varSource = StringVar()
        self.varDestination = StringVar()
#Title describing GUI function
        self.lblDisplay = Label(self.master, text='"Engage" will transfer all files modified within the last 24 hours.', font=("Helvetica", 10), width=50, fg='black', bg='lightgray')
        self.lblDisplay.grid(row=0, column=1, padx=(30,0), pady=(10,0))
#Create button to select source folder
        self.btnSource = Button(self.master, text='Select Source', width=14, height=1, command=self.source)
        self.btnSource.grid(row=1, column=0, padx=(30,0), pady=(10,0), sticky=NW)
#Displays source folder name
        self.lblSource = Label(self.master, text=' ', font=("Helvetica", 10), width=50, fg='black', bg='white')
        self.lblSource.grid(row=1, column=1, padx=(30,0), pady=(10,0))
#Create button to select destination folder
        self.btnDestination = Button(self.master, text='Select Destination', width=14, height=1, command=self.destination)
        self.btnDestination.grid(row=2, column=0, padx=(30,0), pady=(10,0), sticky=NW)
#Displays destination folder name
        self.lblDestination = Label(self.master, text=' ', font=("Helvetica", 10), width=50, fg='black', bg='white')
        self.lblDestination.grid(row=2, column=1, padx=(30,0), pady=(10,0))
#Create button to submit info and transfer files
        self.btnEngage = Button(self.master, text='Engage', width=15, height=2, command=self.engage)
        self.btnEngage.grid(row=3, column=1, padx=(0,180), pady=(15,0), sticky=NE)

#Create button to clear fields
        self.btnClear = Button(self.master, text="Clear", width=10, height=2, command=self.clear)
        self.btnClear.grid(row=3, column=1, padx=(0,90), pady=(15,0), sticky=NE)
#Create button to close window
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=3, column=1, padx=(0,0), pady=(15,0), sticky=N+E)

#Allows browsing to locate source directory
    def source(self):
        name= fd.askdirectory()
        self.lblSource.config(text='{}'.format(name))
        self.varSource = '{}'.format(name)
        
#Allows browsing to locate destination directory
    def destination(self):
        name2= fd.askdirectory()
        self.lblDestination.config(text='{}'.format(name2))
        self.varDestination = '{}'.format(name2)   

#defines what happens when Engage button is clicked
    def engage(self):
#defines myFiles as array of all files in selected folder.
        myFiles = glob.glob(r'{}\*.*'.format(self.varSource))
        for i in myFiles:
            path = i
#pulls last modified time for each file
            m_time = os.path.getmtime(i)
#sets modified time in datetime format
            dt_m = datetime.datetime.fromtimestamp(m_time)
#pulls current time
            dt_n = datetime.datetime.now()
#determines time difference in seconds
            dt_d = dt_n-dt_m
#converts seconds to hours
            hours = dt_d.total_seconds()/3600
#moves files if file was modified in 24 hours or less.
            if hours<=24:
                destination =('{}/'.format(self.varDestination))
                shutil.copy2(i, destination)

#This clears all text fields when "Clear" button is clicked
    def clear(self):
        self.lblSource.config(text=' ')
        self.lblDestination.config(text=' ')
        self.varSource = ' '
        self.varDestination = ' '
#Closes window when "Cancel" is clicked
    def cancel(self):
        self.master.destroy()
        

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
