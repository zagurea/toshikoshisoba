import tkinter as tk
import pyttsx3

root = tk.Tk()
root.title("年越しそば")
root.geometry("200x100")
voice = pyttsx3.init()

voice_say = ""
kosi_count = 1

def run_kosi():
    
    global voice_say
    voice_say = ""
    kosi_count = entry.get()

    kosi_count_text = tk.Label(text="「こし」と言う回数：" + str(kosi_count))
    kosi_count_text.place(x=50,y=10)

    for i in range(int(kosi_count)):
        voice_say += "こし"

    kosi_text = tk.Label(text="とし" + voice_say + "そば")
    kosi_text.place(x=50,y=30)

    voice.say("とし" + voice_say + "そば")
    voice.runAndWait()

    
run = tk.Button(text="実行",command=run_kosi)
run.place(x = 150,y = 50)

entry = tk.Entry(width=10)
entry.place(x=15,y=55)

kosi_count_text = tk.Label(text="「こし」と言う回数：1")
kosi_count_text.place(x=50,y=10)

kosi_text = tk.Label(text="としこしそば")
kosi_text.place(x=50,y=30)

voice.say("としこしそば")
voice.runAndWait()

root.mainloop()