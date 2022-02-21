from tkinter import *
import string
import random
import os.path

## Window 
root = Tk()
root.geometry("300x160")
root.title("PassGen")
if os.path.exists("favicon.png"):
    favicon = PhotoImage(file = "favicon.png")
    root.iconphoto(True, favicon)

## Variables and defaults for data entry/collection
cbSC = BooleanVar()
cbNum = BooleanVar()
cLen = IntVar()
specrequired = False
numrequired = False

## Helper functions
def getletter():
    return random.choice(string.ascii_letters)

def getnumber():
    return str(random.randint(0, 9))

def getspecial():
    return random.choice(string.punctuation)


## Generate Credential
def pg(credentiallength, specrequired, numrequired):
    ## Just in case we get a 0 for length, still generate something
    if credentiallength == 0:
        credentiallength = random.randint(8, 12)

    credential = ''
    i = 0

    while i < credentiallength:
        if not specrequired and numrequired:
            ## add a number or letter
            selector = random.randint(0,1)
            if selector == 0:
                credential = credential + (getletter())
            elif selector == 1:
                credential = credential + (getnumber())

        elif specrequired and numrequired:
            ## add a special character, letter, or number
            selector = random.randint(0,2)
            if selector == 0:
                credential = credential + (getletter())
            elif selector == 1:
                credential = credential + (getnumber())
            elif selector == 2:
                credential = credential + (getspecial())

        elif specrequired and not numrequired:
            ## Add a letter or special characters
            selector = random.randint(0,1)
            if selector == 0:
                credential = credential + (getletter())
            elif selector == 1:
                credential = credential + (getspecial())

        else: 
            ## Add a letter only
            credential = credential + (getletter())
        
        i += 1

    ## Clear and update output
    eOutput.delete(0, END)
    eOutput.insert(0, credential)


## Button click function
def btnGen():
    
    if cbSC.get() == 1:
        specrequired = True
    else:
        specrequired = False
    
    if cbNum.get() == 1:
        numrequired = True
    else:
        numrequired = False

    pg(cLen.get(), specrequired, numrequired)
    

## GUI Items
lblSC = Label(root, text="Are Special Characters required?").grid(row=0, column=0)
scChkbx = Checkbutton(root, variable=cbSC, onvalue=True, offvalue=False).grid(row=0, column=1)

lblNum = Label(root, text="Are Numbers required?").grid(row=1, column=0)
numChkbx = Checkbutton(root, variable=cbNum, onvalue=True, offvalue=False).grid(row=1, column=1)

lblLength = Label(root, text="Length required?").grid(row=2, column=0)
eLength = Entry(root, textvariable=cLen).grid(row=2, column=1)

lblSpacer = Label(root, text=' ').grid(row=3, column=0)
lblDefault = Label(root, text="Default: 8-12", fg="grey").grid(row=3, column=1)

lblCred = Label(root, text="Generated Credential: ").grid(row=4, column=0)
eOutput = Entry(root) ## grid addition has to be separated, otherwise check values return a 'None' before item is placed.
eOutput.grid(row=4, column=1)

btnGen = Button(root, text="Generate", command=btnTest).grid(row=6, column=1)


root.mainloop()
