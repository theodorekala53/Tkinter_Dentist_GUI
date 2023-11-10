import tkinter as tk
from tkinter import ttk

def change_couleur_treeview(treeview, couleur):
    style = ttk.Style()
    style.configure("Treeview", background=couleur)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Exemple de TreeView")

# Création du TreeView
tree = ttk.Treeview(fenetre, columns=('Nom', 'Age', 'Ville'))

# Ajout des en-têtes
tree.heading('#0', text='ID')
tree.heading('Nom', text='Nom')
tree.heading('Age', text='Age')
tree.heading('Ville', text='Ville')

# Ajout des données
tree.insert('', '0', 'item1', text='1', values=('John Doe', 30, 'Ville1'))
tree.insert('', '1', 'item2', text='2', values=('Jane Doe', 25, 'Ville2'))
tree.insert('', '2', 'item3', text='3', values=('Bob Smith', 35, 'Ville3'))

# Changement de la couleur de fond du TreeView
change_couleur_treeview(tree, 'lightgray')

# Affichage du TreeView
tree.pack()

# Lancement de la boucle principale
fenetre.mainloop()
