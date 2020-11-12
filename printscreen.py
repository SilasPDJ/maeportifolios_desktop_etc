def executa():
    from time import sleep
    import pyautogui as pygui

    path = r'C:\Users\Silas\OneDrive\Mae_Area de Trabalho\_PRINTSCREEN_3ANO-2020\11-11'

    prossegue = True
    try:
        with open('counter', 'r') as file:
            valor = file.read()
    except FileNotFoundError:
        with open('counter', 'w') as file:
            file.write('1')
    else:
        with open('counter', 'w') as file:
            file.write(str(int(valor)+1))

        full_path = f'{path}\\print_{valor}.jpg'

        pygui.getActiveWindow().minimize()
        sleep(1)
        pygui.screenshot(full_path)


import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
button = tk.Button(frame,
                   text="TIRA PRINT AUTOMATICO",
                   fg="red",
                   command=executa)
button.pack(side=tk.LEFT)

root.mainloop()
