str = '''                       _ _                     _      __            _             
                      | | |                   | |    / _|          | |            
__      _____  _ __ __| | |__   ___  _ __ ___ | |__ | |_ _   _  ___| | _____ _ __ 
\ \ /\ / / _ \| '__/ _` | '_ \ / _ \| '_ ` _ \| '_ \|  _| | | |/ __| |/ / _ \ '__|
 \ V  V / (_) | | | (_| | |_) | (_) | | | | | | |_) | | | |_| | (__|   <  __/ |   
  \_/\_/ \___/|_|  \__,_|_.__/ \___/|_| |_| |_|_.__/|_|  \__,_|\___|_|\_\___|_|   '''
                                                                                  
print(str) # printing credits
print("\nMade by @isarsindri") # printing credits
print("github.com/isarsindri") # printing credits


import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

class ResultWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("WordbombFucker")

        # Create and place the input box
        self.new_word_entry = tk.Entry(self.master, width=30)
        self.new_word_entry.pack(pady=10)

        self.new_word_entry.bind('<Return>', lambda event: self.sort_new_words())

        self.result_text = scrolledtext.ScrolledText(self.master, width=70, height=20, wrap=tk.WORD)
        self.result_text.pack(expand=True, fill=tk.BOTH)

        self.result_text.configure(font=("Arial", 15))

        # Show the unsorted word list by default
        self.update_content(sort_words(""))

    def update_content(self, sorted_words):
        self.result_text.delete(1.0, tk.END)
        for word in sorted_words:
            self.result_text.insert(tk.END, f"{word} ({len(word)} letters)\n")

    def sort_new_words(self, event=None):
        new_word = self.new_word_entry.get().strip()
        if not new_word:
            messagebox.showinfo("Error", "Please enter a letter combination")
            return

        existing_sorted_words = self.result_text.get(1.0, tk.END).strip().split('\n')
        existing_sorted_words = [word.split(' ')[0] for word in existing_sorted_words]
        all_words = existing_sorted_words + [new_word]
        updated_sorted_words = sorted(all_words, key=lambda x: (len(x), x), reverse=True)
        self.update_content(updated_sorted_words)


def sort_words(input_text):
    with open('word_list.txt', 'r') as file:
        words = [word.strip() for word in file.readlines()]

    filtered_words = [word for word in words if input_text.lower() in word.lower()]

    return sorted(filtered_words, key=lambda x: (len(x), x), reverse=True)


def show_word_list(event=None):
    result_window.update_content(sort_words(result_window.new_word_entry.get()))


# Creating the main window
window = tk.Tk()
window.title("WordbombFucker") #window title
window.configure(bg='white') # window background
window.geometry("600x630")  # window size

# Create and place the button to trigger the word-finding
button = tk.Button(window, text="Find Words", command=show_word_list)
button.pack(pady=10)

# Creating an instance of the ResultWindow class
result_window = ResultWindow(window)

extra_label = tk.Label(window, text="github.com/isarsindri", font=("Georgia", 20), bg='white') # extra label for credit
extra_label.pack(pady=5)

extra_label2 = tk.Label(window, text="https://discord.gg/WFc3gKDGxB", font=("Georgia, 10"), bg='white') # extra label for discord server
extra_label2.pack(pady=5)

window.bind('<Return>', lambda event: show_word_list()) # Binding the return bind to tthe window and the event show_word_list

# Starting the Tkinter main loop
window.mainloop()
