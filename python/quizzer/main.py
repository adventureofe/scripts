import tkinter as tk
import tkinter.font as font
import random

russian_phrases = [
    ["are you an actor?",      "ты актёр?",   "tee ack-teur"],
    ["are you in the subway?", "ты в метро?", "tee-v metro?"],
    ["are you tim?",           "ты тим?",     "tee tim?"], 
    ["backpack",               "рюкзак",      "ROOK-zak"],
    ["bicycle",                "велосипед",   "vealossi-PED"]
]

irish_phrases = [
    ["and",                 "agus",                "augus"],
    [ "apple",              "úll",                 "ool" ],
    [ "a woman and a girl", "bean agus cailín",    "ban augus calleen"],
    [ "boy",                "buachaill",           "boo-hill"],
    [ "boy and man",        "buachaill agus fear", "bo-hill augus far"   ] 
]

class Lang:
  def __init__(self, name, name_eng, phrases):
    self.name = name
    self.name_eng = name_eng
    self.phrases = phrases

langs = {
    "russian" : Lang("Pусский", "Russian", russian_phrases),
    "irish" :  Lang("Gaeilge", "Irish", irish_phrases)
}

WIDTH = 800
HEIGHT = 800

BTN_FONT_SIZE = 19
BTN_PADDING = 10

TITLE_TEXT_SIZE = 20

QUESTION_TEXT_SIZE = 20

ENTRY_TEXT_SIZE = 40

def quiz_frame():
    main_menu_delete()
    frame["top"].place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)
    frame["middle"].place(relx = 0, rely= 0.1, relwidth = 1, relheight = 0.7)
    frame["bottom"].place(relx = 0, rely = 0.8, relwidth = 1, relheight = 0.2)

def main_menu():
    frame["bottom"].place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

    for i in btns_main_menu:
        i["font"] = font.Font(size=BTN_FONT_SIZE)
        i.pack(fill="x", pady = BTN_PADDING) 

def main_menu_delete():
    for i in btns_main_menu:
        i.destroy()

def set_title(lang): 
    title_text.set(lang.name + " / " + lang.name_eng)
    lbl_title["font"] = font.Font(size=TITLE_TEXT_SIZE)
    lbl_title.pack(fill="x")

def ask_question(data, lang, random_q):
    question_text.set("What is\n" + data[random_q][0] + "\nin " + lang + "?")
    lbl_question["font"] = font.Font(size=QUESTION_TEXT_SIZE) 
    lbl_question.pack(fill="x")

def validate(answer, data, random_q, lang):
    if(answer == data[random_q][1]):
        lbl_answer["bg"] = "green"
        answer_text.set("CORRECT!\n" + data[random_q][0] + "\nin " +  lang +  " is\n" + data[random_q][1])
    else:
        lbl_answer["bg"] = "red"
        answer_text.set("INCORRECT!\n" + data[random_q][0] + "\nin " +  lang +  " is\n" + data[random_q][1])

    lbl_answer["font"] = font.Font(size=TITLE_TEXT_SIZE)
    lbl_answer.pack(fill="x")

def quiz(lang):
    random_q = random.randint(0, len(lang.phrases)) - 1
    quiz_frame()
    set_title(lang)
    ask_question(lang.phrases, lang.name_eng, random_q)

    entry["font"] = font.Font(size=ENTRY_TEXT_SIZE)
    entry.focus() #auto select entry
    entry.pack(fill="x")

    root.bind('<Return>', lambda x:validate(entry.get(), lang.phrases, random_q, lang.name_eng))

#start tkinter
root = tk.Tk()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

frame = {
    "top"    : tk.Frame(root, bg='#000000'),
    "middle" : tk.Frame(root, bg='#002222'),
    "bottom" : tk.Frame(root, bg='#000000')
}

title_text = tk.StringVar()
lbl_title =  tk.Label(frame["top"], textvariable=title_text, bg="black", fg="cyan")

question_text = tk.StringVar()
lbl_question = tk.Label(frame["middle"], textvariable=question_text, bg="#002222", fg="cyan")

answer_text = tk.StringVar()
lbl_answer = tk.Label(frame["middle"], textvariable=answer_text, bg="#002222", fg="black")

btn_russian = tk.Button(frame["bottom"], text="Pусский / Russian", bg="black", fg="cyan", command=lambda:quiz(langs["russian"]))
btn_irish = tk.Button(frame["bottom"], text="Gaeilge / Irish", bg="black", fg="cyan", command=lambda:quiz(langs["irish"]))

btns_main_menu = [btn_russian, btn_irish]
main_menu()

entry_text = tk.StringVar()
entry = tk.Entry(frame["bottom"], textvariable=entry_text, fg = "white", bg="#221111")

#end tkinter
root.mainloop()
