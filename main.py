from header import *

Talker = textToSpeech()
Reader = PDF()
# put this together so the user can end the speech partway through, could be done much better I bet. looking into it
def on_press(key):
    if key == pynput.keyboard.Key.esc:
        exit()

def main():

    while True:
        print("Is this a pdf file? (y or n)")
        ans = input()
        if ans[0].lower() == "y" or ans[0].lower() == "n":
            break

    if ans[0] == "y":
        path = input("input the file path: ")
        txt = Reader.readpdf(path)
        p = threading.Thread(target=Talker.speak, args=(txt,))
        p.start()
        with keyboard.Listener(
        on_press=on_press) as listener:
            listener.join()
        #using threading atm for ending the process early.
        #might move to something else though.
    else:
        while True:
            txtin = input("input your text: ")
            if txtin.replace(" ","").isascii() == True:
                break
        p = threading.Thread(target=Talker.speak, args=(txtin,))
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