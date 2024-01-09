# import tkinter as tk

# class ScheduleEditor:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Editeur d'emploi du temps")

#         self.schedule = {
#             "Lundi": ["8-12 Uhr", "14-16 Uhr"],
#             "Mardi": ["8-12 Uhr", "14-16 Uhr"],
#             "Mercredi": ["8-12 Uhr", "14-16 Uhr"],
#             "Jeudi": ["8-12 Uhr", "14-16 Uhr"],
#             "Vendredi": ["8-12 Uhr", "14-16 Uhr"]
#         }

#         self.frame = tk.Frame(self.root)
#         self.frame.pack(padx=20, pady=20)

#         tk.Label(self.frame, text="Mo-Fr: 8-12 Uhr und 14-16 Uhr", font=("Arial", 12, "bold")).pack()

#         # Affichage des plages horaires actuelles
#         self.display_schedule()

#         # Bouton pour ouvrir l'éditeur
#         edit_button = tk.Button(self.frame, text="Modifier", command=self.open_editor)
#         edit_button.pack(pady=10)

#     def display_schedule(self):
#         for day, hours in self.schedule.items():
#             label_text = f"{day}: {hours[0]} and {hours[1]}"
#             tk.Label(self.frame, text=label_text).pack()

#     def open_editor(self):
#         editor_window = tk.Toplevel(self.root)
#         editor_window.title("Editeur de plages horaires")

#         for day, hours in self.schedule.items():
#             tk.Label(editor_window, text=day).grid(row=list(self.schedule.keys()).index(day), column=0)
#             for i in range(2):
#                 entry = tk.Entry(editor_window)
#                 entry.insert(0, hours[i])
#                 entry.grid(row=list(self.schedule.keys()).index(day), column=i+1)

#         save_button = tk.Button(editor_window, text="Enregistrer", command=lambda: self.save_editor(editor_window))
#         save_button.grid(row=len(self.schedule), columnspan=3)

#     def save_editor(self, editor_window):
#         for day, row in zip(self.schedule, range(len(self.schedule))):
#             updated_hours = [editor_window.grid_slaves(row=row, column=col+1)[0].get() for col in range(2)]
#             self.schedule[day] = updated_hours

#         editor_window.destroy()
#         self.frame.destroy()
#         self.frame = tk.Frame(self.root)
#         self.frame.pack(padx=20, pady=20)
#         tk.Label(self.frame, text="Mo-Fr: 8-12 Uhr und 14-16 Uhr", font=("Arial", 12, "bold")).pack()
#         self.display_schedule()

# # Création de la fenêtre principale et lancement de l'application
# root = tk.Tk()
# app = ScheduleEditor(root)
# root.mainloop()


import tkinter as tk

class IhreKlasse:
    def set_behandlungzeit(self):
        new_window1 = tk.Toplevel()
        new_window1.title("Behandlungszeit Ändern")
        new_window1.geometry("400x300")
        new_window1.config(background="#3B6064")

        titel_label = tk.Label(new_window1, text='Bitte geben Sie die Behandlungszeit ein!!', font=("Arial", 15, "bold"), background="#3B6064", fg='white')
        titel_label.pack(pady=20)

        Label1 = tk.Label(new_window1, text='Morgen', font=("Arial", 12), background="#3B6064", fg='white')
        Label1.place(x=60, y=80)
        self.Entry1 = tk.Entry(new_window1, width=15, font=("Arial", 15))
        self.Entry1.place(x=150, y=80)

        Label2 = tk.Label(new_window1, text='Nachmittag', font=("Arial", 12), background="#3B6064", fg='white')
        Label2.place(x=60, y=130)
        self.Entry2 = tk.Entry(new_window1, width=15, font=("Arial", 15))
        self.Entry2.place(x=150, y=130)

        submit = tk.Button(new_window1, text='Änderung speichern', command=self.submit, width=17, height=2)
        submit.place(x=170, y=180)

        self.Entry1.bind('<FocusIn>', self.on_focusin)
        self.Entry1.bind('<FocusOut>', self.on_focusout)
        self.Entry2.bind('<FocusIn>', self.on_focusin)
        self.Entry2.bind('<FocusOut>', self.on_focusout)

    def submit(self):
        print("ok")

    def on_entry_click(self, event):
        if event.widget.get() == 'Entrez votre texte':
            event.widget.delete(0, tk.END)
            event.widget.config(fg="black")  # Changer la couleur du texte lorsqu'il est saisi

    def on_focusin(self, event):
        event.widget.config(bg="#D9D9D9")  # Changer la couleur de fond lorsqu'il obtient le focus

    def on_focusout(self, event):
        if event.widget.get() == '':
            event.widget.insert(0, 'Entrez votre texte')
            event.widget.config(bg="white")  # Revenir à la couleur de fond d'origine

# Usage
obj = IhreKlasse()
obj.set_behandlungzeit()
