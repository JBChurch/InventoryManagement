import tkinter as tk

root = tk.Tk()
root.title('Inventory')
root.configure(background='#b8b6b6')


def submitted_window():

    root2 = tk.Tk()
    root2.title('Submitted.')

    submitted_label = tk.Label(root2, text='Submitted.', width=25)
    submitted_label.grid(row=0, column=0)

    ok_button = tk.Button(root2, text='Ok', command=root2.destroy)
    ok_button.grid(row=1, column=0)

    root2.mainloop()


def clear_entries():

    PC_manufacturer_entry.delete(0, 'end')
    PC_CPU_entry.delete(0, 'end')
    PC_drive_size_factor_entry.delete(0, 'end')
    PC_RAM_size_entry.delete(0, 'end')
    PC_price_entry.delete(0, 'end')


PC_manufacturer_label = tk.Label(root, text='Manufacturer', bg='#b8b6b6')
PC_manufacturer_label.grid(row=0, column=0)

PC_manufacturer_entry = tk.Entry(root, justify='center')
PC_manufacturer_entry.grid(row=0, column=1)

PC_CPU_label = tk.Label(root, text='CPU Specs', bg='#b8b6b6')
PC_CPU_label.grid(row=1, column=0)

PC_CPU_entry = tk.Entry(root, justify='center')
PC_CPU_entry.grid(row=1, column=1)

PC_drive_size_factor_label = tk.Label(root, text='Drive Size', bg='#b8b6b6')
PC_drive_size_factor_label.grid(row=2, column=0)

PC_drive_size_factor_entry = tk.Entry(root, justify='center')
PC_drive_size_factor_entry.grid(row=2, column=1)

PC_RAM_size_label = tk.Label(root, text='Amount of RAM', bg='#b8b6b6')
PC_RAM_size_label.grid(row=3, column=0)

PC_RAM_size_entry = tk.Entry(root, justify='center')
PC_RAM_size_entry.grid(row=3, column=1)

PC_price_label = tk.Label(root, text='Price', bg='#b8b6b6')
PC_price_label.grid(row=4, column=0)

PC_price_entry = tk.Entry(root, justify='center')
PC_price_entry.grid(row=4, column=1)

clear_button = tk.Button(root, text='Clear', pady=5, command=clear_entries)
clear_button.grid(row=5, column=0)

submit_button = tk.Button(root, text='Submit', pady=5, command=submitted_window)
submit_button.grid(row=5, column=1)


root.mainloop()
