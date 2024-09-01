import tkinter as tk  # Import the tkinter to create GUI.
from tkinter import messagebox  # Import messagebox from tkinter for displaying popup messages.
from random import randint, choice, shuffle  # Import random to generating random numbers and choices.
import time, os, json  # Import time for time, os for images and json for handling JSON files.
import tkinter.ttk as ttk  # Import ttk from tkinter.

PROGRAM_PATH = os.getcwd() # Get the current working directory of program.

def center_window(window):  # Function that will center the GUI window.
    """
    Function that will center the GUI window. 
    
    Args:
        window: Window will be centered.
        
    Returns: None
    """
    window.update_idletasks() # Update the window's size and layout information.
    width = window.winfo_width() # Get the width of the window.
    height = window.winfo_height() # Get the height of the window.
    x = (window.winfo_screenwidth() // 2) - (width // 2) # Calculate the x-coordinate.
    y = (window.winfo_screenheight() // 2) - ((height // 2) + 50) # Calculate the y-coordinate.
    window.geometry(f'{width}x{height}+{x}+{y}') # Set the window's geometry to center it on the screen.

class Login(): 
    """
    This class will create the login page for the maths game.
    """

    def __init__(self):
        """
        Run the login page and its functions.

        Returns: None
        """
        self.window = tk.Tk() # Create window for login page.
        self.window.title("Login Form") # Window title.
        self.window.geometry('800x600') # Window size.
        self.window.configure(bg='black') # Window background colour.
        center_window(self.window) # Center the window to the center of screen.

        frame = tk.Frame(self.window, bg='black') # Create and set frame to black.

        login_label = tk.Label(frame, text="Maths Game", bg='black', fg="#911717", font=("Arial", 30)) # Create a login label, 'Maths Game' in the login window,
        login_button = tk.Button(frame, text="Login", bg="#911717", fg="#FFFFFF", font=("Arial", 16), command=lambda: self.login_page(False), width=30, height=1) # Create a login button in login window.
        
        username_label = tk.Label(frame, text="Username: ", bg='black', fg="#FFFFFF", font=("Arial", 16)) # Create username label in login window.
        self.username_entry = tk.Entry(frame, font=("Arial", 16)) # Create username entry box in login window.

        password_label = tk.Label(frame, text="Password: ", bg='black', fg="#FFFFFF", font=("Arial", 16)) # Create password label in login window.
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 16)) # Create password entry box in login window.

        new_account_button = tk.Button(frame, text="Sign Up", bg="#911717", fg="#FFFFFF", font=("Arial", 16), command=lambda: self.login_page(True), width=30, height=1) # Create new account button in login window.

        login_label.grid(row=0, column=0, columnspan=2, pady=40) # Positioning of the login label on the GUI.
        username_label.grid(row=1, column=0, pady=20, padx=10) # Positioning of the username label on the GUI.
        self.username_entry.grid(row=1, column=1, pady=20, padx=10) # Positioning of the username entry on the GUI.
        password_label.grid(row=2, column=0, pady=20, padx=10) # Positioning of the password label on the GUI.
        self.password_entry.grid(row=2, column=1, pady=20, padx=10) # Positioning of the password entry on the GUI.
        login_button.grid(row=3, column=0, columnspan=2, pady=30) # Positioning of the login button on the GUI.
        new_account_button.grid(row=4, column=0, columnspan=2, pady=30) # Positioning of the new account button on the GUI.

        frame.pack(expand=True) # Pack frame and expand it to fill out the window.

        self.window.mainloop() # Runs the tkinter window.
        
    def login_page(self, new_account: bool):
        """
        This function handles the login and signup features in the program.

        Args:
            new_account (bool): Shows if new account is being created.
        
        Returns: None
        """
        with open("login.json", ) as infile:  # Open the login.json file to read existing account data.
            account_data = json.load(infile)  # Load the account data from the JSON file into a dictionary.

        global username # Global variable.
        username = self.username_entry.get() # Get the username from the username entry.
        password = self.password_entry.get() # Get the password from the password entry.

        if new_account == False: # If user is not creating a new account.
            if username in account_data.keys(): # Check if username is in account data.
                if password == account_data[username]["password"]: # If entered password is correct.
                    messagebox.showinfo(title="Login Success", message="You successfully logged in.") # Display message saying successful login.
                    self.window.destroy() # Close the login window.
                    self.difficulty_selection = Difficulty() # Set the difficulty selection window.
                    self.difficulty_selection.run() # Run the method to open the new window.
                elif password == "": # If user leaves password as blank.
                    messagebox.showerror(title="Error", message="Incorrect. Blank password.") # Display error message saying blank password.
                else: # Else any other errors.
                    messagebox.showerror(title="Error", message="Incorrect password. Please try again.") # Display error message saying incorrect password.
            else: # Else if the username does not exist.
                messagebox.showerror(title="Error", message="Username does not exist. Recheck username, or create a new account.") # Display error message saying username does not exist.
        else: # Else if user is creating account.
            if new_account:  # If user is creating account.
                if username in account_data.keys(): # Check if username is in account data.
                    messagebox.showerror(title="Error", message="Username already exists. Please choose a different username.") # Display error message saying username already exists.
                elif username == "": # If username is left empty.
                    messagebox.showerror(title="Error", message="Username cannot be empty.") # Display error message saying username cannot be left empty.
                elif password == "": # If password is left empty.
                    messagebox.showerror(title="Error", message="Password cannot be empty.") # Display error message saying password cannot be left empty.
                else: # If user and password are valid.
                    account_data[username] = { # Add the account to the json file.
                        "password": password, # Store the user's password.
                        "high scores": {"easy": 100, "hard": 100} # Set default high scores as 100.
                    }
                    with open("login.json", "w") as outfile: # Open the login.json file in write.
                        json.dump(account_data, outfile, indent=5) # Save the account data to the JSON file.

                    messagebox.showinfo(title="Account Created", message="You successfully created a new account.") # Display message saying account has been created.
                    self.window.destroy() # Destroy window
                    self.difficulty_selection = Difficulty() # Set the difficulty selection window.
                    self.difficulty_selection.run() # Run the method to open the new window.

class Difficulty():
    """
    Class will create the difficulty selection window and allow the user to choose their preferred difficulty.

    Returns: None
    """
    
    def set_difficulty(self, difficulty):
        """
        Set the difficulty for the game.
        
        Args:
            difficulty: Chooses the easy or hard difficulty.
        
        Returns: None
        """
        create_math_game(difficulty) # Call on the function to create the math game.

    def run(self):
        """
        Create and then show the difficulty selection window.

        Returns: None
        """
        window = tk.Tk() # Create the window for difficulty selection window.
        window.title("Difficulty Page") # Window title.
        window.geometry('800x600') # Window size.
        window.configure(bg='black') # Window background colour.
        center_window(window) # Center the window when opened.

        frame = tk.Frame(window, bg='black') # Create a frame and set it to black background.

        difficulty_label = tk.Label(frame, text="Select Difficulty", bg='black', fg="#911717", font=("Arial", 30)) # Create a difficulty label, 'Select Difficulty' on the difficulty GUI.

        easy_button = tk.Button(frame, text="Easy", bg="#4CAF50", fg="#FFFFFF", font=("Arial", 16), # Create an easy difficulty button.
                                command=lambda: self.set_difficulty("easy"), width=10, height=1) # Set the difficulty to easy.
        hard_button = tk.Button(frame, text="Hard", bg="#F44336", fg="#FFFFFF", font=("Arial", 16), # Create a hard difficulty button.
                                command=lambda: self.set_difficulty("hard"), width=10, height=1) # Set difficulty to hard.

        difficulty_label.grid(row=0, column=0, columnspan=2, pady=40) # Positioning of the difficulty label on the GUI.
        easy_button.grid(row=1, column=0, pady=20, padx=10) # Positioning of the easy button on the GUI.
        hard_button.grid(row=1, column=1, pady=20, padx=10) # Positioning of the hard button on the GUI.

        frame.pack(expand=True) # Pack frame and expand it to fill out the window.

        window.mainloop() # Run the tkinter window.

def create_math_game(difficulty): 
    """
    This function creates the maths game program window.

    Args:
        difficulty: Chooses the easy or hard difficulty.
    
    Returns: None
    """
    root = tk.Tk() # Create window for maths game.
    root.geometry("800x600") # Window size.
    root.title("Maths Game") # Window title.
    root.configure(bg='black') # Black background colour.
    center_window(root) # Center the window when it runs.

    question = tk.StringVar() # Tk variable for the question.
    correct_answer = tk.StringVar() # Tk variable for the question answer.
    correct_answers_count = tk.IntVar(value=0)  # Variable to count correct answers.

    car2_should_move = True  # Control movement for car2.

    if difficulty == "easy": # If chosen difficulty is easy.
        number_range_add_sub = (1, 12) # Number range for addition and subtraction is 1 - 12.
        number_range_mul_div = (1, 12) # Number range for mulitplcation and division is 1 - 12.
        total_correct_answers_needed = 10 # Need 10 correct answers to finish.
    else:  # Else if hard difficulty.
        number_range_add_sub = (50, 100) # Number range for addition and subtraction is 50 - 100.
        number_range_mul_div = (15, 22) # Number range for mulitplcation and division is 15 - 22.
        total_correct_answers_needed = 10 # Need 10 correct answers to finish.

    global start_time # Global variable.

    def on_close():
        """
        This function handles the close events and any scheduled event callbacks.

        Returns: None
        """
        if 'timer_update_id' in globals(): # Check if the timer is running.
            root.after_cancel(timer_update_id) # Stop the timer.
        if 'car2_update_id' in globals(): # Check if car2 is still moving.
            root.after_cancel(car2_update_id) # Stop car2.
        root.destroy() # Destroy the window and program.

    root.protocol("WM_DELETE_WINDOW", on_close) # Calls the on_close function when program is closed.

    car_canvas = tk.Canvas(root, background= "blue") # Create canvas with blue background for the cars.
    car_canvas.place(relx=0, rely=0, width=800, height=400) # Place canvas and size to 800x400.

    track = tk.PhotoImage(master= root, file=f"{PROGRAM_PATH}/race track.png") # Get track image from files.
    car_canvas.create_image(0, 0, anchor="nw",image= track) # Place track image onto canvas.
    
    car1_img = tk.PhotoImage(master= root, file=f"{PROGRAM_PATH}\car1.png") # Get car image from files.
    car1 = car_canvas.create_image(0, 50, anchor="nw",image= car1_img) # Place car image onto canvas.
    
    car2_img = tk.PhotoImage(master= root, file=f"{PROGRAM_PATH}\car2.png") # Get car image from files.
    car2 = car_canvas.create_image(0, 315, anchor="nw",image= car2_img) # Place car image onto canvas.
  
    answer_frame = tk.Frame(root, bg='black') # Frame for the answer buttons.
    answer_frame.grid(row=6, column=0, columnspan=2, pady=1) # Positioning of the frame.

    questionLabel = tk.Label(root, text="", font=('arial', 20), bg='black', fg='white') # Label for displaying question text.
    questionLabel.grid(row=4, column=0, pady=10, columnspan=2) # Positioning of the question label.

    resultLabel = tk.Label(root, text="", font=('arial', 20), bg='#232323', fg='white') # Create label to show if answer is correct or incorrect.
    resultLabel.grid(row=2, column=0, pady=10, sticky='w') # Positioning of the results label.

    timerLabel = tk.Label(root, text="Time: 0.0 seconds", font=('arial', 20), fg="white", bg='black') # Create label to display the time taken for program game.
    timerLabel.grid(row=4, column=1, pady=10, columnspan=2) # Positioning of the timer label.

    correctAnswersLabel = tk.Label(root, text=f"Correct Answers: {correct_answers_count.get()} / {total_correct_answers_needed}", font=('arial', 20), fg="red", bg='#232323') # Label to display amount of correct answers.
    correctAnswersLabel.grid(row=0, column=0, pady=10, columnspan=2) # Positioning of the correct answers label.
    
    def generateQuestion(): 
        """
        Generate random maths questions.

        Returns: None
        """
        nonlocal questionLabel, correct_answer # Declare questionlabel and correct_answer.

        operator = choice(['+', '-', '*', '/']) # Choose operator from the given ones.

        if operator in ['+', '-']: # If operator is addition or subtraction.
            number1 = randint(*number_range_add_sub) # Randomly generates a number from the set addition and subtraction range.
            number2 = randint(*number_range_add_sub) # Randomly generates a number from the set addition and subtraction range.
        else:
            number1 = randint(*number_range_mul_div) # Randomly generates a number from the set multiplication and division range.
            number2 = randint(*number_range_mul_div) # Randomly generates a number from the set multiplication and division range.

        if operator == "-" and number1 < number2: # If operator is subtraction and number 1 is smaller than number 2.
            number1, number2 = number2, number1 # Swap values of number 1 and 2.
        elif operator == "/": # If operator is division.
            while number1 % number2 != 0 or number1 // number2 == 0:  # Make sure that division answer is not 0 and an integer.
                number1 = randint(*number_range_mul_div) # Keep generating new numbers until valid question.
                number2 = randint(*number_range_mul_div) # Keep generating new numbers until valid question.
            number1 *= number2 # Change number 1 so it can be divisible by number 2.

        if operator == "/": # If operator is division.
            correct_answer.set(str(number1 // number2)) # Set correct answer to result of divison.
        else: # Else.
            correct_answer.set(str(eval(f"{number1} {operator} {number2}"))) # Evaluate and set the correct answer.

        question.set(f"{number1} {operator} {number2}") # Set the question.
        questionLabel.config(text=f"Question: {question.get()}") # Show the question on the question label.

        create_answer_buttons() # Call function to create answer buttons.

    def create_answer_buttons():
        """
        Create the answer buttons and display the answers on them.

        Returns: None
        """
        for widget in answer_frame.winfo_children(): # Any widget located in answer frame.
            if isinstance(widget, tk.Button): # If widget is button.
                widget.destroy() # Destroy button.

        wrong_answers = generate_wrong_answers() # Call function for wrong answers.

        answers = [correct_answer.get()] + wrong_answers # Combine the correct and incorrect answers.
        shuffle(answers) # Shuffle the order of answers.

        for i, answer in enumerate(answers): # Loop through answers.
            button = tk.Button(answer_frame, text=answer, command=lambda ans=answer: checkAnswer(ans), width=55, height=2, bg="#222", fg="white") # Create button with answer on it.
            button.grid(row=i // 2, column=i % 2, padx=2, pady=2) # Positioning of buttons.

    def generate_wrong_answers(): 
        """
        Generate wrong answers to be put on buttons.

        Returns:
            wrong_answers: Incorrect answers to be displayed.
        """
        wrong_answers = [] # List to store the wrong answers.
        correct_value = int(correct_answer.get())  # Correct answer will be integer.
        while len(wrong_answers) < 3: # Generate 3 wrong answers.
            wrong_answer = str(randint(correct_value - 10, correct_value + 10)) # Make sure the wrong numbres are close to real answer value with +- 10.
            if '.' not in wrong_answer and wrong_answer != correct_answer.get() and wrong_answer not in wrong_answers: # Check if generated wrong answer is valid.
                wrong_answers.append(wrong_answer) # If generated wrong answer is valid, add to list.
        return wrong_answers # Return wrong answers.
    
    def checkAnswer(givenAnswer): 
        """
        Function checks if the answer the user selected is correct or not.

        Args:
            givenAnswer: The answer that is selected by user.

        Returns: None
        """
        if givenAnswer == correct_answer.get(): # If user's answer is correct.
            correct_answers_count.set(correct_answers_count.get() + 1) # Increase correct answers count by +1.
            resultLabel.config(text="Correct!", fg="green") # Display green 'Correct!' text.
            smooth_move_car1(65)  # Move car1 by 65 pixels.
        else: # Else.
            resultLabel.config(text="Incorrect. Try Again.", fg="red") # Display red 'Incorrect!' text.
            smooth_move_car1(-65) # Move car1 backwards by 65 pixels.
            if correct_answers_count.get() != 0: # If correct answer count is not 0.
                correct_answers_count.set(correct_answers_count.get() - 1) # Decrease correct answer count by -1.

        correctAnswersLabel.config(text=f"Correct Answers: {correct_answers_count.get()} / {total_correct_answers_needed}") # Correct answers label for how many questions user has got right.
        
        if correct_answers_count.get() >= total_correct_answers_needed: # If correct answers got is greater then correct answers needed.
            end_time = time.time() # Stop the timer.
            elapsed_time = round(end_time - start_time, 2) # Calculate the time.
            display_win_screen(elapsed_time) # Show the win screen with the user's time.
        else: # Else.
            generateQuestion() # Keep generating questions.

    def display_win_screen(elapsed_time):
        """
        Function displays the win screen if user wins the game.

        Args:
            elapsed_time: Time taken for user to finish the race game.

        Returns: None
        """
        nonlocal car2_should_move  # Declare car2_should_move.
        car2_should_move = False  # Control car2 movement.

        questionLabel.grid_remove() # Remove the questions label.
        for widget in answer_frame.winfo_children(): # If any widget in answer frame.
            if isinstance(widget, tk.Button): # If widget is a button.
                widget.grid_remove() # Remove the buttons.

        timerLabel.grid_remove() # Remove timer.
        resultLabel.grid_remove() # Remove results text.

        win_label = tk.Label(root, text="You Win!", font=('arial', 40), fg="green", bg="#232323") # Show 'You Win!' label.
        win_label.grid(row=1, column=0, pady=20, columnspan=2) # Positioning of the win label.

        winning_text = tk.Label(root, text="Congratulations! You reached the finish line before the opponent", font=('arial', 20), fg="white", bg="black") # Show winning text when user wins.
        winning_text.grid(row=3, column=0, pady=20, columnspan=2) # Positioning of the winning text.

        with open("login.json", "r") as infile: # Open JSON file in read mode.
            account_data = json.load(infile) # Load account data in JSON.
        
        current_high_score = float(account_data[username]["high scores"][difficulty]) # Write account data, high score and difficulty.

        if elapsed_time < current_high_score:  # If time taken is faster than high score.
            account_data[username]["high scores"][difficulty] = elapsed_time # Update high score.
            with open("login.json", "w") as outfile: # Open JSON in write mode.
                json.dump(account_data, outfile, indent=4) # Save the account data back to the JSON file.
            high_score_message = f"NEW High Score: {elapsed_time:.2f} seconds" # Displays message saying new high score.
        else: # Else.
            high_score_message = f"High Score: {current_high_score:.2f} seconds" # Displays message if no new high score.

        time_label = tk.Label(root, text=f"Your Time: {elapsed_time:.2f} seconds, {high_score_message}", font=('arial', 20), fg="white", bg="black") # Displays time label showing what your time was.
        time_label.grid(row=2, column=0, pady=20, columnspan=2) # Positioning of the time label.
                
    def smooth_move_car1(distance): 
        """
        Move car 1 with a smooth moving animation.

        Args:
            distance: Distance to move car 1.

        Returns: None
        """
        steps = 20  # Number of steps the car takes to move.
        step_distance = distance / steps  # Distance for each step.
        interval = 20  # Time for each step.

        def move_step(current_step):
            """
            Function handles the movement of car 1.

            Args:
                current_step: Current step in the moving event.

            Returns: None
            """
            nonlocal step_distance # Declare step_distance.

            current_x = car_canvas.coords(car1)[0] # Get x coord of car1.

            new_x = current_x + step_distance # Calculate new x-coordinate based on step distance.

            if new_x < 0: # Makes sure car1 doesn't move behind the starting position.
                step_distance = -current_x  # Adjust the step distance to stop at start line.
                new_x = 0  # Set new x coordinate.

            if current_step < steps: # If current steps is less than steps.
                car_canvas.move(car1, step_distance, 0) # Move car1 by step_distance.
                car_canvas.after(interval, move_step, current_step + 1) # Schedule the next step after interval.

        move_step(0) # Start car1 movement.

    def start_game():
        """
        Starts the maths game.

        Returns: None
        """
        global start_time # Declare global variable.
        start_time =  time.time() # Start recording time.
        update_timer() # Updates timer.
        StartButton.destroy() # Removes the start button from window.
        move_car2() # Begin car2 movement.
        generateQuestion() # Generate the maths questions.

    def restart_game():
        """
        Destroys the game window and creates a new one to restart the game.

        Returns: None
        """
        if 'timer_update_id' in globals(): # Check if the timer is running.
            root.after_cancel(timer_update_id) # Stop the timer.
        if 'car2_update_id' in globals(): # CHeck if car2 is still moving.
            root.after_cancel(car2_update_id) # Stop car2.
        root.destroy()  # Destroy the current window
        create_math_game(difficulty)  # Start the game again with the selected difficulty

    def update_timer(): 
        """
        Function updates the timer that tracks the user's time taken.

        Returns: None
        """
        global timer_update_id # Declare global variable.
        if correct_answers_count.get() < total_correct_answers_needed: # If number of correct answers is less than total correct answers needed.
            elapsed_time = round(time.time() - start_time, 2) # Calculate time since start of game.
            timerLabel.config(text=f"Time: {elapsed_time} seconds") # Display and update time label.
            timer_update_id = root.after(100, update_timer) # Update timer every 100 milliseconds.
    
    def move_car2():
        """
        Function handles car 2 movement across the canvas based on selected difficulty.

        Returns: None
        """
        car2_start_time = time.time() # Record start time for car 2.
        car2_distance = 650  # Distance car 2 needs to travel.
        if difficulty == "easy": # If selected difficulty is easy.
            car2_duration = 25  # Amount of time set for car 2 to travel from start to finish.
        else: # Else if difficulty is hard.
            car2_duration = 30 # Amount of time set for car 2 to travel from start to finish.
            
        car2_interval = 70  # Time updates every 70 milliseconds.

        def update_car2(): 
            """
            Update car 2's position on the track image.

            Returns: None
            """
            global car2_update_id # Declare global variable.
            if car2_should_move: # If car 2 should move.
                elapsed_time = time.time() - car2_start_time # Calculate how long car 2 has been moving for.
                distance_moved = (elapsed_time / car2_duration) * car2_distance # Distance car 2 has moved.
                if distance_moved < car2_distance: # If distance moved is less than car 2 total distance.
                    car_canvas.coords(car2, distance_moved, 315) # Update car 2's position.
                    car2_update_id = root.after(car2_interval, update_car2) # Update car 2's position again after every interval.
                else: # Else.
                    car_canvas.coords(car2, car2_distance, 315) # Place car 2 at the end of the canvas.
                    end_time = time.time() # Record time taken when game is over.
                    elapsed_time = round(end_time - start_time, 2) # Time taken since the start of game.
                    display_lose_screen(elapsed_time) # Displays the losing screen.

        update_car2() # Calls on function to update car 2 movement.

    def display_lose_screen(elapsed_time): 
        """
        Displays the lose screen if user loses to the opponent.

        Args:
            elapsed_time: Time taken for user to finish the race game.

        Returns: None
        """
        questionLabel.grid_remove() # Remove the question labels from GUI.
        for widget in answer_frame.winfo_children(): # If any widgets in answer frame.
            if isinstance(widget, tk.Button): # If widget is a button.
                widget.grid_remove() # Remove buttons.

        timerLabel.grid_remove() # Remove the timer label from GUI.
        resultLabel.grid_remove()  # Remove the result label from GUI.

        lose_label = tk.Label(root, text="You Lose!", font=('arial', 40), fg="red", bg="#232323") # Displays the 'You Lose!' label on the GUI.
        lose_label.grid(row=1, column=0, pady=20, columnspan=2) # Positioning of the lose label.

        losing_text = tk.Label(root, text="The opponent reached the finish line before you", font=('arial', 24), fg="white", bg="black") # Displays the losing text with the losing label on GUI.
        losing_text.grid(row=2, column=0, pady=20, columnspan=2) # Positioning of the losing text.

        root.after_cancel(timer_update_id) # Stops the timer.   

    StartButton = tk.Button(root, text="Start Challenge", font=('arial', 15), width=71, command=start_game, bg="#444", fg="white") # Creates start button to begin the maths game.
    StartButton.grid(row=5, column=0, columnspan=2) # Positioning of the start button.

    bottom_frame = tk.Frame(root, bg='black') # Create frame for bottom button.
    bottom_frame.grid(row=7, column=0, pady=1, columnspan=2) # Position the frame on the grid.

    RestartButton = tk.Button(bottom_frame, text="Restart", font=('arial', 15), width=71, command=restart_game, bg="#444", fg="white") # Creates restart button to restart the maths game.
    RestartButton.grid(row=0, column=1, padx=2) # Positioning of the restart button.

    root.grid_columnconfigure(0, weight=1) # Allows column grid to expand and contract.
    root.grid_rowconfigure(0, weight=1) # Allows column row to expand and contract.

    root.mainloop() # Start the tkinter program.

if __name__ == "__main__": # Run if file program is ran directly.
    Login() # Calls on function to create the login page.
