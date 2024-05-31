import tkinter as tk
from tkinter import messagebox

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
