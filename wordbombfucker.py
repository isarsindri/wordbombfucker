str = '''                       _ _                     _      __            _             
                      | | |                   | |    / _|          | |            
__      _____  _ __ __| | |__   ___  _ __ ___ | |__ | |_ _   _  ___| | _____ _ __ 
\ \ /\ / / _ \| '__/ _` | '_ \ / _ \| '_ ` _ \| '_ \|  _| | | |/ __| |/ / _ \ '__|
 \ V  V / (_) | | | (_| | |_) | (_) | | | | | | |_) | | | |_| | (__|   <  __/ |   
  \_/\_/ \___/|_|  \__,_|_.__/ \___/|_| |_| |_|_.__/|_|  \__,_|\___|_|\_\___|_|   '''
                                                                                  
print(str)
print("\nMade by @isarsindri")
print("https://github.com/isarsindri")
print("https://discord.gg/WFc3gKDGxB")

import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import time
from pynput.keyboard import Controller as KeyboardController
import keyboard

def sort_words(input_text):
    with open('word_list.txt', 'r') as file:
        words = [word.strip() for word in file.readlines()]

    filtered_words = [word for word in words if input_text.lower() in word.lower()]

    return sorted(filtered_words, key=lambda x: (len(x), x), reverse=True)

class ResultWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("WordbombFucker")

        # Creating and placing the text input box
        self.new_word_entry = tk.Entry(self.master, width=30)
        self.new_word_entry.pack(pady=10)

        self.new_word_entry.bind('<Return>', lambda event: self.sort_new_words())

        self.result_text = scrolledtext.ScrolledText(self.master, width=70, height=20, wrap=tk.WORD)
        self.result_text.pack(expand=True, fill=tk.BOTH)

        self.result_text.configure(font=("Arial", 15))

        # Show default word list 
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

    def autotype_word(self, key):
        sorted_words = self.result_text.get(1.0, tk.END).strip().split('\n')
        for word in sorted_words:
            if key == 'F1' and len(word.split(' ')[0]) == len(sorted_words[0].split(' ')[0]):
                autotype_word = word.split(' ')[0]
                break
        else:
            return

        keyboard = KeyboardController()

        # Setting the typing speed to 120 WPM
        words_per_minute = 120
        seconds_per_word = 60 / words_per_minute

        for char in autotype_word:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(seconds_per_word / len(autotype_word))

def show_word_list(event=None):
    result_window.update_content(sort_words(result_window.new_word_entry.get()))

# Creating the main window
window = tk.Tk()
window.title("WordbombFucker")
window.configure(bg='white')
window.geometry("600x680")  # Larger window size

# Creating and placing the button to trigger word finding
button = tk.Button(window, text="Find Words", command=show_word_list)
button.pack(pady=10)

# Creating an instance of the ResultWindow class
result_window = ResultWindow(window)

extra_label = tk.Label(window, text="github.com/isarsindri", font=("Georgia", 20), bg='white')
extra_label.pack(pady=5)

extra_label2 = tk.Label(window, text="https://discord.gg/WFc3gKDGxB", font=("Georgia, 10"), bg='white')
extra_label2.pack(pady=5)

window.bind('<Return>', lambda event: show_word_list())

keyboard.add_hotkey('F1', lambda: result_window.autotype_word('F1'))

# Start the main window loop
window.mainloop()
