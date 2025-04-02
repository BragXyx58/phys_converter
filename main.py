import tkinter as tk
from tkinter import ttk
import json

from baseConverter import BaseConverter


class UnitConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")

        self.current_theme = "light"

        self.converters = self.load_converters('converters.json')
        self.converter = BaseConverter(self.converters)

        self.selected_category = tk.StringVar(value = list(self.converters.keys())[0])
        self.units = list(self.converters[self.selected_category.get()].keys())

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.grid(row=0, column=0)

        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=0, column=1)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=1, column=0)

        self.category_combobox = ttk.Combobox(root, values=list(self.converters.keys()),
                                              textvariable=self.selected_category)
        self.category_combobox.grid(row=1, column=1)
        self.category_combobox.bind("<<ComboboxSelected>>", self.update_units)

        self.from_unit_label = tk.Label(root, text="From Unit:")
        self.from_unit_label.grid(row=2, column=0)

        self.from_unit_combobox = ttk.Combobox(root, values=self.units)
        self.from_unit_combobox.grid(row=2, column=1)

        self.to_unit_label = tk.Label(root, text="To Unit:")
        self.to_unit_label.grid(row=3, column=0)

        self.to_unit_combobox = ttk.Combobox(root, values=self.units)
        self.to_unit_combobox.grid(row=3, column=1)

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_units)
        self.convert_button.grid(row=4, column=0, columnspan=2)

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.grid(row=5, column=0)

        self.result_display = tk.Label(root, text="")
        self.result_display.grid(row=5, column=1)

    def load_converters(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def update_units(self, event=None):
        category = self.selected_category.get()
        self.units = list(self.converters[category].keys())
        self.from_unit_combobox['values'] = self.units
        self.to_unit_combobox['values'] = self.units

    def convert_units(self):
        try:
            amount = float(self.amount_entry.get())
            from_unit = self.from_unit_combobox.get()
            to_unit = self.to_unit_combobox.get()

            category = self.selected_category.get()

            result = self.converter.convert(from_unit, amount, to_unit, category)
            self.result_display.config(text=f"{result[to_unit]:.2f} {to_unit}")

        except ValueError:
            self.result_display.config(text="Invalid input")


root = tk.Tk()
app = UnitConverterGUI(root)
root.mainloop()