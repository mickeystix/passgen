## This is the backend for PassGen. Lightweight but also incredibly insecure password generation. Don't use this in any form of production, in other words.
## This is the "console" version

import string
import random

validresponses = ["y", "Y", "yes", "Yes", "n", "N", "no", "No"]
positiveresponses = ["y", "Y", "yes", "Yes"]
negativeresponses = ["n", "N", "no", "No"]

def prompts(selector):
    if selector == 1:
        pstring = 'Numbers'
    else:
        pstring = 'Special Characters'
    
    answer = input("Are " + pstring + " Required? [y/n]: ")

    if answer in validresponses:
        if answer in positiveresponses:
            return True
        elif answer in negativeresponses:
            return False
    else:
        print("Invalid response")
        pgstart()
       
def pgstart():
    credentiallength = int(input("Desired Credential Length: "))
    specrequired = prompts(0)
    numrequired = prompts(1)
    pg(credentiallength, specrequired, numrequired)

def getletter():
    return random.choice(string.ascii_letters)

def getnumber():
    return str(random.randint(0, 9))

def getspecial():
    return random.choice(string.punctuation)

def pg(credentiallength, specrequired, numrequired):
    ## print("\nRequested Length: " + str(credentiallength) + "\nSpec Characters: " + str(specrequired) + "\nNumbers: " + str(numrequired) + "\n")
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
        
    print("Generated Credential: " + credential)

if __name__ == ('__main__'):
    pgstart()
