import tkinter as tk

# Define the questions and their corresponding answers
questions = [
    {
        "question": "What is the capital city of Japan?",
        "options": ["Tokyo", "Kyoto", "Osaka", "Hiroshima"],
        "answer": "Tokyo"
    },
    {
        "question": "What is the highest mountain in the world?",
        "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount Denali"],
        "answer": "Mount Everest"
    },
    {
        "question": "What is the largest country in the world by land area?",
        "options": ["Russia", "Canada", "China", "USA"],
        "answer": "Russia"
    },
    {
        "question": "What is the currency of Brazil?",
        "options": ["Dollar", "Real", "Peso", "Euro"],
        "answer": "Real"
    },
    {
        "question": "What is the highest waterfall in the world?",
        "options": ["Angel Falls", "Niagara Falls", "Iguazu Falls", "Victoria Falls"],
        "answer": "Angel Falls"
    },
    {
        "question": "Which country is home to the Great Barrier Reef?",
        "options": ["Australia", "Thailand", "Mexico", "Brazil"],
        "answer": "Australia"
    },
    {
        "question": "Which river is the longest in the world?",
        "options": ["Nile", "Amazon", "Yangtze", "Mississippi"],
        "answer": "Nile"
    },
    {
        "question": "What is the smallest country in the world?",
        "options": ["Monaco", "San Marino", "Vatican City", "Liechtenstein"],
        "answer": "Vatican City"
    }
]

# Define the initial question index
current_question = 0

# Define a function to check the answer
def check_answer():
    global current_question
    selected_option = var.get()
    if selected_option == "":
        return
    if selected_option == questions[current_question]["answer"]:
        print("Correct!")
    else:
        print("Incorrect!")
    current_question += 1
    if current_question < len(questions):
        ask_question()
    else:
        print("Quiz completed!")

# Define a function to ask the current question
def ask_question():
    global current_question, var, radio_buttons, next_button
    question = questions[current_question]
    question_label.config(text=question["question"])
    var.set("")
    for i, option in enumerate(question["options"]):
        radio_buttons[i].config(text=option, value=option)
    next_button.config(state="disabled")
    
# Define a function to enable the next button
def enable_next_button(*args):
    next_button.config(state="normal")

# Define the main window
root = tk.Tk()
root.title("World Quiz")

# Define the widgets
question_label = tk.Label(root, text="", font=("Arial", 14))
var = tk.StringVar(value="")
var.trace("w", enable_next_button)
radio_buttons = []
for i in range(4):
    radio_button = tk.Radiobutton(root, text="", variable=var, value="", font=("Arial", 12))
    radio_buttons.append(radio_button)
next_button = tk.Button(root, text="Next", command=check_answer, font=("Arial", 12), state="disabled")

# Pack the widgets
question_label.pack(pady=20)
for radio_button in radio_buttons:
    radio_button.pack(pady=5)
next_button.pack(pady=20)

# Define a function to show the history
def show_history():
    history = ""
    for i, question in enumerate(questions):
        history += f"{i+1}. {question['question']} - {question['answer']}\n"
    history_window = tk.Toplevel(root)
    history_label = tk.Label(history_window, text=history, font=("Arial", 14))
    history_label.pack(padx=20, pady=20)

# Define the history button
history_button = tk.Button(root, text="Show History", command=show_history, font=("Arial", 12))

# Pack the history button
history_button.pack(pady=20)

# Define a function to restart the quiz
def restart_quiz():
    global current_question
    current_question = 0
    ask_question()
    restart_button.config(state="active")

# Define the restart button
restart_button = tk.Button(root, text="Restart", command=restart_quiz, font=("Arial", 12), state="active")

# Pack the restart button
restart_button.pack(pady=20)

# Ask the first question
ask_question()

# Start the main loop
root.mainloop()