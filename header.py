import pyttsx3
import os
import threading
import pynput
from pynput import keyboard
from pypdf import PdfReader


class textToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")


    def speak(self, text: str):
        self.engine.setProperty("voice", self.voices[0].id)
        self.engine.setProperty("rate", 200)
        if os.path.exists(text):
            with open(text) as f:
                line = f.readlines()
                for word in line:
                    self.engine.say(word)
                    self.engine.runAndWait()
        else:
            self.engine.say(text)
            self.engine.runAndWait()


    # This function is/was for figuring out all the voices on the computer
    def getNames(self):
        f = open("voices.txt", "w")
        voices = self.engine.getProperty("voices")
        for i in range(len(voices)):
            f.write(str(i) + ": ")
            f.write("Name: {}\n   Language: {}\n   Gender: {}".format(voices[i].name, voices[i].languages, voices[i].gender))
            if i != len(voices) - 1:
                f.write("\n\n")
        f.close

        
class PDF:
    # To read the pdf. Not perfect so I did my best to delete the spaces (there were spaces between every letter in one doc)
    # And replace new lines with spaces. Sure there will be some bugs later
    def readpdf(self, path: str) -> str:
        reader = PdfReader(path)
        text = []
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text.append(page.extract_text().replace(" ", "").replace("\n", " "))
            f = open("pdf.txt", "a")
            f.write(text[i])
        return "pdf.txt"