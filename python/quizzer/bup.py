# code moved out of main for simplifying

japanese_alphabet = [
    #english, hiragana, katakana,
    [    "a",     "あ",     "ア"],
    [    "e",     "え",     "エ"], 
    [    "i",     "い",     "イ"],
    [    "o",     "お",     "オ"],
    [    "u",     "う",     "ウ"]
]

def japanese_quiz():
    print("launched japanese quiz")
    quiz_frame()
    set_title("にほん / Japanese")

def chinese_quiz():
    print("launched chinese quiz")
    quiz_frame()
    set_title("汉语 / Chinese")
   


btn_japanese = tk.Button(frame_bottom, text="にほん / Japanese", bg="black", fg="cyan", command=lambda:japanese_quiz())

btn_chinese = tk.Button(frame_bottom, text="汉语 / Chinese", bg="black", fg="cyan", command=lambda:chinese_quiz())

btn_addition = tk.Button(frame_bottom, text="MATH: addition", bg="black", fg="cyan")
btn_subtraction = tk.Button(frame_bottom, text="MATH: substraction", bg="black", fg="cyan")
btn_multiplication = tk.Button(frame_bottom, text="MATH: multiplication", bg="black", fg="cyan")

def test():
    entry = tk.Entry(frame_2, bg="green2")
    entry.pack(side="left")

    btn_submit = tk.Button(frame_2, text="hello button", bg="black", fg="cyan")
    btn_submit.pack(side="left")

    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.grid(columnspan=3, rowspan=3)

    #lbl_test = tk.Label(root, text="hello world")
    #lbl_test.grid(column=1, row=0)
    
    #lbl_test_2 = tk.Label(root, text="test 2")
    #lbl_test_2.grid(column=1, row=0)
    
    #lbl_instructions = tk.Label(root, text="asflkj")
    #lbl_instructions.grid(column=0, row=0)
    
    #txt_test = tk.StringVar()
    #btn_test = tk.Button(root, 
    #                     textvariable=txt_test,
    #                     command=lambda:change_button(),
    #                     bg="#20bbbb", 
    #                     fg="white")
    
    #txt_test.set("hsk")
    #btn_test.grid(column=2, row=0)
