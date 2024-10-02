from tkinter import *
from tkinter import ttk
import math

window = Tk() # Основное окно приложения
window.geometry("200x250")
window.title("Калькулятор ИМТ")


gender_var = StringVar(value="М") # Переменная для сброва значений Radiobutton

intro = ttk.Label(text="Программа для вычисления ИМТ") # Шапка
intro.grid(row=0, column=0)

# Выбор пола
sex = ttk.Label(text="Ваш пол")
sex.grid(row=1, column=0)
man = ttk.Radiobutton(window, text="М", variable=gender_var, value="М")
man.grid(row=2, column=0)
woman = ttk.Radiobutton(window, text="Ж", variable=gender_var, value="Ж")
woman.grid(row=3, column=0)


# Ввод веса
weight_txt = ttk.Label(text="Введите ваш вес, в кг.:")
weight_txt.grid(row=4, column=0)
weight_etr = ttk.Entry()
weight_etr.grid(row=5, column=0)


# Ввод роста
height_txt = ttk.Label(text="Введите ваш рост, в см:")
height_txt.grid(row=6, column=0)
height_etr = ttk.Entry()
height_etr.grid(row=7, column=0)


def calculate():
    """Вычисление ИМТ"""
    weight = weight_etr.get()
    height = height_etr.get()
    try:
        result = float(weight) / (float(height) / 100) ** 2
        if result <= 18.5:
            result_la.config(text=f"Вам ИМТ: {result:.2f}\nНедостаточный вес")
        elif result >= 18.5 and result < 25:
            result_la.config(text=f"Вам ИМТ: {result:.2f}\nНормальный вес")
        elif result >= 25 and result <= 29.9:
            result_la.config(text=f"Вам ИМТ: {result:.2f}\nИзбыточный вес")
        else:
            result_la.config(text=f"Вам ИМТ: {result:.2f}\nОжирение")
    except:
        result_la.config(text="Ошибка!")

# Кнопка запуска расчетов
submit_button = ttk.Button(text="Рассчитать", command=calculate)
submit_button.grid(row=8, column=0)


result_la = ttk.Label(text="", font=("Helvetica", 14), foreground="black")
result_la.grid(row=9, column=0, columnspan=2, pady=10)

window.mainloop()