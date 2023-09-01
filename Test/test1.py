import tkinter as tk

class Terminkalender(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Terminkalender")
        self.geometry("400x300")

        self.selected_label = None  # Variable zur Verfolgung des ausgewählten Labels
        self.create_calendar()

    def create_calendar(self):
        # Überschrift
        header_label = tk.Label(self, text="Terminkalender", font=("Helvetica", 16))
        header_label.pack(pady=10)

        # Tabelle für Stunden und Tage
        auswahl_Frame2 = tk.LabelFrame(self, text="", width=527.5, height=237, background="white")
        auswahl_Frame2.place(rely=0.5325, relx=0.186)

        calendar_frame = tk.Frame(auswahl_Frame2)  # Parent Frame ist nun auswahl_Frame2
        calendar_frame.pack()

        # Liste mit Stunden (8-12 und 14-16 Uhr)
        hours = [str(i) + ":00" for i in range(8, 13)] + [str(i) + ":00" for i in range(14, 17)]

        # Liste mit Wochentagen (Montag bis Freitag)
        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]

        # Labels für Stunden und Wochentage erstellen
        for day in days:
            day_label = tk.Label(calendar_frame, text=day, width=10, borderwidth=1, relief="solid")
            day_label.grid(row=0, column=days.index(day) + 1, padx=5, pady=5)

        for i, hour in enumerate(hours):
            hour_label = tk.Label(calendar_frame, text=hour, width=10, borderwidth=1, relief="solid")
            hour_label.grid(row=i + 1, column=0, padx=5, pady=5)

            for day in days:
                # Überprüfen, ob die Stunde in den erlaubten Zeiträumen liegt
                if (8 <= int(hour.split(":")[0]) <= 12) or (14 <= int(hour.split(":")[0]) <= 16):
                    # Hinzufügen der Einträge für jede Stunde und jeden Wochentag
                    entry_label = tk.Label(calendar_frame, text="", width=10, borderwidth=1, relief="solid")
                    entry_label.grid(row=i + 1, column=days.index(day) + 1, padx=5, pady=5)

                    # Hinzufügen eines Event-Handlers für die Labels
                    entry_label.bind("<Button-1>", lambda event, label=entry_label, day=day, hour=hour: self.select_entry(label, day, hour))

    def select_entry(self, label, day, hour):
        # Überprüfen, ob das Label bereits ausgewählt wurde
        if self.selected_label == label:
            # Wenn das Label bereits ausgewählt ist, wird der rote Hintergrund entfernt und der Text gelöscht
            label.configure(background="white", text="")
            self.selected_label = None
        else:
            # Wenn das Label noch nicht ausgewählt ist, wird es als ausgewählt markiert und der Text aktualisiert
            if self.selected_label:
                self.selected_label.configure(background="white", text="")  # Vorheriges Label zurücksetzen
            label.configure(background="red", text=f"{day}\n{hour}")
            self.selected_label = label

if __name__ == "__main__":
    app = Terminkalender()
    app.mainloop()
