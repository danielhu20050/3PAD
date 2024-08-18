import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle

def create_login_page():
    def login_page():
        username = ""  
        password = ""
        if username_entry.get() == username and password_entry.get() == password:
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
            window.destroy()
            create_math_game()
        else:
            messagebox.showerror(title="Error", message="Invalid login.")

    window = tk.Tk()
    window.title("Login Form")
    window.geometry('800x600')
    window.configure(bg='black')

    frame = tk.Frame(window, bg='black')

    login_label = tk.Label(frame, text="Login", bg='black', fg="#911717", font=("Arial", 30))
    login_button = tk.Button(frame, text="Login", bg="#911717", fg="#FFFFFF", font=("Arial", 16), command=login_page, width=10, height=1)

    username_label = tk.Label(frame, text="Username: ", bg='black', fg="#FFFFFF", font=("Arial", 16))
    username_entry = tk.Entry(frame, font=("Arial", 16))

    password_label = tk.Label(frame, text="Password: ", bg='black', fg="#FFFFFF", font=("Arial", 16))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 16))

    login_label.grid(row=0, column=0, columnspan=2, pady=40)
    username_label.grid(row=1, column=0, pady=20, padx=10)
    username_entry.grid(row=1, column=1, pady=20, padx=10)
    password_label.grid(row=2, column=0, pady=20, padx=10)
    password_entry.grid(row=2, column=1, pady=20, padx=10)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    frame.pack(expand=True)

    window.mainloop()

def create_math_game():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("Math Game")
    root.configure(bg='black')

    question = tk.StringVar()
    correct_answer = tk.StringVar()
    score = tk.IntVar()
    questionNumber = tk.IntVar()
    time_left = tk.IntVar(value=15) 

    questionLabel = tk.Label(root, text="", font=('arial', 20), bg='black', fg='white')
    questionLabel.grid(row=1, column=0, pady=10)

    resultLabel = tk.Label(root, text="", font=('arial', 20), bg='black', fg='white')
    resultLabel.grid(row=6, column=0, pady=10)

    scoreLabel = tk.Label(root, text="", font=('arial', 20), fg="white", bg='black')
    scoreLabel.grid(row=7, column=0, pady=10)

    timerLabel = tk.Label(root, text=f"Time left: {time_left.get()}s", font=('arial', 20), fg="red", bg='black')
    timerLabel.grid(row=8, column=0, pady=10)

    timer_id = None

    def update_timer():
        nonlocal timer_id
        if time_left.get() > 0:
            time_left.set(time_left.get() - 1)
            timerLabel.config(text=f"Time left: {time_left.get()}s")
            timer_id = root.after(1000, update_timer)  
        else:
            end_game()

    def generateQuestion():
        nonlocal questionLabel, correct_answer

        number1 = randint(1, 12)
        number2 = randint(1, 12)
        operator = choice(['+', '-', '*', '/'])

        if operator == "-" and number1 < number2:
            number1, number2 = number2, number1
        elif operator == "/":
            while number1 % number2 != 0 or number1 // number2 == 0:
                number1 = randint(1, 12)
                number2 = randint(1, 12)
            number1 *= number2

        if operator == "/":
            correct_answer.set(str(number1 // number2))
        else:
            correct_answer.set(str(eval(f"{number1} {operator} {number2}")))

        question.set(f"{number1} {operator} {number2}")
        questionLabel.config(text=f"Question: {question.get()}")

        create_answer_buttons()

    def create_answer_buttons():
        for widget in root.winfo_children():
            if isinstance(widget, tk.Button) and widget not in (SkipButton, StartButton, RestartButton):
                widget.destroy()

        wrong_answers = generate_wrong_answers()

        answers = [correct_answer.get()] + wrong_answers
        shuffle(answers) 

        for i, answer in enumerate(answers):
            button = tk.Button(root, text=answer, command=lambda ans=answer: checkAnswer(ans), width=50, height=2, bg="#222", fg="#FFF")
            button.grid(row=2 + i, column=0, pady=10)

    def generate_wrong_answers():
        wrong_answers = []
        correct_value = int(correct_answer.get()) 
        while len(wrong_answers) < 3:
            wrong_answer = str(randint(correct_value - 10, correct_value + 10))
            if '.' not in wrong_answer and wrong_answer != correct_answer.get() and wrong_answer not in wrong_answers:
                wrong_answers.append(wrong_answer)
        return wrong_answers
    
    def checkAnswer(selected_answer):
        nonlocal resultLabel, scoreLabel

        if questionNumber.get() > 10:
            return

        if resultLabel:
            resultLabel.destroy()

        if selected_answer == correct_answer.get():
            score.set(score.get() + 1)
            resultLabel = tk.Label(root, text="Correct", font=('arial', 20), fg="green", bg='black')
        else:
            resultLabel = tk.Label(root, text="Incorrect", font=('arial', 20), fg="red", bg='black')

        resultLabel.grid(row=6, column=0, pady=10)
        scoreLabel.config(text=f"Score: {score.get()}")

        if questionNumber.get() == 10:
            scoreLabel.config(text=f"Final Score: {score.get()}")
        else:
            generateQuestion()

    def Skip():
        score.set(0)
        questionNumber.set(0)
        generateQuestion()

    def start_game():
        StartButton.destroy()
        update_timer()
        generateQuestion()

    def restart_game():
        nonlocal timer_id
        if timer_id is not None:
            root.after_cancel(timer_id) 
            timer_id = None
        root.destroy()
        create_math_game()

    def end_game():
        for widget in root.winfo_children():
            if isinstance(widget, tk.Button) and widget != RestartButton:
                widget.config(state='disabled')
        resultLabel.config(text="Time's up!", fg="red", bg='black')

    headingLabel = tk.Label(root, text="Math Game", font=('arial', 25), bg='black', fg='white')
    headingLabel.grid(row=0, column=0, pady=20)

    StartButton = tk.Button(root, text="Start Challenge", font=('arial', 15), width=35, command=start_game, bg="#444", fg="white")
    StartButton.grid(row=9, column=0, pady=10)

    SkipButton = tk.Button(root, text="Skip", font=('arial', 15), width=35, command=Skip, bg="#444", fg="white")
    SkipButton.grid(row=10, column=0, pady=10)

    RestartButton = tk.Button(root, text="Restart", font=('arial', 15), width=35, command=restart_game, bg="#444", fg="white")
    RestartButton.grid(row=11, column=0, pady=10)

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_login_page()
