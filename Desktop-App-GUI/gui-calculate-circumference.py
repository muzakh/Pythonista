
import tkinter as tk
import tkinter.ttk as ttk

class Circle():
    def __init__(self, radius):
        self.radius = radius
    def __str__(self):
        return "This is a class to print the circumference of a circle with given radius."     
    def circumference_calc(self):
        return (2 * 3.142 * self.radius)


def event():
    radius = tk_radius.get()
    circle = Circle(radius)
    tk_circumference.set(circle.circumference_calc())

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Circle Circumference")
    window.geometry("600x400")

    tk_radius = tk.DoubleVar()
    tk_circumference = tk.DoubleVar()

    entry = ttk.Entry(window, textvariable=tk_radius)
    entry.pack()
    entry.focus()

    ttk.Label(window, text="radius").pack()

    button = ttk.Button(window, text="Calculate", command=event).pack()

    ttk.Label(window, textvariable=tk_circumference).pack()
    ttk.Label(window, text="circumference").pack()


    window.mainloop()
