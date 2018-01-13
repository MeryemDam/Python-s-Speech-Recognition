from tkinter import *
from tkinter import ttk
import webbrowser
import speech_recognition as sr
from pygame import mixer



root = Tk()
root.title('Votre application')
root.iconbitmap('C:\\Users\\pc\\Desktop\\micro.ico')

style = ttk.Style()
style.theme_use('winnative')

photo = PhotoImage(file='C:\\Users\\pc\\Desktop\\micro.png').subsample(15,15)

label1 = ttk.Label(root, text='Rechercher:')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=40)
entry1.grid(row=0, column=1, columnspan=4)

btn2 = StringVar()

def callback():
    
    if btn2.get() == 'google':
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'Traduction':
        webbrowser.open('https://translate.google.com/?hl=fr&tab=TT&authuser=0#fr/en/'+entry1.get())
    elif btn2.get() == 'Youtube':
        webbrowser.open('http://youtube.com/search?q='+entry1.get())
def get(event):

    if btn2.get() == 'google':
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif btn2.get() == 'Traduction':
        webbrowser.open('https://translate.google.com/?hl=fr&tab=TT&authuser=0#fr/en/'+entry1.get())
    elif btn2.get() == 'Youtube':
        webbrowser.open('http://youtube.com/search?q='+entry1.get())	

def buttonClick():
    mixer.init()
    mixer.music.load('start.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone() as source:

        try:

            audio = r.listen(source, timeout=5)
            message = str(r.recognize_google(audio))
            mixer.music.load('start.mp3')
            mixer.music.play()
            entry1.focus()
            entry1.delete(0, END)
            entry1.insert(0, message)

            if btn2.get() == 'google':
                webbrowser.open('http://google.com/search?q='+message)
        
            elif btn2.get() == 'Traduction':
                webbrowser.open('https://translate.google.com/?hl=fr&tab=TT&authuser=0#fr/en/'+message)

            elif btn2.get() == 'Youtube':
                webbrowser.open('http://youtube.com/search?q='+message)

            else:
                pass

        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')

        else:
            pass    
	

entry1.bind('<Return>', get)

MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)
MyButton1.grid(row=0, column=6)

MyButton2 = ttk.Radiobutton(root, text='google', value='google', variable=btn2)
MyButton2.grid(row=1, column=1, sticky=W)

MyButton3 = ttk.Radiobutton(root, text='Traduction', value='Traduction', variable=btn2)
MyButton3.grid(row=1, column=2, sticky=W)

MyButton4 = ttk.Radiobutton(root, text='Youtube', value='Youtube', variable=btn2)
MyButton4.grid(row=1, column=3)



MyButton6 = Button(root, image=photo, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton6.grid(row=0, column=5)

entry1.focus()
btn2.set('google')
root.wm_attributes('-topmost', 1)
root.mainloop()
