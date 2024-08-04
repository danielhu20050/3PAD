import tkinter as tk
from tkinter import messagebox, ttk
from random import randint, choice

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
    answer = tk.StringVar()
    givenAnswer = tk.StringVar()
    score = tk.IntVar()
    questionNumber = tk.IntVar()

    questionLabel = None
    resultLabel = None

    def generateQuestion():
        nonlocal questionLabel
        questionNumber.set(questionNumber.get() + 1)

        number1 = randint(1, 12)
        number2 = randint(1, 12)
        operator = choice(['+', '-', '*', '/'])

        if operator == "-" and number1 < number2:
            number1, number2 = number2, number1
        if operator == "/":
            number1 *= number2 

        question.set(f"{number1} {operator} {number2}")
        answer.set(str(eval(question.get())))

        if questionLabel:
            questionLabel.destroy()

        questionLabel = tk.Label(root, text=f"Question: {question.get()}", font=('arial', 20))
        questionLabel.grid(row=2, column=0)

    def clear():
        answerEntry.delete(0, tk.END)

    def checkAnswer():
        nonlocal resultLabel, scoreLabel

        if questionNumber.get() > 10:
            return

        if resultLabel:
            resultLabel.destroy()


        correct_answer = str(eval(question.get())) if '/' not in question.get() else str(eval(question.get().replace('/', '//')))

        if correct_answer == str(givenAnswer.get()):
            score.set(score.get() + 1)
            resultLabel = tk.Label(root, text="Correct", font=('arial', 20), fg="green")
        else:
            resultLabel = tk.Label(root, text="Incorrect", font=('arial', 20), fg="red")

        resultLabel.grid(row=4, column=0)
        scoreLabel.config(text=f"Score: {score.get()}")

        if questionNumber.get() == 10:
            scoreLabel.config(text=f"Final Score: {score.get()}")
        else:
            generateQuestion()
            clear()

    def restart():
        nonlocal scoreLabel
        score.set(0)
        questionNumber.set(0)
        generateQuestion()
        clear()
        scoreLabel.config(text=f"Score: {score.get()}")

    headingLabel = tk.Label(root, text="Math Game", font=('arial', 25))
    headingLabel.grid(row=0, column=0)

    questionLabel = tk.Label(root, text=question.get(), font=('arial', 20))
    questionLabel.grid(row=2, column=0)

    answerEntry = tk.Entry(root, textvariable=givenAnswer, font=('arial', 20), width=25)
    answerEntry.grid(row=3, column=0)

    submitButton = tk.Button(root, text="Submit", fg="black", font=('arial', 15), command=checkAnswer)
    submitButton.grid(row=3, column=1)

    resultLabel = tk.Label(root, text="Result", font=('arial', 20), fg="black")
    resultLabel.grid(row=4, column=0)

    scoreLabel = tk.Label(root, text=f"Score: {score.get()}", font=('arial', 20), fg="black")
    scoreLabel.grid(row=5, column=0)

    restartButton = tk.Button(root, text="Restart", fg="black", font=('arial', 15), width=35, command=restart)
    restartButton.grid(row=6, column=0)

    generateQuestion()
    root.bind("<Return>", lambda x: checkAnswer())
    root.mainloop()

if __name__ == "__main__":
    create_login_page()
