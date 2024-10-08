import tkinter as tk
from logic import CalculatorLogic

class CalculatorUI:
    def __init__(self, root):
        self.root = root
        
        # Create a display widget for the calculator
        self.display = tk.Entry(self.root, font=("Arial", 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Create an instance of the logic handler
        self.logic = CalculatorLogic(self.display)
        
        # Create buttons for the calculator
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]
        
        row = 1
        col = 0

        for button in buttons:
            if button == "=":
                tk.Button(self.root, text=button, padx=20, pady=20, bd=5, font=("Arial", 18),
                          command=self.logic.calculate).grid(row=row, column=col, columnspan=2, sticky="nsew")
                col += 2
            elif button == "C":
                tk.Button(self.root, text=button, padx=20, pady=20, bd=5, font=("Arial", 18),
                          command=self.logic.clear_display).grid(row=row, column=col)
            else:
                tk.Button(self.root, text=button, padx=20, pady=20, bd=5, font=("Arial", 18),
                          command=lambda btn=button: self.logic.on_button_click(btn)).grid(row=row, column=col)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
