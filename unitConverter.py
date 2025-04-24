import tkinter as tk
from tkinter import ttk

def lengthConvert(fromUnit, toUnit, value):
    conversionUnits = {
        "meter": 1,
        "kilometer": 0.001,
        "inches": 39.3701,
        "feet": 3.28084
    }
    return value * conversionUnits[toUnit] / conversionUnits[fromUnit]

def convertUnit():
    try:
        value = float(entryValue.get())
        fromUnit = comboFrom.get()
        toUnit = comboTo.get()
        category = comboCategory.get()
        
        if category == "Length":
            result = lengthConvert(fromUnit, toUnit, value)
            labelResult.config(text=f"Result: {value} {fromUnit} = {result:.2f} {toUnit}")
        else:
            labelResult.config(text="Error: Unsupported category")
    except ValueError:
        labelResult.config(text="Put a valid number")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x400")
root.resizable(True, True)

labelCategory = tk.Label(root, text="Select Category")
labelCategory.pack(pady=5)
comboCategory = ttk.Combobox(root, values=['Length'], state="readonly")
comboCategory.current(0)
comboCategory.pack(pady=5)

labelFrom = tk.Label(root, text="Convert from:")
labelFrom.pack(pady=5)
comboFrom = ttk.Combobox(root, values=["meter", "kilometer", "inches", "feet"], state="readonly")
comboFrom.current(0)
comboFrom.pack(pady=5)

labelTo = tk.Label(root, text="Convert to:")
labelTo.pack(pady=5)
comboTo = ttk.Combobox(root, values=["meter", "kilometer", "inches", "feet"], state="readonly")
comboTo.current(0)
comboTo.pack(pady=5)

labelValue = tk.Label(root, text="Enter Value")
labelValue.pack(pady=5)
entryValue = tk.Entry(root)
entryValue.pack(pady=5)

buttonConvert = tk.Button(root, text='Convert', command=convertUnit)
buttonConvert.pack(pady=11)

labelResult = tk.Label(root, text="Result:", font=('Arial', 15))
labelResult.pack(pady=22)

root.mainloop()
