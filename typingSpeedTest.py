import tkinter as tk
from time import time
import random

texts = [
    "the quick brown fox jumps over the lazy do",
    "python is a versatile and powerful programming language",
    "typing speed tests are a fun way to improve speed"
]

class TypingspeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.sample_text = random.choice(texts)
        self.start_time = None

        self.label = tk.Label(root, text="Type the text below", font=("Arial", 20))
        self.label.pack(pady=10)

        self.text_label = tk.Label(root, text=self.sample_text, font=("Arial", 20))
        self.text_label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 20), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)
        self.entry.bind("<Return>", self.check_result)

        self.result_label = tk.Label(root, text="", font=("Arial", 20))
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time()

    def check_result(self, event):
        end_time = time()
        typed_text = self.entry.get()
        time_taken = end_time - self.start_time if self.start_time else 1
        typed_words = typed_text.split()
        sample_words = self.sample_text.split()
        
        correct_words = sum(1 for a, b in zip(typed_words, sample_words) if a == b)
        wpm = correct_words / (time_taken / 60) if time_taken > 0 else 0
        correct_chars = sum(1 for a, b in zip(typed_text, self.sample_text) if a == b)
        accuracy = (correct_chars / len(self.sample_text)) * 100 if self.sample_text else 0

        self.result_label.config(
            text=f"WPM: {wpm:.2f}\nAccuracy: {accuracy:.2f}%\nTime: {time_taken:.2f}s"
        )

    def reset(self):
        self.sample_text = random.choice(texts)
        self.text_label.config(text=self.sample_text)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None

root = tk.Tk()
app = TypingspeedTestApp(root)
root.mainloop()
