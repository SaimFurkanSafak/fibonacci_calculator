import tkinter
from sympy import fibonacci
def fibonacci_calculate():
    n = int(n_entry.get())
    result = fibonacci(n)
    cevap_label.config(text= f"{n}. fibonacci elemanı {result}")
window = tkinter.Tk()
window.title("Fibonacci Finder")
window.geometry("200x200")
n_label = tkinter.Label(window, text="Enter a number x<100")
n_label.pack()

n_entry = tkinter.Entry(window)
n_entry.pack()
bos_label1 =tkinter.Label(text="")
bos_label1.pack()

bos_label2 =tkinter.Label(text="")
bos_label2.pack()

calculate_button = tkinter.Button(window, text="Calculate", command=fibonacci_calculate)
calculate_button.pack()

bos_label3 =tkinter.Label(text="")
bos_label3.pack()

cevap_label = tkinter.Label(text=" ")
cevap_label.pack()

window.mainloop()