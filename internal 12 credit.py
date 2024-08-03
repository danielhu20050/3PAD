import tkinter as tk
from tkinter import *
from tkinter import ttk
from random import randint,choice



root = Tk()
root.geometry("560x420")
root.title("Math Game")

question = StringVar()
answer = StringVar()
givenAnswer = StringVar()
score = IntVar()
questionNumber = IntVar()

def generateQuestion():

    global questionLabel, choice
    
    questionNumber.set(questionNumber.get() + 1) #Makes the questions only go up to 10

    number1 = randint(1 , 12)
    number2 = randint(1 , 12)
    operator = choice(['+' , '-' , '*' , '/'])

    if operator == "-" and number1 < number2:
        number1, number2 = number2, number1

    question.set(str(number1) + operator + str(number2))
    
    answer.set(eval(question.get()))

    if questionLabel:
        questionLabel.destroy()

    questionLabel = Label(root , text=f"Question: {question.get()}" , font=('arial' , 20))
    questionLabel.grid(row=2 , column=0)


def clear():
   answerEntry.delete(0, END)


def checkAnswer():
    global scoreLabel

    if questionNumber.get() > 10 :
        return

    global resultLabel

    if resultLabel:
        resultLabel.destroy()

    if str(answer.get()) == givenAnswer.get():
        score.set(score.get() + 1)
        resultLabel = Label(root , text="Correct" , font=('arial' , 20), fg="green")
        resultLabel.grid(row=4 , column=0)
        scoreLabel = Label(root , text=f"Score : {score.get()}" , font=('arial' , 20) , fg="black")
        scoreLabel.grid(row=5 , column=0)

    else:
        resultLabel = Label(root , text="Incorrect" , font=('arial' , 20) , fg="red")
        resultLabel.grid(row=4 , column=0)


    if questionNumber.get() == 10:
        scoreLabel.destroy()
        scoreLabel = Label(root , text=f"Final Score : {score.get()}" , font=('arial' , 20) , fg="black")
        scoreLabel.grid(row=5 , column=0)
    
    else:
        generateQuestion()
        clear()

        
def restart():

    global scoreLabel
    scoreLabel.destroy()

    score.set(0)
    questionNumber.set(0)
    generateQuestion()
    clear()

    scoreLabel = Label(root , text=f"Score : {score.get()}" , font=('arial' , 20) , fg="black")
    scoreLabel.grid(row=5 , column=0)

headingLabel = Label(root , text="Maths Game" , font=('arial' , 25) )
headingLabel.grid(row=0 , column=0)

questionLabel = Label(root , text=question.get() , font=('arial' , 20))
questionLabel.grid(row=2 , column=0)

answerEntry = Entry(root , textvariable=givenAnswer , font=('arial' , 20), width=25)
answerEntry.grid(row=3 , column=0)

submitButton = Button(root , text="Submit" , fg="black", font=('arial' , 15) , command=checkAnswer)
submitButton.grid(row=3 , column=1)

resultLabel = Label(root , text="Result" , font=('arial' , 20) , fg="black")
resultLabel.grid(row=4 , column=0)

scoreLabel = Label(root , text=f"Score : {score.get()}" , font=('arial' , 20) , fg="black")
scoreLabel.grid(row=5 , column=0)

submitButton = Button(root , text="Restart" , fg="black", font=('arial' , 15), width=35 , command=restart)
submitButton.grid(row=6 , column=0)

generateQuestion()


root.bind("<Return>", lambda x: checkAnswer())

root.mainloop()