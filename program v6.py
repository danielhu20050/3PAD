import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import time

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - ((height // 2) + 50)
    window.geometry(f'{width}x{height}+{x}+{y}')

def create_login_page():
    def login_page(new_account:bool):
        with open("login.json", ) as infile:
            account_data =  json.load(infile)
        if new_account == False:
            if username_entry.get() in account_data.keys():
                if password_entry.get() == account_data[username_entry.get()]["password"]: 
                    messagebox.showinfo(title="Login Success", message="You successfully logged in.")
                    window.destroy()
                    create_difficulty_selection()
                else: 
                    messagebox.showerror(title="Error", message="wrong password.")
            else:
                messagebox.showerror(title="Error", message="Invalid login. (No such account)")
        else:
            if username_entry.get() not in account_data.keys() and username_entry.get() != "" and password_entry.get()!= "":
                account_data[str(username_entry.get())] = {"password":str(password_entry.get()), "high score": 0}
                with open("login.json", "w") as outfile:
                    json.dump(account_data, outfile, indent=5)
                
                messagebox.showinfo(title="Login Success", message="You successfully made new account.")
                window.destroy()
                create_difficulty_selection()
            else:
                messagebox.showerror(title="Error", message="Error in creating account.")
        

    window = tk.Tk()
    window.title("Login Form")
    window.geometry('800x600')
    window.configure(bg='black')
    center_window(window)

    frame = tk.Frame(window, bg='black')

    login_label = tk.Label(frame, text="Login", bg='black', fg="#911717", font=("Arial", 30))
    login_button = tk.Button(frame, text="Login", bg="#911717", fg="#FFFFFF", font=("Arial", 16), command=lambda: login_page(False), width=10, height=1)
    
    username_label = tk.Label(frame, text="Username: ", bg='black', fg="#FFFFFF", font=("Arial", 16))
    username_entry = tk.Entry(frame, font=("Arial", 16))

    password_label = tk.Label(frame, text="Password: ", bg='black', fg="#FFFFFF", font=("Arial", 16))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 16))

    new_account_button = tk.Button(frame, text="Sign Up", bg="#911717", fg="#FFFFFF", font=("Arial", 16), command=lambda: login_page(True), width=10, height=1)

    login_label.grid(row=0, column=0, columnspan=2, pady=40)
    username_label.grid(row=1, column=0, pady=20, padx=10)
    username_entry.grid(row=1, column=1, pady=20, padx=10)
    password_label.grid(row=2, column=0, pady=20, padx=10)
    password_entry.grid(row=2, column=1, pady=20, padx=10)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)
    new_account_button.grid(row=4, column=0, columnspan=2, pady=30)
    

    frame.pack(expand=True)

    window.mainloop()

def create_difficulty_selection():
    def set_difficulty(difficulty):
        create_math_game(difficulty)

    window = tk.Tk()
    window.title("Difficulty Page")
    window.geometry('800x600')
    window.configure(bg='black')
    center_window(window)

    frame = tk.Frame(window, bg='black')

    difficulty_label = tk.Label(frame, text="Select Difficulty", bg='black', fg="#911717", font=("Arial", 30))

    easy_button = tk.Button(frame, text="Easy", bg="#4CAF50", fg="#FFFFFF", font=("Arial", 16),
                            command=lambda: set_difficulty("easy"), width=10, height=1)
    hard_button = tk.Button(frame, text="Hard", bg="#F44336", fg="#FFFFFF", font=("Arial", 16),
                            command=lambda: set_difficulty("hard"), width=10, height=1)

    difficulty_label.grid(row=0, column=0, columnspan=2, pady=40)
    easy_button.grid(row=1, column=0, pady=20, padx=10)
    hard_button.grid(row=1, column=1, pady=20, padx=10)

    frame.pack(expand=True)

    window.mainloop()

def create_math_game(difficulty):
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Maths Game")
    root.configure(bg='black')
    center_window(root)

    question = tk.StringVar()
    correct_answer = tk.StringVar()
    questionNumber = tk.IntVar(value=1)  

    if difficulty == "easy":
        number_range_add_sub = (1, 12)
        number_range_mul_div = (1, 12)
        total_questions = 10
    else:  
        number_range_add_sub = (50, 100)
        number_range_mul_div = (15, 22)
        total_questions = 10

    start_time = None  

    answer_frame = tk.Frame(root, bg='black')
    answer_frame.grid(row=6, column=0, columnspan=2, pady=1)

    questionLabel = tk.Label(root, text="", font=('arial', 20), bg='black', fg='white')
    questionLabel.grid(row=4, column=0, pady=10, columnspan=2)

    resultLabel = tk.Label(root, text="", font=('arial', 20), bg='black', fg='white')
    resultLabel.grid(row=2, column=0, pady=10, sticky='w')

    timerLabel = tk.Label(root, text="Time: 0.0 seconds", font=('arial', 20), fg="white", bg='black')
    timerLabel.grid(row=4, column=1, pady=10, columnspan=2)

    questionNumberLabel = tk.Label(root, text=f"Question: {questionNumber.get()} / {total_questions}", font=('arial', 20), fg="red", bg='black')
    questionNumberLabel.grid(row=0, column=0, pady=10, columnspan=2)

    def generateQuestion():
        nonlocal questionLabel, correct_answer, start_time

        if questionNumber.get() == 1:  
            start_time = time.time()
            update_timer()

        operator = choice(['+', '-', '*', '/'])

        if operator in ['+', '-']:
            number1 = randint(*number_range_add_sub)
            number2 = randint(*number_range_add_sub)
        else:
            number1 = randint(*number_range_mul_div)
            number2 = randint(*number_range_mul_div)

        if operator == "-" and number1 < number2:
            number1, number2 = number2, number1
        elif operator == "/":
            while number1 % number2 != 0 or number1 // number2 == 0:  
                number1 = randint(*number_range_mul_div)
                number2 = randint(*number_range_mul_div)
            number1 *= number2

        if operator == "/":
            correct_answer.set(str(number1 // number2))
        else:
            correct_answer.set(str(eval(f"{number1} {operator} {number2}")))

        question.set(f"{number1} {operator} {number2}")
        questionLabel.config(text=f"Question: {question.get()}")

        create_answer_buttons()

    def create_answer_buttons():
        for widget in answer_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        wrong_answers = generate_wrong_answers()

        answers = [correct_answer.get()] + wrong_answers
        shuffle(answers) 

        for i, answer in enumerate(answers):
            button = tk.Button(answer_frame, text=answer, command=lambda ans=answer: checkAnswer(ans), width=55, height=2, bg="#222", fg="red")
            button.grid(row=i // 2, column=i % 2, padx=2, pady=2)

    def generate_wrong_answers():
        wrong_answers = []
        correct_value = int(correct_answer.get())  
        while len(wrong_answers) < 3:
            wrong_answer = str(randint(correct_value - 10, correct_value + 10))
            if '.' not in wrong_answer and wrong_answer != correct_answer.get() and wrong_answer not in wrong_answers:
                wrong_answers.append(wrong_answer)
        return wrong_answers
    
    def checkAnswer(selected_answer):
        nonlocal resultLabel

        if resultLabel:
            resultLabel.destroy()

        if selected_answer == correct_answer.get():
            resultLabel = tk.Label(root, text="Correct", font=('arial', 20), fg="green", bg='black')
        else:
            resultLabel = tk.Label(root, text="Incorrect", font=('arial', 20), fg="red", bg='black')

        resultLabel.grid(row=4, column=0, pady=10, sticky="w")

        if questionNumber.get() == total_questions:
            end_game()
        else:
            questionNumber.set(questionNumber.get() + 1)
            questionNumberLabel.config(text=f"Question: {questionNumber.get()} / {total_questions}")
            generateQuestion()

    def Skip():
        questionNumber.set(0)
        generateQuestion()

    def start_game():
        StartButton.destroy()
        generateQuestion()

    def restart_game():
        root.destroy()
        create_math_game(difficulty)

    def end_game():
        nonlocal start_time
        elapsed_time = time.time() - start_time
        timerLabel.config(text=f"Final Time: {elapsed_time:.2f} seconds")
        for widget in answer_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state='disabled')
        resultLabel.config(text="Game Over!", fg="red", bg='black')

    def update_timer():
        if questionNumber.get() <= total_questions:
            elapsed_time = time.time() - start_time
            timerLabel.config(text=f"Time: {elapsed_time:.2f} seconds")
            root.after(100, update_timer) 

    StartButton = tk.Button(root, text="Start Challenge", font=('arial', 15), width=71, command=start_game, bg="#444", fg="white")
    StartButton.grid(row=5, column=0, columnspan=2)

    bottom_frame = tk.Frame(root, bg='black')
    bottom_frame.grid(row=7, column=0, pady=1, columnspan=2)

    SkipButton = tk.Button(bottom_frame, text="Skip", font=('arial', 15), width=35, command=Skip, bg="#444", fg="white")
    SkipButton.grid(row=0, column=0, padx=2)

    RestartButton = tk.Button(bottom_frame, text="Restart", font=('arial', 15), width=35, command=restart_game, bg="#444", fg="white")
    RestartButton.grid(row=0, column=1, padx=2)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    root.mainloop()


if __name__ == "__main__":
    create_login_page()