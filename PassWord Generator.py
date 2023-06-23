
import random
import tkinter as tk

# Define the colors for the GUI
BG_COLOR = '#F2F2F2'
BUTTON_COLOR = '#4285F4'
TEXT_COLOR = '#333333'

# Define the function to generate the password
def generate_password():
    numbers = []
    symbols = ['%', '&', '(', ')', '*', '+','!', '#', '$']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    password = ''
    symbol_string = ''
    password_list = []

    number_choice = int(num_entry.get())
    number_symbols = int(symbol_entry.get())
    number_letters = int(letter_entry.get())
    password_length = number_choice + number_symbols + number_letters

    for x in range(number_symbols):
        symbol_string = symbol_string+symbols[random.randint(0, len(symbols)-1)]

    for x in range(number_choice):
        numbers.append(random.randint(0, 10))

    letter_counter = 0
    number_counter = 0
    symbol_counter = 0

    for x in range(number_letters):
        password_list.append(random.choice(letters))

    for x in range(number_choice):
        password_list.append(str(random.choice(numbers)))

    for x in range(number_symbols):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    for x in password_list:
        password = password + x

    password_label.config(text=password)


# Create the GUI window
root = tk.Tk()
root.title("EUAS Password Generator")
root.geometry("400x300")
root.configure(bg=BG_COLOR)

# Create the input fields and labels
num_label = tk.Label(root, text="Number of Numbers:", bg=BG_COLOR, fg=TEXT_COLOR)
num_label.pack(pady=10)

num_entry = tk.Entry(root, width=20, bg=BG_COLOR, fg=TEXT_COLOR)
num_entry.pack()

symbol_label = tk.Label(root, text="Number of Symbols:", bg=BG_COLOR, fg=TEXT_COLOR)
symbol_label.pack(pady=10)

symbol_entry = tk.Entry(root, width=20, bg=BG_COLOR, fg=TEXT_COLOR)
symbol_entry.pack()

letter_label = tk.Label(root, text="Number of Letters:", bg=BG_COLOR, fg=TEXT_COLOR)
letter_label.pack(pady=10)

letter_entry = tk.Entry(root, width=20, bg=BG_COLOR, fg=TEXT_COLOR)
letter_entry.pack()

# Create the generate button
generate_button = tk.Button(root, text="Generate Password", bg=BUTTON_COLOR, fg=BG_COLOR, command=generate_password)
generate_button.pack(pady=20)

# Create the label to display the generated password
password_label = tk.Label(root, text="", bg=BG_COLOR, fg=TEXT_COLOR, font=("Helvetica", 20))
password_label.pack(pady=10)


root.mainloop()
