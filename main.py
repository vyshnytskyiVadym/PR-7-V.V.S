import tkinter as tk
from tkinter import messagebox

# Імпортування класу Processor з лабораторної роботи №4 та №5
class Processor:
    def __init__(self, brand, model, architecture, frequency, cores, cache, socket):
        self.brand = brand
        self.model = model
        self.architecture = architecture
        self.frequency = frequency  # GHz
        self.cores = cores
        self.cache = cache  # MB
        self.socket = socket

    def overclock(self, increase):
        self.frequency += increase
        print(f"The processor frequency has been increased to {self.frequency} GHz.")

# Створення основного вікна застосунку
class ProcessorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Processor Information")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for Processor attributes
        self.label_brand = tk.Label(self, text="Brand")
        self.label_brand.pack()
        self.entry_brand = tk.Entry(self)
        self.entry_brand.pack()

        self.label_model = tk.Label(self, text="Model")
        self.label_model.pack()
        self.entry_model = tk.Entry(self)
        self.entry_model.pack()

        self.label_architecture = tk.Label(self, text="Architecture")
        self.label_architecture.pack()
        self.entry_architecture = tk.Entry(self)
        self.entry_architecture.pack()

        self.label_frequency = tk.Label(self, text="Frequency (GHz)")
        self.label_frequency.pack()
        self.entry_frequency = tk.Entry(self)
        self.entry_frequency.pack()

        self.label_cores = tk.Label(self, text="Cores")
        self.label_cores.pack()
        self.entry_cores = tk.Entry(self)
        self.entry_cores.pack()

        self.label_cache = tk.Label(self, text="Cache (MB)")
        self.label_cache.pack()
        self.entry_cache = tk.Entry(self)
        self.entry_cache.pack()

        self.label_socket = tk.Label(self, text="Socket")
        self.label_socket.pack()
        self.entry_socket = tk.Entry(self)
        self.entry_socket.pack()

        # Button to create processor object
        self.button_create = tk.Button(self, text="Create Processor", command=self.create_processor)
        self.button_create.pack()

        # Label to display processor information
        self.label_info = tk.Label(self, text="")
        self.label_info.pack()

        # Entry and Button for overclocking
        self.label_overclock = tk.Label(self, text="Overclock Amount (GHz)")
        self.label_overclock.pack()
        self.entry_overclock = tk.Entry(self)
        self.entry_overclock.pack()

        self.button_overclock = tk.Button(self, text="Overclock", command=self.overclock_processor)
        self.button_overclock.pack()

    def create_processor(self):
        brand = self.entry_brand.get()
        model = self.entry_model.get()
        architecture = self.entry_architecture.get()
        frequency = float(self.entry_frequency.get())
        cores = int(self.entry_cores.get())
        cache = float(self.entry_cache.get())
        socket = self.entry_socket.get()

        self.processor = Processor(brand, model, architecture, frequency, cores, cache, socket)

        info = (f"Processor Information:\n"
                f"Brand: {self.processor.brand}\n"
                f"Model: {self.processor.model}\n"
                f"Architecture: {self.processor.architecture}\n"
                f"Frequency: {self.processor.frequency} GHz\n"
                f"Cores: {self.processor.cores}\n"
                f"Cache: {self.processor.cache} MB\n"
                f"Socket: {self.processor.socket}")

        self.label_info.config(text=info)

    def overclock_processor(self):
        if hasattr(self, 'processor'):
            increase = float(self.entry_overclock.get())
            self.processor.overclock(increase)
            self.create_processor()  # Update the displayed information
        else:
            messagebox.showerror("Error", "No processor created yet!")

if __name__ == "__main__":
    app = ProcessorApp()
    app.mainloop()
