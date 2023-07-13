##############################################
#  Autor: Theodore Noubissi Kala
#
#  Aufgabe: Grafische Oberfläsche für Zahnartz
##############################################

import tkinter as tk
import pandas as pd
import openpyxl
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from PIL import ImageTk, Image, Image


class LoginWindow(tk.Tk):
    def __init__(self): # Funktion für die LoginWindow-Klasse initialisieren
        super().__init__()
        self.title("Anmeldung")
        self.config(background="#3B6064")

        # Login Seite
        login_Frame = tk.Frame(background="#5B949A", width=450, height= 850)
        login_Frame.pack(pady=60, padx=60)

        Login_label = tk.Label(login_Frame, background="#5B949A", text="Log in", fg="white", font=("Arial", 23))
        Login_label.place(x=170, y=35)


        # Benutzername-Etikett und Eingabefeld
        username_label = tk.Label(login_Frame, text="Name", background="#5B949A", fg="white", font=("Arial", 15))
        username_label.place(x= 70, y=120, height=36)
        password_label = tk.Label(login_Frame, text="Passwort", background="#5B949A", fg="white", font=("Arial", 15))
        password_label.place(x= 70, y=180, height=36)


        self.username_entry = tk.Entry(login_Frame, background="white", fg="black", font=("Arial", 13))
        self.username_entry.place(x= 190, y=120, height=36, width=180)
        self.password_entry = tk.Entry(login_Frame, background="white", fg="black", show="*", font=("Arial", 13))
        self.password_entry.place(x= 190, y=180, height=36, width=182) 

        # Anmeldebutton und Registrierungsbutton
        login_button = tk.Button(login_Frame, text="Login", width= 41, height= 2, background="#3B6064", fg="white", command=self.login)   # TODO: command=self.login implementieren 
        login_button.place(x=70, y=260)        
        arzt_regist_button = tk.Button(login_Frame, text="Patient sign Up", width= 17, height= 2, background="#3B6064", fg="white")   # TODO: command=self.open_new_window_Patient_regist implementieren 
        arzt_regist_button.place(x=70, y=320)        
        patient_regist_button = tk.Button(login_Frame, text="Artz sign Up", width= 17, height= 2, background="#3B6064", fg="white")   # TODO: command=self.open_new_window_Arzt_regist implementieren 
        patient_regist_button.place(x=237, y=320)        


    def login(self):
        password = None

        # Ärzten Database
        db = pd.read_excel("Database/Patienten_Zahnärzte_Kosten.xlsx", sheet_name="Zahnärzte", header=None)
        full_names = db.iloc[3:80, 1].values.tolist()
        last_names = [name.split()[-1] for name in full_names]
        passwords = db.iloc[3:80, 2].values.tolist()

        global username
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in last_names and password in passwords:
            index1 = last_names.index(username)
            role1 = db.iloc[3+index1, 3]
            self.open_dentist_view(username)
        elif username == "a" and password == "a":
            self.open_dentist_view(username)
        # elif username in last_names2 and password in passwords2:
        #     index2 = last_names2.index(username)  # Obtenir l'index correspondant au nom d'utilisateur    # <----------------
        #     role2 = role = db2.iloc[3+index2, 3]                                      # <----------------
        #     self.open_patient_view(username)  # Übergeben der Patienten-ID -------- db2
        else:
            messagebox.showerror("Fehler", "Ungultige Anmeldeinformationen")
    

    def open_dentist_view(self, last_names):
        self.withdraw()
        # self.iconify()

        dentist_view = DentistView(self, last_names)
        dentist_view.mainloop()


class DentistView(tk.Toplevel):
    def __init__(self, master, last_names):
        super().__init__(master)
        self.geometry("1300x580")
        self.minsize(1300, 580)
        self.maxsize(1300, 580)
        self.title("Zahnarztansicht")
        self.config(background="#3B6064")
        self.last_names2 = last_names


        untersten_Frame = tk.Frame(self, width=1300, height=30, background="#5B949A")
        untersten_Frame.pack(side="bottom", fill="y")
        
        self.firma_name_label = tk.Label(untersten_Frame, text="Zahnärzte am Park GmbH", background="#5B949A", fg="white", font=("Arial", 11, "bold"))
        # firma_name_label.pack(side="left", fill="x")
        self.firma_name_label.place(x=15, y=5)
        self.animate_label()  # Animation starten

        self.current_time_label = tk.Label(untersten_Frame, text="", font=("Arial", 11, "bold"), fg="white", bg="#5B949A")
        self.current_time_label.place(x=1150, y=5)

        self.NameLabel = tk.Label(untersten_Frame, text= username, font=("Arial", 11, "bold"), background="#5B949A", fg="white")
        self.NameLabel.place(x=600, y=5)

        self.termin_Frame = tk.LabelFrame(self, text="Terminkalender",border=0, background="white")
        self.termin_Frame.place(x=7, y=7)

        columns=("Patientname", "Behandlungen", "Gebugte Zeit")
        self.treeview_gebu_Termin = ttk.Treeview(self.termin_Frame, columns= columns, height=11, show='headings')
        self.treeview_gebu_Termin.pack()

        # Überschrift für den Treeview festlegen
        self.treeview_gebu_Termin.heading("Patientname", text="Patientname", anchor='center')
        self.treeview_gebu_Termin.heading("Behandlungen", text="Behandlungen", anchor='center')
        self.treeview_gebu_Termin.heading("Gebugte Zeit", text="Gebugte Zeit", anchor='center')

        self.treeview_gebu_Termin.column("Patientname", width=250)
        self.treeview_gebu_Termin.column("Behandlungen", width=250)
        self.treeview_gebu_Termin.column("Gebugte Zeit", width=250)

        self.imageView_frame = tk.Frame(self, height=260, width=530)
        self.imageView_frame.place(x=765, y=7)

        # Zielgröße für das redimensionierte Bild
        self.width = 530
        self.height = 260
        # Liste der Bildpfade
        self.image_paths = ["Bilder/img1.jpg", "Bilder/img2.jpg", "Bilder/img3.jpg", "Bilder/img4.jpg", "Bilder/img5.jpg"]

        self.current_image_index = 0  # Index des aktuellen Bildes

        # Hintergrundbild laden und redimensionieren
        image = Image.open(self.image_paths[self.current_image_index])
        image = image.resize((self.width, self.height), Image.LANCZOS)

        # Redimensioniertes Hintergrundbild in ein Tkinter-Bildobjekt konvertieren
        self.background_image = ImageTk.PhotoImage(image)

        # Hintergrundbild-Label erstellen und platzieren
        self.background_label = tk.Label(self.imageView_frame, image=self.background_image)
        self.background_label.pack()

        # OPtionen (Button)
        self.optionFrame1 = tk.Frame(self, width=351, height=256, bg="#3B6064", highlightbackground="#5B949A", highlightthickness=0.5)
        self.optionFrame1.place(x=765, y=278)
        #----------------------------
        self.logout_button = tk.Button(self.optionFrame1, text="Krankenkasse\nändern", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=18, y=25)
        self.logout_button = tk.Button(self.optionFrame1, text="Behandlungszeit\nändern", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=197, y=25)
        self.logout_button = tk.Button(self.optionFrame1, text="Einstellung", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=18, y=83.5)
        self.logout_button = tk.Button(self.optionFrame1, text="Einstellung", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=197, y=83.5)
        self.logout_button = tk.Button(self.optionFrame1, text="Einstellung", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=18, y=140)
        self.logout_button = tk.Button(self.optionFrame1, text="Einstellung", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=18, y=140)
        self.logout_button = tk.Button(self.optionFrame1, text="Einstellung", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=197, y=140)
        self.logout_button = tk.Button(self.optionFrame1, text="Einstellung", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=18, y=200)
        self.logout_button = tk.Button(self.optionFrame1, text="Einstellung", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=197, y=200)
        #----------------------------
        #----------------------------
        self.optionFrame2 = tk.Frame(self, width=170, height=256, bg="#3B6064", highlightbackground="#5B949A", highlightthickness=0.5)
        self.optionFrame2.place(x=1126, y=278)
        #----------------------------
        self.logout_button = tk.Button(self.optionFrame2, text="Passwort ändern", width=18, height=2, font=("Arial", 9, "bold"))
        self.logout_button.place(x=18, y=25)
        #----------------------------
        self.Hintergrung_button = tk.Button(self.optionFrame2, text="Hintergrung", width=18, height=2, font=("Arial", 9, "bold"))
        self.Hintergrung_button.place(x=18, y=83.2)
        #----------------------------
        self.Sprache_button = tk.Button(self.optionFrame2, text="Englisch/Deutsch", width=18, height=2, font=("Arial", 9, "bold"))
        self.Sprache_button.place(x=18, y=140)
        #----------------------------
        self.logout_button = tk.Button(self.optionFrame2, text="Auslogen", command=self.logout, width=16, height=2, background="#E36370", fg="white", font=("Arial", 10, "bold"))
        self.logout_button.place(x=18, y=200)

        self.update_image()  # Bildwechsel starten
        self.update_time()  # Time Update


    # Funktion zum Aktualisieren des Bildes
    def update_image(self):
        # Nächsten Bildindex berechnen
        self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)

        # Bild laden und anzeigen
        image = Image.open(self.image_paths[self.current_image_index])
        image = image.resize((self.width, self.height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.background_label.config(image=photo)
        self.background_label.image = photo  # Referenz behalten, um das Bild im Speicher zu halten

        # Timer für das nächste Bild setzen (nach 4 Sekunden)
        self.after(3000, self.update_image)


    def update_time(self):
        current_datetime = datetime.now()
        current_time = datetime.now().strftime("%H:%M:%S")  # Aktuelle Uhrzeit abrufen
        current_date = current_datetime.strftime("%d.%m.%Y")  # Aktuelles Datum abrufen
        self.current_time_label.config(text=current_time)  # Uhrzeit im Label aktualisieren

        datetime_text = f"{current_date} {current_time}"  # Kombinierten Text erstellen
        self.current_time_label.config(text=datetime_text)  # Text im Label aktualisieren

        self.current_time_label.after(1000, self.update_time)  # Nach 1000 Millisekunden erneut aufrufen


    def animate_label(self):
        current_fg = self.firma_name_label["foreground"]
        if current_fg == "white":
            self.firma_name_label["foreground"] = "black"
        else:
            self.firma_name_label["foreground"] = "white"
        self.firma_name_label.after(500, self.animate_label)  # Nach 500 Millisekunden erneut aufrufen


    def logout(self):
        self.destroy()
        self.master.deiconify()
        self.master.username_entry.delete(0, tk.END)
        self.master.password_entry.delete(0, tk.END)
  

# Hauptprogramm
if __name__ == "__main__":
    loginWindow = LoginWindow()
    loginWindow.geometry("550x500")
    loginWindow.maxsize(550, 550)
    loginWindow.minsize(550, 550)

    loginWindow.mainloop()
