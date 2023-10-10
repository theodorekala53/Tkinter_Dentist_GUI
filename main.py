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
from tkinter import Label, PhotoImage
from tkinter.ttk import Combobox
from tkinter.font import Font

#database für Ärzte (beim Login)
db = pd.read_excel("Database/Patienten_Zahnärzte_Kosten.xlsx", sheet_name="Zahnärzte", header=None)
db2 = pd.read_excel("Database/Patienten_Zahnärzte_Kosten.xlsx", sheet_name="Stamm-Patienten", header=None)


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
        arzt_regist_button = tk.Button(login_Frame, text="Patient sign Up", width= 17, height= 2, background="#3B6064", fg="white", command=self.open_new_window_Patient_regist)   # TODO: command=self.open_new_window_Patient_regist implementieren 
        arzt_regist_button.place(x=70, y=320)        
        patient_regist_button = tk.Button(login_Frame, text="Artz sign Up", width= 17, height= 2, background="#3B6064", fg="white", command = self.open_new_window_Arzt_regist)   # TODO: command=self.open_new_window_Arzt_regist implementieren 
        patient_regist_button.place(x=237, y=320)        

    def login(self):
        password = None

        # Ärzten Database
        full_names = db.iloc[3:80, 1].values.tolist()
        last_names = [name.split()[-1] for name in full_names]
        passwords = db.iloc[3:80, 2].values.tolist()

        #Patienten
        full_names2 = db2.iloc[4:61, 2].values.tolist()
        patient_names = [name.split()[-1] for name in full_names2]
        patient_passwords = db2.iloc[4:61, 3].values.tolist()

        global username
        global KrankenkasseArt
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in last_names and password in passwords:
            self.open_dentist_view(username)
        elif username == "a" and password == "a":
            self.open_dentist_view(username)
        elif username == "p" and password == "p":
            self.open_Patient_View(username)
        elif username in patient_names and password in patient_passwords:
            self.open_Patient_View(username) 
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

    def open_Patient_View(self, patient_names):
        self.withdraw()
        dentist_View = PatientView(self, patient_names)
        dentist_View.mainloop()

    def open_new_window_Arzt_regist(self):
        self.withdraw()  

        new_window = tk.Toplevel()
        new_window.title("Arzt Registrierung")
        new_window.geometry("700x450")
        new_window.config(background="#2A324B")

        # Variables
        self.name_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.problematik_var = tk.StringVar()
        self.dentist_var = tk.StringVar()
        self.teeth_var = tk.StringVar()
  

        name_Label = tk.Label(new_window, text="Name:", font=("Arial", 10, "bold"), fg="white", background="#2A324B")
        name_Label.place(rely=0.2, relx=0.09)
        name_Label_Entry = tk.Entry(new_window, textvariable=self.name_var)
        name_Label_Entry.place(rely=0.2, relx=0.29)

        passwort_Label = tk.Label(new_window, text="passwort:", font=("Arial", 10, "bold"), fg="white", background="#2A324B")
        passwort_Label.place(rely=0.3, relx=0.09)
        passwort_Label_Entry = tk.Entry(new_window, textvariable=self.password_var, show ='*')
        passwort_Label_Entry.place(rely=0.30, relx=0.29)
        
        Krankenkassenart_Label = tk.Label(new_window, text="Krankenkassenart:", font=("Arial", 10, "bold"), fg="white", background="#2A324B")
        Krankenkassenart_Label.place(rely=0.4, relx=0.09)
        krankenkassenarten = ["gesetzlich", "freiwillig gesetzlich", "privat"]
        self.krankenk_var = tk.StringVar(self)
        self.combobox2 = Combobox(new_window, values=krankenkassenarten, textvariable=self.krankenk_var, width=24)  # Bind the selection event
        self.combobox2.current(0)  # Set the default selection
        self.combobox2.place(rely=0.4, relx=0.29)

        # register_button = tk.Button(new_window, text="Register", font=("Arial", 11, "bold"), command=self.save_data)
        self.register_button = tk.Button(new_window, text="Registrieren", font=("Arial", 11, "bold"), command=self.save_data)
        self.register_button.place(rely=0.55, relx=0.19)

        self.Auslogen_button = tk.Button(new_window, text="Zurück",command=self.logout, width=25, bg="#DE5466", fg="white", font=("Arial", 9, "bold"))
        self.Auslogen_button.pack(side="bottom", pady=7)

        name_Label_Entry.delete(0, tk.END)
        passwort_Label_Entry.delete(0, tk.END)
        self.combobox2.delete(0, tk.END)
    	
        # new_window.protocol("WM_DELETE_WINDOW", self.on_new_window_close)
    
    def open_new_window_Patient_regist(self):
        # self.withdraw()  

        new_window = tk.Toplevel()
        new_window.title("Patient Registrierung")
        new_window.geometry("700x450")
        new_window.config(background="#2A324B")


        # Variables
        self.name_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.problematik_var = tk.StringVar()
        self.dentist_var = tk.StringVar()
        self.teeth_var = tk.StringVar()
  

        name_Label = tk.Label(new_window, text="Name:", font=("Arial", 10, "bold"), fg="white", background="#2A324B")
        name_Label.place(rely=0.1, relx=0.05)
        name_Label_Entry = tk.Entry(new_window, textvariable=self.name_var, width=27)
        name_Label_Entry.place(rely=0.1, relx=0.25)

        passwort_Label = tk.Label(new_window, text="passwort:", font=("Arial", 10, "bold"), fg="white", background="#2A324B")
        passwort_Label.place(rely=0.2, relx=0.05)
        passwort_Label_Entry = tk.Entry(new_window, show ='*', textvariable=self.password_var, width=27)
        passwort_Label_Entry.place(rely=0.20, relx=0.25)
        
        Krankenkassenart_Label = tk.Label(new_window, text="Krankenkassenart:", font=("Arial", 10, "bold"), fg="white", background="#2A324B")
        Krankenkassenart_Label.place(rely=0.3, relx=0.05)
        krankenkassenarten = ["gesetzlich", "freiwillig gesetzlich", "privat"]
        self.krankenk_var = tk.StringVar(self)
        self.combobox2 = Combobox(new_window, values=krankenkassenarten, textvariable=self.krankenk_var, width=24)  # Bind the selection event
        self.combobox2.current(0)  # Set the default selection
        self.combobox2.place(rely=0.3, relx=0.25)

        Problematik_label = tk.Label(new_window, text="Problematik", font=("Arial", 10, "bold"), fg="white", background="#2A324B")
        Problematik_label.place(rely=0.4, relx=0.05)
        Problem_options = ["Karies klein", "Karies groß", "Teilkrone", "krone", "Wurzelbehandlung"]
        self.combobox1 = Combobox(new_window, textvariable=self.problematik_var, values=Problem_options, width=24)
        self.problematik_var.set(Problem_options[0])  # Set the default selection
        self.combobox1.place(rely=0.4, relx=0.25)   

        self.Zahnanzahl_label = tk.Label(new_window, text="Zahnanzahl",  font=("Arial", 10, "bold"), fg="white", background="#2A324B")
        self.Zahnanzahl_label.place(rely=0.5, relx=0.05)
        self.Zahnanzahl_entry = tk.Entry(new_window, background="#f1f1f1", textvariable=self.teeth_var, width=27)
        self.Zahnanzahl_entry.place(rely=0.5, relx=0.25) 

        # register_button = tk.Button(new_window, text="Register", font=("Arial", 11, "bold"), command=self.save_data)
        self.register_button = tk.Button(new_window, text="Registrieren", font=("Arial", 11, "bold"), command=self.save_data2)
        self.register_button.place(rely=0.65, relx=0.16)

        self.Auslogen_button = tk.Button(new_window, text="Zurück",command=self.logout, width=25, bg="#DE5466", fg="white", font=("Arial", 9, "bold"))
        self.Auslogen_button.pack(side="bottom", pady=7)

        name_Label_Entry.delete(0, tk.END)
        passwort_Label_Entry.delete(0, tk.END)
        self.combobox2.delete(0, tk.END)
        self.combobox1.delete(0, tk.END)
        self.Zahnanzahl_entry.delete(0, tk.END)

        new_window.protocol("WM_DELETE_WINDOW", self.on_new_window_close)

    def save_data(self):
        # Récupérer les données saisies
        name = self.name_var.get()
        password = self.password_var.get()
        krankenkassenart = self.krankenk_var.get()

        # Charger le fichier Excel existant
        workbook = openpyxl.load_workbook('Database/Patienten_Zahnärzte_Kosten.xlsx')
        # Sélectionner la feuille de calcul spécifiée
        sheet = workbook['Zahnärzte']
        # Trouver la première ligne vide à partir de la ligne 4 (lignes 1 à 3 sont des en-têtes)
        row = 3
        while sheet.cell(row=row, column=2).value:
            row += 1
        # Enregistrer les données dans les colonnes spécifiées
        sheet.cell(row=row, column=2).value = name
        sheet.cell(row=row, column=3).value = password
        sheet.cell(row=row, column=4).value = krankenkassenart

        # Sauvegarder les modifications dans le fichier Excel
        workbook.save('Database/Patienten_Zahnärzte_Kosten.xlsx')

        # Afficher un message de succès
        tk.messagebox.showinfo("Success", "Registrierung Erfolgreich")

    def is_name_exists(self, name, sheet):
        # Vérifie si le nom existe déjà dans la colonne 3 (colonne des noms)
        for row in sheet.iter_rows(min_row=4, min_col=3, max_col=3):
            if row[0].value == name:
                return True
        return False

    def generate_unique_name(self, name, sheet):
        # Wenn ein Patient denselben Namen hat, generieren Sie einen eindeutigen Namen mit einer numerischen Erweiterung
        name_count = 0
        modified_name = name
        while self.is_name_exists(modified_name, sheet):
            name_count += 1
            modified_name = f"{name}_{name_count}"
        return modified_name

    def save_data2(self):
        # Daten aus den Eingabefeldern abrufen
        name = self.name_var.get()
        password = self.password_var.get()
        krankenkassenart = self.krankenk_var.get()
        zahn_probl = self.problematik_var.get()
        zahn_anzahl = self.teeth_var.get()

        # Vorhandenes Excel-Datei laden
        workbook = openpyxl.load_workbook('Database/Patienten_Zahnärzte_Kosten.xlsx')
        # Gewünschtes Tabellenblatt auswählen
        sheet = workbook['Stamm-Patienten']

        # Überprüfen, ob der Name bereits in den Daten vorhanden ist
        if self.is_name_exists(name, sheet):
            # Wenn der Name bereits vorhanden ist, fragen Sie den Benutzer, ob er sich bereits registriert hat.
            response = tk.messagebox.askquestion("Frage", f"Es existiert bereits ein Eintrag für '{name}'. Sind Sie bereits registriert?")
            if response == 'yes':
                # Wenn der Benutzer bereits registriert ist, aktualisieren Sie das Passwort und die dentalen Probleme.
                for row in sheet.iter_rows(min_row=4, min_col=3, max_col=3):
                    if row[0].value == name:
                        row_index = row[0].row
                        # Aktualisieren Sie das Passwort und die anderen Spaltenwerte (z.B., Krankenkasse, etc.) nach Bedarf
                        sheet.cell(row=row_index, column=4).value = password
                        # Fügen Sie neue dental Probleme hinzu
                        current_problematik = sheet.cell(row=row_index, column=6).value
                        new_problematik = f"{current_problematik}, {zahn_probl}"
                        sheet.cell(row=row_index, column=6).value = new_problematik
                        break
            else:
                # Wenn der Benutzer nicht bereits registriert ist, können Sie hier entsprechende Aktionen durchführen.
                pass
        else:
            # Wenn der Name nicht vorhanden ist, generieren Sie einen eindeutigen Namen
            unique_name = self.generate_unique_name(name, sheet)

            # Finden Sie die erste leere Zeile ab Zeile 4 (Zeilen 1 bis 3 sind Überschriften).
            row = 4
            while sheet.cell(row=row, column=3).value:
                row += 1
            # Daten in die entsprechenden Spalten eintragen
            sheet.cell(row=row, column=3).value = unique_name
            sheet.cell(row=row, column=4).value = password
            sheet.cell(row=row, column=5).value = krankenkassenart
            sheet.cell(row=row, column=6).value = zahn_probl
            sheet.cell(row=row, column=7).value = zahn_anzahl

        # Sauvegarder les modifications dans le fichier Excel
        workbook.save('Database/Patienten_Zahnärzte_Kosten.xlsx')

        # Afficher un message de succès
        tk.messagebox.showinfo("Success", "Registrierung Erfolgreich")
    
    def logout(self):
        self.withdraw()
        self.deiconify()
        # self.master.deiconify()
        # self.master.username_entry.delete(0, tk.END)
        # self.master.password_entry.delete(0, tk.END)

    def get_password(self):
        return self.password_entry.get()

    def on_new_window_close(self):
        self.deiconify()  # Réaffiche la première fenêtre lorsque la deuxième fenêtre est fermée
        self.destroy()

def open_change_password_window():
        change_password_window = ChangePasswordWindow()

class PatientView(tk.Toplevel):
    def __init__(self, master, patient_names):
        super().__init__(master)
        self.geometry("1300x580")
        # self.minsize(1300, 580)
        # self.maxsize(1300, 580)
        self.title("Patientenansicht")
        self.config(background="#3B6064")
        # self.last_names2 = last_names


        # Hauptframe für das Layout der Patientenansicht
        self.main_frame = tk.Frame(self, width=240, height=580)
        self.main_frame.pack(side="left")

        # Linker Frame für die Navigation oder zusätzliche Informationen
        self.left_frame = tk.Frame(self.main_frame, width=240, height=580, bg="#5B949A")
        self.left_frame.pack(side="left")
        self.left_frame.pack_propagate(False)

        self.info_Frame = tk.LabelFrame(self.main_frame, width=238, height=305, background="white", text="")
        self.info_Frame.place(rely=0.003, relx=0.005)
        
        self.info_frame_unterbox = tk.Frame(self.info_Frame, width=230, height=150, background="white")
        self.info_frame_unterbox.place(rely=0.66, relx=0)

        #Profil Bild
        self.image_frame = tk.Frame(self.info_Frame, width=180, height=180)
        self.image_frame.place(rely=0.04, relx=0.11)
        img = PhotoImage(file = "Bilder/user.png")
        lbl = Label(self.image_frame, image=img, anchor="center")
        lbl.place(rely=0, relx=0)

        # Info Frame
        self.Name_Label = tk.Label(self.info_frame_unterbox ,text="Titel: ", font=("Arial", 11, "bold"), background="white")
        self.Name_Label.place(rely=0.08, relx=0.11)

        self.Name_Label = tk.Label(self.info_frame_unterbox ,text="Name: " + patient_names, font=("Arial", 11, "bold"), background="white")
        self.Name_Label.place(rely=0.25, relx=0.11)

        self.Krankenkass_Label = tk.Label(self.info_frame_unterbox ,text="Krankenkasse: ", font=("Arial", 11, "bold"), background="white")
        self.Krankenkass_Label.place(rely=0.45, relx=0.11)

        #Button
        self.bg_button = tk.Button(self.left_frame, text="Background Ändern", width=25, bg="#2A324B", fg="white", font=("Arial", 9, "bold"))
        self.bg_button.pack(side="bottom", pady=13)

        self.Auslogen_button = tk.Button(self.left_frame, text="Auslogen",command=self.logout, width=25, bg="#DE5466", fg="white", font=("Arial", 9, "bold"))
        self.Auslogen_button.pack(side="bottom", pady=7)

        self.einstellung_button = tk.Button(self.left_frame, text="Passwort Ändern", width=25, bg="#2A324B", fg="white", font=("Arial", 9, "bold"), command=open_change_password_window) # TODO: , command=open_change_password_window
        self.einstellung_button.pack(side="bottom", pady=10)
       
        self.untersten_Frame = tk.Frame(self, width=1058, height=30, background="#5B949A")
        self.untersten_Frame.pack(side="bottom", fill="y")

        self.firma_name_label = tk.Label(self.untersten_Frame, text="Zahnärzte am Park GmbH", background="#5B949A", fg="white", font=("Arial", 11, "bold"))
        # firma_name_label.pack(side="left", fill="x")
        self.firma_name_label.place(x=15, y=5)
        self.animate_label()  # Animation starten

        self.current_time_label = tk.Label(self.untersten_Frame, text="", font=("Arial", 11, "bold"), fg="white", bg="#5B949A")
        self.current_time_label.place(x=350, y=5)

        self.NameLabel = tk.Label(self.untersten_Frame, text= username, font=("Arial", 11, "bold"), background="#5B949A", fg="white")
        self.NameLabel.place(x=490, y=5)


        #--------Auswahl Frame oben---------
        auswahl_Frame1 = tk.LabelFrame(self, text="", width=1055, height=304, background="white")
        auswahl_Frame1.place(rely=0.003, relx=0.186)


        # Variables
        self.teeth_var = tk.StringVar()
        self.fill_material_var = tk.StringVar()
        self.cost_var = tk.StringVar()
        self.dentist_var = tk.StringVar()
        self.problematik_var = tk.StringVar()

        # Create labels and entries for teeth and filling selection
        self.DentaleProblem = tk.Label(auswahl_Frame1, text="Problematik:", background="white", font=("Arial", 10, "bold"))
        self.DentaleProblem.place(rely=0.05, relx=0.01)

        Problem_options = ["Karies klein", "Karies groß", "Teilkrone", "krone", "Wurzelbehandlung"]        
        self.combobox1 = Combobox(auswahl_Frame1, textvariable=self.problematik_var, values=Problem_options)
        self.problematik_var.set(Problem_options[0])  # Set the default selection
        self.combobox1.place(rely=0.05, relx=0.15) 

        self.teeth_label = tk.Label(auswahl_Frame1, text="Zahnanzahl:", background="white", font=("Arial", 10, "bold"))
        self.teeth_label.place(rely=0.243, relx=0.01)
        self.teeth_entry = tk.Entry(auswahl_Frame1, background="#f1f1f1",width=23 ,textvariable=self.teeth_var)
        self.teeth_entry.place(rely=0.243, relx=0.15)

        self.filling_label = tk.Label(auswahl_Frame1, text="Füllmaterial:", background="white", font=("Arial", 10, "bold"))
        self.filling_label.place(rely=0.45, relx=0.01)
        filling_options = ["normal", "höherwertig", "höchstwertig"]
        self.combobox1 = Combobox(auswahl_Frame1, textvariable=self.fill_material_var, values=filling_options)
        self.fill_material_var.set(filling_options[0])  # Set the default selection
        self.combobox1.place(rely=0.45, relx=0.15)

        self.behandlung_Zeit_Label = tk.Label(auswahl_Frame1,text="Behandlungszeit", background="white", font=("Arial", 10, "bold"))
        self.behandlung_Zeit_Label.place(rely=0.65, relx=0.01)
        self.anzeige_Zeit_Label = tk.Label(auswahl_Frame1,text="", height=2, width=10, background="#B2CFD2", font=("Arial", 10, "bold"))
        self.anzeige_Zeit_Label.place(rely=0.62, relx=0.15)

        self.Krankenk_label = tk.Label(auswahl_Frame1, text="Krankenkassenart:", background="white", font=("Arial", 10, "bold"))
        self.Krankenk_label.place(rely=0.05, relx=0.36)
        # Krankenkassenart ComboBox
        krankenkassenarten = ["------ Auswählen ------","gesetzlich", "freiwillig gesetzlich", "privat"]
        self.krankenk_var = tk.StringVar(self)
        self.combobox2 = Combobox(auswahl_Frame1, values=krankenkassenarten, textvariable=self.krankenk_var, width=24)
        self.combobox2.bind("<<ComboboxSelected>>", self.update_dentist_options)  # Bind the selection event
        self.combobox2.current(0)  # Set the default selection
        self.combobox2.place(rely=0.05, relx=0.56)

        # Dentist Selection Label
        self.dentist_label = tk.Label(self, text="Behandelter Zahnarzt:", background="white", font=("Arial", 10, "bold"))
        self.dentist_label.place(rely=0.1, relx=0.478)
        # Dentist ComboBox
        self.dentist_var = tk.StringVar(self)
        self.dentist_combobox = Combobox(self, textvariable=self.dentist_var, state="readonly", width=24)
        self.dentist_combobox.place(rely=0.1, relx=0.639)
        self.dentist_combobox.bind("<<ComboboxSelected>>", self.updateDescription)

        self.cost_label = tk.Label(auswahl_Frame1, text="Behandlungskosten: $0.00", pady=20, background="#B2CFD2", height=3, padx=60, justify="center", font=("Arial", 10, "bold"))
        self.cost_label.place(rely=0.446, relx=0.4)

        self.buttonBerechnen = tk.Button(auswahl_Frame1, text="Kosten Berechnen",background="#3B6064", fg="white", command=self.calculate_cost, font=("Arial", 10, "bold"), padx=5, pady=10)
        self.buttonBerechnen.place(rely=0.8, relx=0.399)
        self.buttonBerechnen = tk.Button(auswahl_Frame1, text="Termin Buchen",background="#3B6064", fg="white", command=TerminView, font=("Arial", 10, "bold"), padx=10, pady=10)
        self.buttonBerechnen.place(rely=0.8, relx=0.5516)

        self.terminDescr = tk.Frame(auswahl_Frame1, background="white", width=266, height=280)
        self.terminDescr.place(rely=0.03, relx=0.74)

        self.description = tk.Label(self.terminDescr, text="keine Beschreibung", width=36, height=10, background="white")
        self.description.place(rely=0.24, relx=0.01)

        # Termin kalender 
        #--------Auswahl Frame unter---------
        auswahl_Frame2 = tk.LabelFrame(self, text="", width=480.5, height=237, background="white")
        auswahl_Frame2.place(rely=0.5325, relx=0.186)

        auswahl_Frame3 = tk.LabelFrame(self, text="", width=540.5, height=237, background="white")
        auswahl_Frame3.place(rely=0.5325, relx=0.5575)

        columns=("Datum", "Uhrzeit", "Arzt")
        self.treeview_gebu_Termin = ttk.Treeview(auswahl_Frame3, columns= columns, height=10,  show='headings')
        self.treeview_gebu_Termin.pack()

        # Überschrift für den Treeview festlegen
        self.treeview_gebu_Termin.heading("Datum", text="Datum", anchor='center')
        self.treeview_gebu_Termin.heading("Uhrzeit", text="Uhrzeit", anchor='center')
        self.treeview_gebu_Termin.heading("Arzt", text="Arzt", anchor='center')

        # Überschriften für den Treeview festlegen
        for column in columns:
            self.treeview_gebu_Termin.heading(column, text=column, anchor='center')
        # Spalten konfigurieren, um die Werte zu zentrieren
        for column in columns:
            self.treeview_gebu_Termin.column(column, anchor='center')



        # testButton = tk.Button(auswahl_Frame2,text="buttonTest", width=10, height=2, command=TerminView)
        # testButton.place(rely=0, relx=0)







        # self.update_image(self)  # Bildwechsel starten
        self.update_time()  # Time Update
    
    def open_Kalender_view(self):
        kalender_view = TerminView(self)
        # kalender_view.mainloop()
    
    def calculate_cost(self):
        teeth = int(self.teeth_var.get())
        filling = self.fill_material_var.get()
        selected_krankenk = self.krankenk_var.get()
        problematik = self.problematik_var.get()
        last_names2 = username

        ## TODO: wenn Teeth == 0 or wenn filling == 0 or ....... messagebox.showerror("Fehler", "Anzahl teeth eingeben")

        # Arbeitsblatt mit openpyxl öffnen
        workbook = openpyxl.load_workbook('Database\Patienten_Zahnärzte_Kosten.xlsx')

        if selected_krankenk == "privat":
            sheet = workbook['privat']
        elif selected_krankenk == "gesetzlich":
            sheet = workbook['gesetzlich']
        else:
            sheet = workbook['freiwillig gesetzlich']

        # Überschriften
        sheet['A1'] = 'Patient'
        sheet['B1'] = 'Anzahl zu behandelnder Zähne'
        sheet['C1'] = 'Filling Material'
        sheet['D1'] = 'Krankenkasse'
        sheet['E1'] = 'Problematik'

        # Werte
        row = sheet.max_row + 1  # Nächste verfügbare Zeile
        sheet[f'A{row}'] = last_names2
        sheet[f'B{row}'] = teeth
        sheet[f'C{row}'] = filling
        sheet[f'D{row}'] = selected_krankenk
        sheet[f'E{row}'] = problematik


        # Datei speichern
        workbook.save('Database\Patienten_Zahnärzte_Kosten.xlsx')

        # Correspondance des options de combobox avec les pourcentages
        if problematik == "Karies klein":
            self.anzeige_Zeit_Label.config(text="0.25")
            if filling == "normal":
                if selected_krankenk == "gesetzlich":
                    cost = 100 * teeth * 0.8
            elif filling == "höherwertig":
                    cost = 180 * teeth * 0.7
            elif filling == "höchstwertig":
                    cost = 250 * teeth * 0.5
        if problematik == "Karies klein":
            self.anzeige_Zeit_Label.config(text="0.25")
            if filling == "normal":
                if selected_krankenk == "privat":
                    cost = 100 * teeth * 1
            elif filling == "höherwertig":
                    cost = 180 * teeth * 1
            elif filling == "höchstwertig":
                    cost = 250 * teeth * 0.95
        if problematik == "Karies groß":
            self.anzeige_Zeit_Label.config(text="1")
            if filling == "normal":
                if selected_krankenk == "gesetzlich":
                    cost = 200 * teeth * 0.8
            elif filling == "höherwertig":
                if selected_krankenk == "gesetzlich":
                    cost = 360 * teeth * 0.7
            elif filling == "höchstwertig":
                    cost = 480 * teeth * 0.5
        if problematik == "Karies groß":
            if filling == "normal":
                self.anzeige_Zeit_Label.config(text="1")
                if selected_krankenk == "privat":
                    cost = 200 * teeth * 1
            elif filling == "höherwertig":
                    cost = 360 * teeth * 1
            elif filling == "höchstwertig":
                    cost = 480 * teeth * 0.95
        if problematik == "Teilkrone":
            if filling == "normal":
                self.anzeige_Zeit_Label.config(text="1")
                if selected_krankenk == "gesetzlich":
                    cost = 1000 * teeth * 0.8
            elif filling == "höherwertig":
                    cost = 1800 * teeth * 0.7
            elif filling == "höchstwertig":
                    cost = 3100 * teeth * 0.30
        if problematik == "Teilkrone":
            if filling == "normal":
                self.anzeige_Zeit_Label.config(text="1")
                if selected_krankenk == "privat":
                    cost = 1000 * teeth * 1
            elif filling == "höherwertig":
                    cost = 1800 * teeth * 0.95
            elif filling == "höchstwertig":
                    cost = 3100 * teeth * 0.85
        if problematik == "krone":
            if filling == "normal":
                self.anzeige_Zeit_Label.config(text="2")
                if selected_krankenk == "gesetzlich":
                    cost = 2800 * teeth * 0.7
            elif filling == "höherwertig":
                    cost = 3600 * teeth * 0.5
            elif filling == "höchstwertig":
                    cost = 4200 * teeth * 0.25
        if problematik == "krone":
            if filling == "normal":
                self.anzeige_Zeit_Label.config(text="2")
                if selected_krankenk == "privat":
                    cost = 2800 * teeth * 1
            elif filling == "höherwertig":
                    cost = 3600 * teeth * 0.85
            elif filling == "höchstwertig":
                    cost = 4200 * teeth * 0.75
        if problematik == "Wurzelbehandlung":
            self.anzeige_Zeit_Label.config(text="1.5")
            if filling == "normal":
                if selected_krankenk == "gesetzlich":
                    cost = 750 * teeth * 0.9
            elif filling == "höherwertig":
                    self.anzeige_Zeit_Label.config(text="1.5")
                    cost = 1200 * teeth * 0.70
            elif filling == "höchstwertig":
                    cost = 1500 * teeth * 0.45
                    self.anzeige_Zeit_Label.config(text="2")
        if problematik == "Wurzelbehandlung":
            if filling == "normal":
                if selected_krankenk == "privat":
                    cost = 750 * teeth * 1
            elif filling == "höherwertig":
                    cost = 1200 * teeth * 0.95
            elif filling == "höchstwertig":
                    cost = 1500 * teeth * 0.85
        

        self.cost_var.set("Behandlungskosten: {}€".format(cost))
        self.cost_label.config(textvariable=self.cost_var)
    
    def update_dentist_options(self, event):
        selected_krankenk = self.krankenk_var.get()
        if selected_krankenk == "gesetzlich":
            allowed_dentists = ["Herr Dr. Kraft", "Herr Dr. Hausmann"]
        elif selected_krankenk == "privat":
            allowed_dentists = ["Herr Dr. Huber", "Frau Dr. Wurzel", "Frau Dr. Winkel"]
        elif selected_krankenk == "freiwillig gesetzlich":
            allowed_dentists = ["Frau Dr. Winkel", "Herr Dr. Hausmann"]
        else:
            allowed_dentists = ["Herr Dr. 1", "Herr Dr. 2", "Herr Dr. 3", "Herr Dr. 4", "Herr Dr. 5"]

        self.dentist_var.set("")  # Clear the current selection
        self.dentist_combobox['values'] = allowed_dentists  # Update the ComboBox widget

    def updateDescription(self, event):
         selected_Artz = self.dentist_combobox.get()
         if selected_Artz == "Herr Dr. Huber":
              self.description.config(background="#F8C9CF", text="Öffnungszeiten von Dr. Huber:\nMo-Fr: 8-12 Uhr und 14-16 Uhr\n\n Drücken sie bitte ganz unter\n auf Terminkalender")
         if selected_Artz == "Herr Dr. Kraft":
              self.description.config(background="#F8C9CF", text="Öffnungszeiten von Dr. Kraft:\nMo-Fr: 10-12 Uhr und 14-18 Uhr\n\n Drücken sie bitte ganz unter\n auf Terminkalender")
         if selected_Artz == "Frau Dr. Winkel":
              self.description.config(background="#F8C9CF", text="Öffnungszeiten von Dr. Winkel:\nMo-Fr: 8-14 Uhr\n\n Drücken sie bitte ganz unter\n auf Terminkalender")
         if selected_Artz == "Herr Dr. Hausmann":
              self.description.config(background="#F8C9CF", text="Öffnungszeiten von Dr. Hausmann:\nMo: 9-12 Uhr und Fr 12-16 Uhr\n\n Drücken sie bitte ganz unter\n auf Terminkalender")
         if selected_Artz == "Frau Dr. Wurzel":
              self.description.config(background="#F8C9CF", text="Öffnungszeiten von Dr. Wurzel:\nDi: 8-12 und Do: 12-18 Uhr\n\n Drücken sie bitte ganz unter\n auf Terminkalender")

    def update_time(self):
        current_datetime = datetime.now()
        current_time = datetime.now().strftime("%H:%M:%S")  # Aktuelle Uhrzeit abrufen
        current_date = current_datetime.strftime("%d.%m.%Y")  # Aktuelles Datum abrufen
        self.current_time_label.config(text=current_time)  # Uhrzeit im Label aktualisieren

        datetime_text = f"{current_date} {current_time}"  # Kombinierten Text erstellen
        self.current_time_label.config(text=datetime_text)  # Text im Label aktualisieren

        self.current_time_label.after(1000, self.update_time)  # Nach 1000 Millisekunden erneut aufrufen

    def logout(self):
        self.destroy()
        self.master.deiconify()
        self.master.username_entry.delete(0, tk.END)
        self.master.password_entry.delete(0, tk.END)

    def animate_label(self):
        current_fg = self.firma_name_label["foreground"]
        if current_fg == "white":
            self.firma_name_label["foreground"] = "black"
        else:
            self.firma_name_label["foreground"] = "white"
        self.firma_name_label.after(500, self.animate_label)  # Nach 500 Millisekunden erneut aufrufen

class TerminView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Terminkalender")
        self.geometry("525x295")
        self.config(bg="#3B6064")
        self.maxsize(525, 355)
        self.minsize(525, 355)

        self.selected_label = None  # Variable zur Verfolgung des ausgewählten Labels
        self.create_calendar()

        self.buch_button = tk.Button(self, text="Termin bestätigen", background="white", fg="black", font=("Arial", 13))
        self.buch_button.pack(side="bottom",  padx=5, pady=10, ipadx=50)


    def create_calendar(self):

        # Tabelle für Stunden und Tage
        auswahl_Frame2 = tk.LabelFrame(self, text="", width=550.5, height=237, background="white", bg="#FFF8E8")
        auswahl_Frame2.place(rely=0.05, relx=0.016)

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

class DentistView(tk.Toplevel):
    def __init__(self, master, last_names):
        super().__init__(master)
        self.geometry("1300x580")
        self.minsize(1300, 580)
        self.maxsize(1300, 580)
        self.title("Zahnarztansicht")
        self.config(background="#3B6064")
        self.last_names2 = last_names

        # Zielgröße für das redimensionierte Bild
        self.width = 530
        self.height = 260

        self.untersten_Frame = tk.Frame(self, width=1300, height=30, background="#5B949A")
        self.untersten_Frame.pack(side="bottom", fill="y")
        
        self.firma_name_label = tk.Label(self.untersten_Frame, text="Zahnärzte am Park GmbH", background="#5B949A", fg="white", font=("Arial", 11, "bold"))
        # firma_name_label.pack(side="left", fill="x")
        self.firma_name_label.place(x=15, y=5)
        self.animate_label()  # Animation starten

        self.current_time_label = tk.Label(self.untersten_Frame, text="", font=("Arial", 11, "bold"), fg="white", bg="#5B949A")
        self.current_time_label.place(x=1150, y=5)

        self.NameLabel = tk.Label(self.untersten_Frame, text= username, font=("Arial", 11, "bold"), background="#5B949A", fg="white")
        self.NameLabel.place(x=600, y=5)

        self.termin_Frame = tk.LabelFrame(self, text="Terminkalender",border=0, background="white")
        self.termin_Frame.place(x=7, y=7)

        columns=("Patient", "Problematik", "Filling Material", "Anzahl zu behandelnder Zähne")
        self.treeview_gebu_Termin = ttk.Treeview(self.termin_Frame, columns= columns, height=12, show='headings')
        self.treeview_gebu_Termin.pack()

        # Überschrift für den Treeview festlegen
        self.treeview_gebu_Termin.heading("Patient", text="Patientname", anchor='center')
        self.treeview_gebu_Termin.heading("Problematik", text="Behandlungen", anchor='center')
        self.treeview_gebu_Termin.heading("Filling Material", text="Material", anchor='center')
        self.treeview_gebu_Termin.heading("Anzahl zu behandelnder Zähne", text="Zähne", anchor='center')

        self.treeview_gebu_Termin.column("Patient", width=150)
        self.treeview_gebu_Termin.column("Problematik", width=200)
        self.treeview_gebu_Termin.column("Filling Material", width=200)
        self.treeview_gebu_Termin.column("Anzahl zu behandelnder Zähne", width=200)

        # Überschriften für den Treeview festlegen
        for column in columns:
            self.treeview_gebu_Termin.heading(column, text=column, anchor='center')
        # Spalten konfigurieren, um die Werte zu zentrieren
        for column in columns:
            self.treeview_gebu_Termin.column(column, anchor='center')
        style = ttk.Style()
        style.configure('treeview_gebu_Termin', rowheight=30)  # Hier können Sie die gewünschte Höhe anpassen

        self.imageView_frame = tk.Frame(self, height=260, width=530)
        self.imageView_frame.place(x=765, y=7)

        df = None  # Initialisation par défaut de df
        if username == "Huber" or username == "Wurzel":
            df = pd.read_excel("Database\Patienten_Zahnärzte_Kosten.xlsx", sheet_name="privat")
        elif username == "Kraft":
             df = pd.read_excel("Database\Patienten_Zahnärzte_Kosten.xlsx", sheet_name="gesetzlich")
        # elif username == "Winkel":
        elif username == "Hausmann":
             df1 = pd.read_excel("Database\Patienten_Zahnärzte_Kosten.xlsx", sheet_name="gesetzlich")
             df2 = pd.read_excel("Database\Patienten_Zahnärzte_Kosten.xlsx", sheet_name="freiwillig gesetzlich")
             df = pd.concat([df1, df2])
             
        if df is not None:
            font = Font(size=11, weight="bold")
            for index, row in df.iterrows():
                self.treeview_gebu_Termin.insert("", "end", values=(row[0], row[4], row[2], row[1]), tags="custom_font")
        
            self.treeview_gebu_Termin.tag_configure("custom_font", font=font)
        style = ttk.Style()
        style.configure("treeview_gebu_Termin", rowheight=40)  # Augmenter la valeur de rowheight pour augmenter l'espace


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
  
class ChangePasswordWindow(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Passwort Änderung")
        self.geometry("500x400")
        self.config(background="#5B949A")
        self.resizable(False, False)

        self.old_password_label = tk.Label(self, text="Alte Passwort:", background="#5B949A", font=("Arial", 10, "bold"))
        self.old_password_label.place(rely=0.15, relx=0.18)
        self.old_password_entry = tk.Entry(self, show="*")
        self.old_password_entry.place(rely=0.15, relx=0.46)

        self.new_password_label = tk.Label(self, text="Neue Passwort:", background="#5B949A", font=("Arial", 10, "bold"))
        self.new_password_label.place(rely=0.25, relx=0.18)
        self.new_password_entry = tk.Entry(self, show="*")
        self.new_password_entry.place(rely=0.25, relx=0.46)

        self.confirm_password_label = tk.Label(self, text="Pass Bestätigen:", background="#5B949A", font=("Arial", 10, "bold"))
        self.confirm_password_label.place(rely=0.37, relx=0.18)
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.place(rely=0.37, relx=0.46)

        self.change_button = tk.Button(self, text="Bestätigen", background="white", command=self.change_password, padx= 40, pady=10)
        self.change_button.place(rely=0.55, relx=0.35)

    def change_password(self):
        old_password = self.old_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Vérification si les champs de mot de passe sont vides
        if not old_password or not new_password or not confirm_password:
            messagebox.showerror("Fehler", "Bitte Felder ausfüllen!!")
            return

        # Vérification si le nouveau mot de passe correspond à la confirmation
        if new_password != confirm_password:
            messagebox.showerror("Fehler", "Das neue Passwort stimmt nicht mit der Bestätigung überein.")
            return

        # Vérification si le mot de passe actuel est correct (exemple de mot de passe actuel : "password")
        current_password = self.master.get_password()
        if old_password != current_password:
            messagebox.showerror("Fehler", "Das aktuelle Passwort ist inkorrekt.")
            return

        workbook = openpyxl.load_workbook("Patienten_Zahnärzte_Kosten.xlsx")
        sheet = workbook["Stamm-Patienten"]

        # Recherche de l'index de la ligne correspondant à l'utilisateur
        # username = self.username_entry.get()
        username = self.username
        row_index = None
        for row in sheet.iter_rows(min_row=5, min_col=3, max_col=4):
            if row[0].value == username:
                row_index = row[0].row
                break
        if row_index is not None:
        # Mise à jour du mot de passe dans la colonne appropriée
            sheet.cell(row=row_index, column=4).value = new_password
            workbook.save("Patienten_Zahnärzte_Kosten.xlsx")
            messagebox.showinfo("Succès", "Le mot de passe a été changé avec succès.")
            self.destroy()
        else:
            messagebox.showerror("Erreur", "Utilisateur non trouvé dans la base de données.")


        messagebox.showinfo("Succès", "Le mot de passe a été changé avec succès.")
        self.destroy()  


# Hauptprogramm
if __name__ == "__main__":
    loginWindow = LoginWindow()
    loginWindow.geometry("550x500")
    loginWindow.maxsize(550, 550)
    loginWindow.minsize(550, 550)

    loginWindow.mainloop()
