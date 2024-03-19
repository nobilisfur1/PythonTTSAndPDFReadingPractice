import pyttsx3
import threading
import os
from pypdf import PdfReader

#put this together so the user can end the speech partway through, could be done much better I bet. looking into it
def keyChecker(path: str):
    esc = False
    while esc == False:
        input("press enter to end.")
        if os.path.exists(path):
            os.remove(path)
        exit()

def speak(text: str):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 200)
    if os.path.exists(text):
        with open(text) as f:
            line = f.readlines()
            for word in line:
                engine.say(word)
                engine.runAndWait()
    else:
        engine.say(text)
        engine.runAndWait()

        
# This function is/was for figuring out all the voices on the computer
def writeNames():
    engine = pyttsx3.init()
    f = open("voices.txt", "w")
    voices = engine.getProperty("voices")
    for i in range(len(voices)):
        f.write(str(i) + ": ")
        f.write("Name: {}\n   Language: {}\n   Gender: {}".format(voices[i].name, voices[i].languages, voices[i].gender))
        if i != len(voices) - 1:
            f.write("\n\n")
    f.close

# To read the pdf. Not perfect so I did my best to delete the spaces (there were spaces between every letter in one doc)
# And replace new lines with spaces. Sure there will be some bugs later
def readpdf(path: str) -> str:
    reader = PdfReader(path)
    text = []
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text.append(page.extract_text().replace(" ", "").replace("\n", " "))
        f = open("pdf.txt", "a")
        f.write(text[i])
    return "pdf.txt"


def main():
    while True:
        print("Is this a pdf file? (y or n)")
        ans = input()
        if ans[0].lower() == "y" or ans[0].lower() == "n":
            break

    if ans[0] == "y":
        path = input("input the file path: ")
        txt = readpdf(path)
        p = threading.Thread(target=speak, args=(txt,))  #using threading atm for ending the process early.
        p.start()                                        #might move to something else though.
        keyChecker(txt)

    else:
        while True:
            txtin = input("input your text: ")
            if txtin.replace(" ","").isalnum() == True:
                break
        threading.Thread(target=speak, args=(txtin,)).start()
        keyChecker("oof")
    
    if os.path.exists(txt):
        os.remove(txt)

if __name__ == "__main__":
    main()