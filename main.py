from header import *

Talker = textToSpeech()
Reader = PDF()

File = ""

# put this together so the user can end the speech partway through, could be done much better I bet. looking into it
def onPress(key):
    if key == pynput.keyboard.Key.esc:
        exit()

def deleteFile(filePath):
    try:
        if os.path.exists(filePath):
            os.remove(filePath)
    except:
        pass


# writing the user flow through program in this function to clean up main
def flow() -> str:
    global File

    userAnswer = input("Is this a (pdf) or (txt) file?\n")

    if userAnswer == "pdf":
        File = input("File path: ")
    elif userAnswer == "txt" or userAnswer == "text":
        return input("File path: ")
    else:
        return input("if not, type what you would like me to say: ")


def main():
    global File

    txtin = flow()

    if File != "":
        path = File
        txt = Reader.readpdf(path)
        p = threading.Thread(target=Talker.speak, args=(txt,))
        p.start()
        with keyboard.Listener(
        on_press=onPress) as listener:
            listener.join()
        #using threading atm for ending the process early.
        #might move to something else though.
    else:
        if txtin.replace(" ","").isascii() == True:
            p = threading.Thread(target=Talker.speak, args=(txtin,))
            p.start()
            with keyboard.Listener(
            on_press=onPress) as listener:
                listener.join()
    deleteFile(txt)

if __name__ == "__main__":
    main()