import pyttsx3
from pypdf import PdfReader


def speak(text: str):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 200)
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
    page = reader.pages[0]
    text = page.extract_text().replace(" ", "")
    f = open("tts/pdf.txt", "w")
    f.write(text)
    return text


def main():
    print("Is this a pdf file?")
    while True:
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
    

if __name__ == "__main__":
    main()