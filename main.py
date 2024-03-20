from header import *

# put this together so the user can end the speech partway through, could be done much better I bet. looking into it
def on_press(key):
    if key == pynput.keyboard.Key.esc:
        exit()

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

    talker = textToSpeech()

    while True:
        print("Is this a pdf file? (y or n)")
        ans = input()
        if ans[0].lower() == "y" or ans[0].lower() == "n":
            break

    if ans[0] == "y":
        path = input("input the file path: ")
        txt = readpdf(path)
        p = threading.Thread(target=talker.speak, args=(txt,))
        p.setDaemon(True)
        p.start()
        #using threading atm for ending the process early.
        #might move to something else though.
    else:
        while True:
            txtin = input("input your text: ")
            if txtin.replace(" ","").isalnum() == True:
                break
        p = threading.Thread(target=talker.speak, args=(txtin,))
        p.setDaemon(True)
        p.start()
        with keyboard.Listener(
        on_press=on_press) as listener:
            listener.join()
    try:
        if os.path.exists(txt):
            os.remove(txt)
    except:
        pass

if __name__ == "__main__":
    main()