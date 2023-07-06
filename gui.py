from tkinter import *


def checkstartup():
    return True

def checkCamera():
    return True


window = Tk()
window.geometry("700x360")
window.configure(background="White")
window.title("Face Recognition Autolock")
heading = Label(window, text="Face Recognition Autolock", relief='raised', bg="White")

optionFrame = LabelFrame(window, background='white')
startupButton = Button(optionFrame, text='Startup', command=checkstartup, background='White')
showCameraButton = Button(optionFrame, text='Show camera', command=checkCamera, background='White')


window.rowconfigure(index=3, weight=1)
window.columnconfigure(index=0, weight=1)


heading.grid(row=0,column=0,sticky='NSEW')
optionFrame.grid(row=1,column=0,sticky='NSEW')
startupButton.grid(row=0,column=0,sticky='EW')
showCameraButton.grid(row=0,column=1,sticky='EW')

window.mainloop()
