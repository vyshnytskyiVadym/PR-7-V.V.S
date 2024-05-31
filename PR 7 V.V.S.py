import tkinter as tk
from tkinter import messagebox


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Лабораторна робота №10")
        self.geometry("300x200")
        self.resizable(False, False)

        # Створення міток (Label)
        self.label_x1 = tk.Label(self, text="Змінна X1")
        self.label_x1.pack(pady=5)
        self.tbX1 = tk.Entry(self)
        self.tbX1.pack(pady=5)

        self.label_x2 = tk.Label(self, text="Змінна X2")
        self.label_x2.pack(pady=5)
        self.tbX2 = tk.Entry(self)
        self.tbX2.pack(pady=5)

        self.label_result = tk.Label(self, text="Результат розрахунку Y")
        self.label_result.pack(pady=5)
        self.tbY = tk.Entry(self, state='readonly')
        self.tbY.pack(pady=5)

        # Створення кнопок (Button)
        self.btnCalculate = tk.Button(self, text="Обчислити", command=self.calculate)
        self.btnCalculate.pack(side=tk.LEFT, padx=10, pady=10)

        self.btnClear = tk.Button(self, text="Очистити", command=self.clear)
        self.btnClear.pack(side=tk.LEFT, padx=10, pady=10)

        self.btnExit = tk.Button(self, text="Вихід", command=self.exit)
        self.btnExit.pack(side=tk.LEFT, padx=10, pady=10)

    def calculate(self):
        try:
            x1 = float(self.tbX1.get())
            x2 = float(self.tbX2.get())
            y = x1 * x2
            self.tbY.config(state='normal')
            self.tbY.delete(0, tk.END)
            self.tbY.insert(0, f'{y:.6f}')
            self.tbY.config(state='readonly')
        except ValueError:
            messagebox.showerror("Помилка", "Не введено даних!")

    def clear(self):
        self.tbX1.delete(0, tk.END)
        self.tbX2.delete(0, tk.END)
        self.tbY.config(state='normal')
        self.tbY.delete(0, tk.END)
        self.tbY.config(state='readonly')

    def exit(self):
        self.destroy()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
