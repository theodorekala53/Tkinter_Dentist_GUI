class ClasseA:
    variable_de_classe = 42

class ClasseB:
    def __init__(self):
        # Pour accéder à la variable de classe de ClasseA
        valeur = ClasseA.variable_de_classe
        print(valeur)

# Création d'une instance de ClasseB
obj_b = ClasseB()
