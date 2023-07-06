from tkinter import *

# function for button to work -> check if startup is enable/disabled
def checkstartup():
    return True

# function for button to work -> check to enable camera or not
def checkCamera():
    return True

# function for button to work -> button to change log location
def changelog():
    return True

# main window initialization and properties
window = Tk()
window.geometry("700x360")
window.configure(background="White")
window.title("Face Recognition Autolock")
heading = Label(window, text="Face Recognition Autolock", relief='raised', bg="White")

# first frame for buttons
optionFrame = LabelFrame(window, background='white')
startupButton = Button(optionFrame, text='Startup', command=checkstartup, background='White')
showCameraButton = Button(optionFrame, text='Show camera', command=checkCamera, background='White')
changelogLoc = Button(optionFrame, text='Change log location', command=changelog, background='White')

# code for creating a dynamic size window
window.rowconfigure(index=3, weight=1)
window.columnconfigure(index=0, weight=1)
optionFrame.columnconfigure(index=0, weight=1)
optionFrame.columnconfigure(index=1, weight=1)
optionFrame.columnconfigure(index=2, weight=1)

# putting all widgets to grid
heading.grid(row=0,column=0,sticky='NSEW')
optionFrame.grid(row=1,column=0,sticky='NSEW')
startupButton.grid(row=0,column=0,sticky='EW')
showCameraButton.grid(row=0,column=1,sticky='EW')
changelogLoc.grid(row=0,column=2,sticky='EW')

#  tkinter mail loop
window.mainloop()
