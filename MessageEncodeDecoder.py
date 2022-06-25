'''Importing important libraries'''
from tkinter import *
import base64


'''Initialize Window'''
root = Tk()
root.geometry('1000x500')
root.resizable(0,0)
root.title('Message Encoder-Decoder')

Label(root, text= 'Encoder-Decoder', font= 'timesnewroman 15 bold').pack()
Label(root, text= 'VKP', font= 'timesnewroman 10 bold').pack(side= BOTTOM)


'''Define Variables'''
text = StringVar()
privatekey = StringVar()
mode = StringVar()
result = StringVar()


'''Function to Code'''
def Encode(key, message):
    enc= []
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def Decode(key, message):
    dec= []
    message= base64.urlsafe_b64decode(message).decode()
    
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256+ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


def Mode():
    if (mode.get() == 'e'):
        result.set(Encode(privatekey.get(), text.get()))
    elif (mode.get() == 'd'):
        result.set(Decode(privatekey.get(), text.get()))
    else:
        result.set("Invalid Mode")


def Exit():
    root.destroy()


def Reset():
    text.set("")
    privatekey.set("")
    mode.set("")
    result.set("")


'''Labels & Buttons to Set'''
Label(root, text= 'Message', font= 'TimesNewRoman 10').place(x=60, y= 60)
Entry(root, textvariable = text, bg='ghost white').place(x=300, y= 60)

Label(root, text= 'Key', font= 'TimesNewRoman 10').place(x= 60, y= 100)
Entry(root, textvariable = privatekey, bg= 'ghost white').place(x=300, y=100)

Label(root, text= 'Mode(e= Encode, d= Decode)', font= 'TimesNewRoman 10').place(x=60, y= 130)
Entry(root, textvariable= mode, font= 'TimesNewRoman 10', bg= 'ghost white').place(x=300, y=140)
Entry(root, textvariable= result, font= 'TimesNewRoman 10', bg= 'ghost white').place(x=300, y= 180)

Button(root, text= 'RESULT', font= 'TimesNewRoman 10', padx=2, bg= 'LightGray', command= Mode).place(x=100, y= 250)
Button(root, text= 'RESET', font= 'TimesNewRoman 10', padx= 2, pady=2, width= 6, bg= 'LimeGreen', command= Reset).place(x=200, y= 250)
Button(root, text= 'Exit', font= 'TimesNewRoman 10', padx= 2, pady= 2, width= 6, bg= 'OrangeRed', command= Exit).place(x=300, y= 250)


'''Display the window'''
root.mainloop()