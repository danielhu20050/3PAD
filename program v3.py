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
    window.configure(bg='#141414')

    frame = tk.Frame(window, bg='#141414')

    
    login_label = tk.Label(frame, text="Login", bg='#141414', fg="#911717", font=("Arial", 30))
    login_button = tk.Button(frame, text="Login", bg="#911717", fg="#FFFFFF", font=("Arial", 16), command=login_page, width=10, height=1)

    username_label = tk.Label(frame, text="Username: ", bg='#141414', fg="#FFFFFF", font=("Arial", 16))
    username_entry = tk.Entry(frame, font=("Arial", 16))

    password_label = tk.Label(frame, text="Password: ", bg='#141414', fg="#FFFFFF", font=("Arial", 16))
    password_entry = tk.Entry(frame, show="*", font=("Arial", 16))

    
    login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
    login_button.grid(row=3, column=0, columnspan=2, pady=30)

    username_label.grid(row=1, column=0)
    username_entry.grid(row=1, column=1, pady=20)

    password_label.grid(row=2, column=0)
    password_entry.grid(row=2, column=1, pady=20)

    frame.pack()

    window.mainloop()

def create_math_game():
    root = tk.Tk()
    root.geometry("560x420")
    root.title("Math Game")

    question = tk.StringVar()
    correct_answer = tk.StringVar()
    score = tk.IntVar()
    questionNumber = tk.IntVar()

    questionLabel = tk.Label(root, text="", font=('arial', 20))
    questionLabel.grid(row=1, column=0)

    resultLabel = tk.Label(root, text="", font=('arial', 20))
    resultLabel.grid(row=6, column=0)

    scoreLabel = tk.Label(root, text="", font=('arial', 20), fg="black")
    scoreLabel.grid(row=7, column=0)

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
            if isinstance(widget, tk.Button) and widget != SkipButton:
                widget.destroy()

        wrong_answers = generate_wrong_answers()

        answers = [correct_answer.get()] + wrong_answers
        shuffle(answers)  

        for i, answer in enumerate(answers):
            tk.Button(root, text=answer, command=lambda ans=answer: checkAnswer(ans), width=20).grid(row=2 + i, column=0, pady=10)

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
            resultLabel = tk.Label(root, text="Correct", font=('arial', 20), fg="green")
        else:
            resultLabel = tk.Label(root, text="Incorrect", font=('arial', 20), fg="red")

        resultLabel.grid(row=6, column=0)
        scoreLabel.config(text=f"Score: {score.get()}")

        if questionNumber.get() == 10:
            scoreLabel.config(text=f"Final Score: {score.get()}")
        else:
            generateQuestion()

    def Skip():
        score.set(0)
        questionNumber.set(0)
        generateQuestion()

    headingLabel = tk.Label(root, text="Math Game", font=('arial', 25))
    headingLabel.grid(row=0, column=0)

    SkipButton = tk.Button(root, text="Skip", fg="black", font=('arial', 15), width=35, command=Skip)
    SkipButton.grid(row=8, column=0)

    generateQuestion()
    root.mainloop()

if __name__ == "__main__":
    create_login_page()
