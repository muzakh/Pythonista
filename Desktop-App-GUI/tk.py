import tkinter as tk

def myFunc():
    print(entry.get())


if __name__ == '__main__':
    window = tk.Tk()
    window.title("My first TK Application")
    window.geometry('600x400')

    label = tk.Label(window, text="Hello World!", fg="green", bg="red", width=50)
    label.pack()
    
    #entry = tk.Entry(window, width=50, state=tk.DISABLED)
    entry = tk.Entry(window, width=50)
    entry.pack()
    entry.focus()

    button = tk.Button(window, text="Calculate", command=myFunc, fg="green", bg="red", activebackground="yellow", activeforeground="black")
    button.pack()


    window.mainloop()

