import tkinter as tk
from tkinter import messagebox

class CalculatorLogic:
    def __init__(self, display):
        self.display = 
    
    def on_button_click(self, char):
        current_text = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current_text + char)

    def calculate(self):
        try:
            result = str(eval(self.display.get()))  # Evaluate the expression entered
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")

    def clear_display(self):
        self.display.delete(0, tk.END)
