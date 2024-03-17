import pyttsx3
from pypdf import PdfReader
import os


def speak(text: str):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 200)
    try:
        with open(text) as f:
            line = f.readlines()
            for word in line:
                engine.say(word)
                engine.runAndWait()
    except:
        engine.say(text)
        engine.runAndWait()

        

def writeNames():
    engine = pyttsx3.init()
    f = open("tts/voices.txt", "w")
    voices = engine.getProperty("voices")
    for i in range(len(voices)):
        f.write(str(i) + ": ")
        f.write("Name: {}\n   Language: {}\n   Gender: {}".format(voices[i].name, voices[i].languages, voices[i].gender))
        if i != len(voices) - 1:
            f.write("\n\n")
    f.close


def readpdf(path: str) -> str:
    reader = PdfReader(path)
    text = []
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text.append(page.extract_text().replace(" ", "").replace("\n", " "))
        f = open("tts/pdf.txt", "a")
        f.write(text[i])
    return "tts/pdf.txt"


def main():
    while True:
        print("Is this a pdf file? (y or n)")
        ans = input()
        if ans[0].lower() == "y" or ans[0].lower() == "n":
            break

    if ans[0] == "y":
        path = input("input the file path: ")
        txt = readpdf(path)
        speak(txt)
    else:
        txtin = input("input your text: ")
        speak(txtin)
    
    if os.path.exists(txt):
        os.remove(txt)

if __name__ == "__main__":
    main()