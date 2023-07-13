import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack(pady = 10, padx = 10)

button1 = tk.Button(frame, text = "Button 1")
button1.grid(row = 0, column = 0, padx = 5, pady = 5)

button2 = tk.Button(frame, text = "Button 2")
button2.grid(row = 0, column = 1, padx = 5, pady = 5)

button3 = tk.Button(frame, text = "Button 3")
button3.grid(row = 1, column = 0, padx = 5, pady = 5)

button4 = tk.Button(frame, text = "Button 4")
button4.grid(row = 1, column = 1, padx = 5, pady = 5)

root.mainloop()