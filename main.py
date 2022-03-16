from tkinter import *
import string
import random
import os.path
from tkinter import scrolledtext
import urllib.request
import webbrowser

## Window 
root = Tk()
root.geometry("675x400")
root.title("PassGen")
root.resizable(False, False)
if os.path.exists("favicon.png"):
    favicon = PhotoImage(file = "favicon.png")
    root.iconphoto(True, favicon)


## Variables and defaults for data entry/collection
gh = "https://github.com/mickeystix/passgen"
default_wordlisturl = "https://www.mit.edu/~ecprice/wordlist.10000"
custom_wordlisturl = ''
cbSC = BooleanVar()
cbNum = BooleanVar()
cbDict = BooleanVar()
cLen = IntVar()
specrequired = False
numrequired = False
dictrequired = False


## Helper functions
def setNewWURL(url):
    global custom_wordlisturl
    custom_wordlisturl = url

def getWURL():
    if custom_wordlisturl == '':
        word_url = default_wordlisturl
    else:
        word_url = custom_wordlisturl
    return word_url


def resetWURL():
    setNewWURL(default_wordlisturl)


def getletter():
    return random.choice(string.ascii_letters)

def getnumber():
    return str(random.randint(0, 9))

def getspecial():
    return random.choice(string.punctuation)

##Reach out to word list url and grab a random word
def getdict():
    try:
        response = urllib.request.urlopen(getWURL())
        long_txt = response.read().decode()
        words = long_txt.splitlines()
        selected = random.choice(words)
        return selected
    except Exception:
        eOutput.insert(END, "Dict URL Error")

    


## Generate Credential
def pg(credentiallength, specrequired, numrequired, dictrequired):
    ## Just in case we get a 0 for length, still generate something
    if credentiallength == 0:
        credentiallength = random.randint(8, 12)

    credential = ''
    i = 0

    while i < credentiallength:
        if not specrequired and numrequired and not dictrequired:
            ## add a number or letter
            selector = random.randint(0,1)
            if selector == 0:
                credential = credential + (getletter())
            elif selector == 1:
                credential = credential + (getnumber())

        elif specrequired and numrequired and not dictrequired:
            ## add a special character, letter, or number
            selector = random.randint(0,2)
            if selector == 0:
                credential = credential + (getletter())
            elif selector == 1:
                credential = credential + (getnumber())
            elif selector == 2:
                credential = credential + (getspecial())

        elif specrequired and not numrequired and not dictrequired:
            ## Add a letter or special characters
            selector = random.randint(0,1)
            if selector == 0:
                credential = credential + (getletter())
            elif selector == 1:
                credential = credential + (getspecial())
        
        elif not specrequired and not numrequired and dictrequired:
            ## Add a dictionary word or letter
            maxlength = credentiallength - i
            selectedword = getdict()
            selector = random.randint(0,1)

            ## The usual selector and also verifying word length is appropriate
            if selector == 0 and len(selectedword) < maxlength:
                credential = credential + getdict()
            elif selector == 1:
                credential = credential + (getletter())
            
            ## Adjust iterator 
            if i <= credentiallength:
                i = len(credential)
            else:
                i = len(credential) - i

        elif not specrequired and numrequired and dictrequired:
            ## Add a dictionary word or letter or number
            maxlength = credentiallength - i
            selectedword = getdict()
            selector = random.randint(0,2)

            ## The usual selector and also verifying word length is appropriate
            if selector == 0 and len(selectedword) < maxlength:
                credential = credential + getdict()
            elif selector == 1:
                credential = credential + (getletter())
            elif selector == 2:
                credential = credential + (getnumber())
            
            ## Adjust iterator 
            if i <= credentiallength:
                i = len(credential)
            else:
                i = len(credential) - i

        elif  specrequired and numrequired and dictrequired:
            ## Add a dictionary word or letter or number or spec character
            maxlength = credentiallength - i
            selectedword = getdict()
            selector = random.randint(0,3)

            ## The usual selector and also verifying word length is appropriate
            if selector == 0 and len(selectedword) < maxlength:
                credential = credential + getdict()
            elif selector == 1:
                credential = credential + (getletter())
            elif selector == 2:
                credential = credential + (getnumber())
            elif selector == 3:
                credential = credential + (getspecial())
            
            ## Adjust iterator 
            if i <= credentiallength:
                i = len(credential)
            else:
                i = len(credential) - i

        else: 
            ## Add a letter only
            credential = credential + (getletter())
        
        i += 1


    ## If dictionary words causes issues with word length, this adds letters to end of string
    if len(credential) <= credentiallength:
        fixer = credentiallength - len(credential)
        while fixer > 0:
            credential = credential + (getletter())
            fixer -= 1
    
    if len(credential) > credentiallength:
        credential = credential[0:credentiallength]

    ## Clear and update output
    eOutput.delete(0, END)
    eOutput.insert(0, credential)

    lDisplay = Label(root, text="Length Check: " + str(len(credential)), fg="grey").grid(row=3, column=11)

## Button click function
def gen():
    ## Get the repeat counter
    r = eRepeats.get()
    if r != '':
        r = int(r)
    else:
        r = 0

    ## Parameters check/set
    if cbSC.get() == 1:
        specrequired = True
    else:
        specrequired = False
    
    if cbNum.get() == 1:
        numrequired = True
    else:
        numrequired = False

    if cbDict.get() == 1:
        dictrequired = True
    else:
        dictrequired = False

    ## Repetition handler
    if r:
        if r > 1:
            while r != 0:
                pg(cLen.get(), specrequired, numrequired, dictrequired)
                txtField.insert(END, ("#" + str(r) + ": "))
                insertText()
                r -= 1
        else:
            pg(cLen.get(), specrequired, numrequired, dictrequired)
    else:
        pg(cLen.get(), specrequired, numrequired, dictrequired)
    

def insertText():
    if eOutput.get() != '':
        txtField.insert(END, (eOutput.get() + "\n"))

def clearPad():
    txtField.delete(1.0, END)


def openSettings():
    ##Settings GUI Items
    settingsWindow = Toplevel(root)
    settingsWindow.title("Settings")
    settingsWindow.geometry("620x200")
    settingsWindow.resizable(False, False)
    ## Word List Settings Items
    swlblWordList = Label(settingsWindow, text="Wordlist")
    swlblWordList.grid(row=0, column=0)
    sweWordListURL = Entry(settingsWindow, width=80)
    sweWordListURL.grid(row=0, column=1)
    sweWordListURL.insert(END, getWURL())
    swSpacer = Label(settingsWindow, text=" ")
    swSpacer.grid(row=0, column=2)
    swbtnSetWordListURL = Button(settingsWindow, text="Set", command= lambda: setNewWURL(sweWordListURL.get()))
    swbtnSetWordListURL.grid(row=0, column=2)
    swbtnResetWordListURL = Button(settingsWindow, text="Reset", command= lambda: [resetWURL(), resetURLDisplay()])
    swbtnResetWordListURL.grid(row=0, column=3)
    #swLogField = scrolledtext.ScrolledText(settingsWindow, state=DISABLED)
    #swLogField.grid(row=1, column=0, columnspan=12)

    def resetURLDisplay():
        sweWordListURL.delete(0, END)
        sweWordListURL.insert(END, default_wordlisturl)



## Main GUI Items
## Spec Char checkbox
lblSC = Label(root, text="Are Special Characters required?").grid(row=0, column=0)
scChkbx = Checkbutton(root, variable=cbSC, onvalue=True, offvalue=False).grid(row=0, column=1)

## Numbers checkbox
lblNum = Label(root, text="Are Numbers required?").grid(row=1, column=0)
numChkbx = Checkbutton(root, variable=cbNum, onvalue=True, offvalue=False).grid(row=1, column=1)

## Dict words checkbox
lblDict = Label(root, text="Try Dictionary Words?").grid(row=2, column=0)
dictChkbx = Checkbutton(root, variable=cbDict, onvalue=True, offvalue=False).grid(row=2, column=1)
lblDictInfo = Label(root, text="Words may truncate to required length", fg="grey").grid(row=2, column=11)

## Length input field
lblLength = Label(root, text="Length required?").grid(row=3, column=0)
eLength = Entry(root, textvariable=cLen).grid(row=3, column=1)

lblSpacer = Label(root, text=' ').grid(row=4, column=0)
lblDefault = Label(root, text="Default: 8-12", fg="grey").grid(row=4, column=1)

## Generated Credential Output field
lblCred = Label(root, text="Generated Credential: ").grid(row=6, column=0)
eOutput = Entry(root) ## grid addition has to be separated, otherwise check values return a 'None' before item is placed.
eOutput.grid(row=6, column=1)

## Generate Credential Button
btnGen = Button(root, text="Generate", command=gen).grid(row=7, column=1)

## Insert generated password into Text Area Button
btnInsert = Button(root, text="Insert to Notepad", command=insertText).grid(row=9, column=10)

## Clear Text Area Button
btnClearPad = Button(root, text="Clear Notepad", command=clearPad).grid(row=9, column=11)

lblSpacer = Label(root, text=' ').grid(row=8, column=0)

## Scratchpad w/scrollbar
txtFrame = Frame(root).grid(row=10, column=0)
txtField = scrolledtext.ScrolledText(txtFrame, height=10)
txtField.grid(row=10, column=0, columnspan=12, padx=(10, 0))

## Link to Github
lblAbout = Label(root, text="View on GitHub", fg="blue", cursor="hand2")
lblAbout.grid(row=0, column=11)
lblAbout.bind("<Button-1>", lambda event: webbrowser.open(gh))

## Settings button
btnSettings = Button(root, text="Settings", command=openSettings).grid(row=1, column=11)

## Repeats
lblRepeats = Label(root, text="Iterations:").grid(row=5, column=0)
eRepeats = Entry(root)
eRepeats.grid(row=5, column=1)


root.mainloop()
