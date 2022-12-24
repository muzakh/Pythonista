import tkinter as tk
import tkinter.ttk as ttk

def calc():
    value = float(feets.get())
    meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Feet to Meter")
    window.geometry("600x400")

    feets = tk.StringVar()
    meters = tk.StringVar()

    entry = ttk.Entry(window, textvariable=feets, width=10)
    entry.pack()
    entry.focus()

    label = ttk.Label(window, text="feets")
    label.pack()

    button = ttk.Button(window, text="Calculate", command=calc)
    button.pack()
    
    label_meter = ttk.Label(window, textvariable=meters)
    label_meter.pack()
    tk.Label(window, text="meters").pack()


    window.mainloop()




