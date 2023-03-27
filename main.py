import tkinter as tk

# Define the questions and their respective answers
questions = {
    "What is the capital of France?": ["Paris", "London", "Madrid", "Berlin"],
    "What is the currency of Japan?": ["Yen", "Dollar", "Euro", "Pound"],
    "What is the largest country in the world by area?": ["Russia", "Canada", "China", "USA"]
}

# Define the correct answers for each question
answers = {
    "What is the capital of France?": "Paris",
    "What is the currency of Japan?": "Yen",
    "What is the largest country in the world by area?": "Russia"
}

# Create the main window for the quiz
root = tk.Tk()
root.geometry("400x400")

# Create a label for the quiz title
title = tk.Label(root, text="World Quiz", font=("Arial", 24))
title.pack(pady=10)

# Create a label for the question and a variable to store the answer
question_label = tk.Label(root, font=("Arial", 16))
question_var = tk.StringVar()

# Create a list of answer buttons
answer_buttons = []

# Define a function to display the next question
def next_question():
    # Clear the previous question and answer buttons
    question_label.pack_forget()
    for button in answer_buttons:
        button.pack_forget()
    answer_buttons.clear()

    # Get the next question and its answer options
    question, options = next(iter(questions.items()))
    question_var.set(question)
    question_label.pack()

    # Create a button for each answer option
    for option in options:
        button = tk.Button(root, text=option, width=20, font=("Arial", 12),
                           command=lambda o=option: check_answer(o))
        answer_buttons.append(button)
        button.pack(pady=5)

# Define a function to check the selected answer
def check_answer(answer):
    # Get the current question and its correct answer
    question = question_var.get()
    correct_answer = answers[question]

    # Check if the selected answer is correct
    if answer == correct_answer:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect!")

# Create a label for the quiz result
result_label = tk.Label(root, font=("Arial", 16), fg="green")
result_label.pack(pady=10)

# Create a button to start the quiz
start_button = tk.Button(root, text="Start Quiz", width=20, font=("Arial", 12),
                         command=next_question)
start_button.pack(pady=20)

# Set the initial question label and answer buttons
question_label.config(textvariable=question_var)
for button in answer_buttons:
    button.pack(pady=5)

# Run the main loop
root.mainloop()