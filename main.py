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
    
# Define the main window
root = tk.Tk()
root.title("World Quiz")

# Define the widgets
question_label = tk.Label(root, text="", font=("Arial", 14))
var = tk.StringVar(value="")
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

# Ask the first question
ask_question()

# Start the main loop
root.mainloop()