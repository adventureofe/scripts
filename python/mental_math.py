# simple and quick (badly written) program that tests mental math skills

import random as rand

def ask_question_add(min_add, max_add):
    a = rand.randint(min_add, max_add)
    b = rand.randint(min_add, max_add)

    print("What is", a, "+", b)
    answer = input()
    
    if int(answer) == a + b:
        return True
    else:
        print("NOT CORRECT, The answer was", a+b, "you entered", answer)
        return False

def ask_question_minus(min_minus, max_minus):
    a = rand.randint(min_minus, max_minus)
    b = rand.randint(min_minus, max_minus)

    print("What is", a, "-", b)
    answer = input()

    if int(answer) == a - b:
        return True
    else:
        print("NOT CORRECT, the answer was", a-b, "you entered", answer)
        return False

game_running = True

start_max = 1
start_min = 0
correct_count = 0


question_type_list = [ask_question_add, ask_question_minus];

while game_running:
    game_running = question_type_list[rand.randint(0, len(question_type_list)-1)](start_min, start_max)
    start_max = start_max + 1
    correct_count = correct_count + 1
    print("correct", correct_count)

    if correct_count % 10 == 0:
        print("level increased")
        start_min += 5
        
    
