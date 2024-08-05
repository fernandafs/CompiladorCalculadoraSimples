import tkinter as tk
from interpreter import interpret


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Simples")  # Define o título da janela
        self.geometry("400x600")  # Define o tamanho da janela
        self.expression = ""  # Inicializa a expressão matemática
        self.entry = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="solid")
        self.entry.pack(pady=10, padx=10, fill="both")
        self.create_buttons()  # Cria os botões da calculadora
        self.bind_keys()  # Associa eventos de teclado

    # Cria e organiza os botões da calculadora na interface gráfica
    def create_buttons(self):
        buttons_frame = tk.Frame(self)
        buttons_frame.pack(pady=10)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '(', ')', '+',
            '.', '^', 'C', '⌫',
            '='
        ]
        row = 0
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            b = tk.Button(buttons_frame, text=button, font=("Arial", 18), command=action)
            b.grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
            buttons_frame.grid_rowconfigure(i, weight=1)

    # Associa eventos de teclado aos métodos de manipulação
    def bind_keys(self):
        self.bind('<Key>', self.on_key_press)

    # Manipula a entrada de teclado para atualizar a expressão
    def on_key_press(self, event):
        key = event.keysym
        key_map = {
            'Return': '=',
            'BackSpace': '⌫',
            'Escape': 'C',
            'parenleft': '(',
            'parenright': ')',
            'period': '.',
            'slash': '/',
            'asterisk': '*',
            'plus': '+',
            'minus': '-',
            'numbersign': '#',
            'comma': ',',
            'space': ' ',
            'caret': '^'
        }
        if key in key_map:
            if event.char == '^':
                char = '^'
            elif event.keysym in key_map:
                char = key_map[event.keysym]
            else:
                char = event.char

            if char == '=':
                self.calculate()
            elif char == '⌫':
                self.backspace()
            elif char == 'C':
                self.clear()
            else:
                self.expression += char
        elif key in '0123456789':
            self.expression += key
        self.update_entry()

    # Manipula cliques em botões para atualizar a expressão
    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.clear()
        elif char == "⌫":
            self.backspace()
        else:
            self.expression += str(char)
        self.update_entry()

    # Calcula o resultado da expressão atual e atualiza a exibição
    def calculate(self):
        try:
            result = interpret(self.expression)
            self.expression = str(result)
        except Exception:
            self.expression = "Error"
        self.update_entry()

    # Limpa a expressão atual e a exibição
    def clear(self):
        self.expression = ""
        self.update_entry()

    # Remove o último caractere da expressão e atualiza a exibição
    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_entry()

    # Atualiza o campo de entrada com a expressão atual
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()  # Inicia o loop principal da interface gráfica
