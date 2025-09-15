from tkinter import messagebox
from fastf1.plotting import get_driver_color, get_driver_style
from matplotlib import pyplot as plt
import fastf1.plotting
import tkinter as tk
from tkinter import simpledialog
import os


# Создать папку кэша
cache_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'cache')
os.makedirs(cache_dir, exist_ok=True)

# Включить кэш
fastf1.Cache.enable_cache(cache_dir)

fastf1.plotting.setup_mpl(color_scheme='fastf1')

# Создаем окно для ввода данных
root = tk.Tk()
root.withdraw()  # Скрываем основное окно

while True:

    try:
        year = simpledialog.askinteger("Input", "Enter Year Of GP:", parent=root, minvalue=2018, maxvalue=2025)
        if year is None:  # Пользователь нажал Cancel
            break
        gp = simpledialog.askstring("Input", "Enter Country Or Number Of GP:")
        if gp is None:  # Пользователь нажал Cancel
            break
        s = simpledialog.askstring("Input", "Enter Type Of Session (Free Practice, Qualification or Race):")
        if s is None:  # Пользователь нажал Cancel
            break
        driver1 = simpledialog.askstring("Input", "Enter First Driver's Identifier:", parent=root)
        if driver1 is None:  # Пользователь нажал Cancel
            break
        driver2 = simpledialog.askstring("Input", "Enter Second Driver's Identifier:", parent=root)
        if driver2 is None:  # Пользователь нажал Cancel
            break

        session = fastf1.get_session(year, gp, s)

        messagebox.showinfo("Загрузка", "Данные загружаются, подождите...")

        session.load()

        fast_d1 = session.laps.pick_driver(driver1).pick_fastest()
        fast_d2 = session.laps.pick_driver(driver2).pick_fastest()
        if fast_d1.empty:
            messagebox.showerror("Ошибка", f"Данные для {driver1} не найдены!")
            continue
        if fast_d2.empty:
            messagebox.showerror("Ошибка", f"Данные для {driver2} не найдены!")
            continue
        d1_car_data = fast_d1.get_car_data()
        d2_car_data = fast_d2.get_car_data()
        t = d1_car_data["Time"]
        tp = d2_car_data["Time"]
        vCar = d1_car_data["Speed"]
        vCarp= d2_car_data["Speed"]

        fig, ax = plt.subplots(figsize=(12, 8))  # Вместо (10, 6)
        ax.plot(t, vCar, label=[driver1], **get_driver_style(identifier=driver1, style=["color", "linestyle"], session=session))
        ax.plot(tp, vCarp, label=[driver2], **get_driver_style(identifier=driver2, style=["color", "linestyle"], session=session))
        ax.set_title(f"Сравнение: {driver1} vs {driver2}\n{s} сессия, {gp} {year}",
                     fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)  # Полупрозрачная сетка
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Speed (km/h)")
        ax.legend(fontsize=11)
        plt.show()

        continue_program = messagebox.askyesno("Continue", "Compare other drivers?")
        if not continue_program:
            break
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
        continue_program = messagebox.askyesno("Ошибка", "Хотите попробовать снова?")
        if not continue_program:
            break
