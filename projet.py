# This is the project out teacher assign us
# We have to define "Etudiant", "Section" and "Projet" and the main function that will use these classes

class Section:
    def __init__(self, numSection, nomSection):
        self.__numSection = numSection
        self.__nomSection = nomSection
    def getNumSection(self):
        return self.__numSection
    def getNomSection(self):
        return self.__nomSection

    # If you need setters you can define them

class Projet:
    def __init__(self, numProjet, theme):
        self.__numProjet = numProjet
        self.__theme = theme
    def getNumProjet(self):
        return self.__numProjet
    def getTheme(self):
        return self.__theme

    # If you need setters you can define them

class Etudiant:
    def __init__(self, numero, prenom, nom, section, projet):
        self.__numero = numero
        self.__prenom = prenom
        self.__nom = nom
        self.__section = section
        self.__projet = projet
    def getNumero(self):
        return self.__numero
    def getPrenom(self):
        return self.__prenom
    def getNom(self):
        return self.__nom
    def getSection(self):
        return self.__section
    def getProjet(self):
        return self.__projet

    # If you need setters you can define them


# The main function what will execute our application
def main():
    choix = 0
    listeSection = []
    listeProjet = []
    listeEtudiant = []

    while choix == 0:
        print("+-----------------------------------------------+")
        print("1. Creer une section")
        print("2. Creer un projet")
        print("3. Creer un etudiant")
        print("4. Lister les sections")
        print("5. Lister les projets")
        print("6. Lister les etudiants")
        print("7. Afficher les etudiants d'une section donnee")
        print("8. Afficher les etudiant qui travaillent dans un projet donnee")
        print("9. Afficher pour chaque projet les etudiants qui y travaillent et leur section respective")
        print("10. Sortie")
        choix = int(input("Faite votre choix: "))
        if choix == 1:
            print("+--------------Creation d'une section----------------+")
            numero = int(input("Numero section ? "))
            nom = input("Nom section ? ")
            section = Section(numero, nom)
            listeSection.append(section)
            choix = 0
            print("+--------------Section creer----------------+")
        elif choix == 2:
            print("+--------------Creation d'un projet----------------+")
            numero = int(input("Numero projet ? "))
            theme = input("Theme projet ? ")
            projet = Projet(numero, theme)
            listeProjet.append(projet)
            choix = 0
            print("+--------------Projet creer----------------+")
        elif choix == 3:
            if len(listeSection) == 0 or len(listeProjet) == 0:
                if len(listeSection) == 0:
                    print("-- Il n'y a aucune section existante.--\nCreer d'abord une section au moins")
                elif len(listeProjet) == 0:
                    print("-- Il n'y a aucun projet existant.--\nCreer d'abord un projet au moins")
            else:
                print("+--------------Creation d'un etudiant-----------1-----+")
                numero = int(input("Numero etudiant ? "))
                prenom = input("Prenom etudiant ? ")
                nom = input("Nom etudiant ? ")

                section = None

                while section == None:
                    print("+--------------Section de l'etudiant----------------+")
                    numSection = int(input("Numero de section de cet etudiant ? "))
                    for i in range(len(listeSection)):
                        if listeSection[i].getNumSection() == numSection:
                            section = listeSection[i]
                            print("+------------------------------+")
                            break
                    if section == None:
                        print("Ce numero de section n'existe pas ! ")
                        print("+--------------Liste des sections existantes----------------+")
                        for j in listeSection:
                            print("+------------------------------+")
                            print(f"Numero section: {j.getNumSection()}")
                            print(f"Nom section: {j.getNomSection()}")
                        print("+------------------------------+")

                projet = None
                while projet == None:
                    print("+--------------Projet de l'etudiant----------------+")
                    numProjet = int(input("Numero de projet de cet etudiant ? "))
                    for i in range(len(listeProjet)):
                        if listeProjet[i].getNumProjet() == numProjet:
                            projet = listeProjet[i]
                            print("+------------------------------+")
                            break
                    if projet == None:
                        print("Ce numero de projet n'existe pas ! ")
                        print("+--------------Liste des projets existants----------------+")
                        for j in listeProjet:
                            print("+------------------------------+")
                            print(f"Numero projet: {j.getNumProjet()}")
                            print(f"Theme: {j.getTheme()}")
                        print("+------------------------------+")

                if section != None and projet != None:
                    etudiant = Etudiant(numero, prenom, nom, section, projet)
                    listeEtudiant.append(etudiant)
                    print("+--------------Etudiant creer----------------+")
            choix = 0
        elif choix == 4:
            if len(listeSection) == 0:
                print("------- Il n'y a pas de section -------")
            else:
                print("+--------------Liste des sections----------------+\n")
                for s in listeSection:
                    print("+------------------------------+")
                    print(f"Numero section: {s.getNumSection()}")
                    print(f"Nom section: {s.getNomSection()}")
                print("+------------------------------+")
            choix = 0
        elif choix == 5:
            if len(listeProjet) == 0:
                print("------- Il n'y a pas de projets -------")
            else:
                print("+--------------Liste des projet----------------+\n")
                for p in listeProjet:
                    print("+------------------------------+")
                    print(f"Numero projet: {p.getNumProjet()}")
                    print(f"Theme: {p.getTheme()}")
                print("+------------------------------+")
            choix = 0
        elif choix == 6:
            if len(listeEtudiant) == 0:
                print("------- Il n'y a pas d'etudiant -------")
            else:
                print("+--------------Liste des etudiants----------------+\n")
                for e in listeEtudiant:
                    print("+------------------------------+")
                    print(f"Numero: {e.getNumero()}")
                    print(f"Prenom: {e.getPrenom()}")
                    print(f"Nom: {e.getNom()}")
                    print(f"Numero section: {e.getSection().getNumSection()}")
                    print(f"Nom section: {e.getSection().getNomSection()}")
                    print(f"Numero projet: {e.getProjet().getNumProjet()}")
                    print(f"Theme: {e.getProjet().getTheme()}")
                print("+------------------------------+")
            choix = 0
        elif choix == 7:
            if len(listeSection) == 0 or len(listeEtudiant) == 0:
                if len(listeSection) == 0:
                    print("Il n'y a pas de section cree en d'abord")
                elif len(listeEtudiant) == 0:
                    print("Il n'y a pas d'etudiant cree en d'abord")
            else:
                numSectionE = None
                while numSectionE == None:
                    numSection = int(input("Donner le numero de la section ? "))
                    for i in listeSection:
                        if i.getNumSection() == numSection:
                            numSectionE = numSection
                            break
                    if numSectionE == None:
                            print("Numero section inexistant !")

                for e in listeEtudiant:
                    if e.getSection().getNumSection() == numSectionE:
                        print("+------------------------------+")
                        print(f"Numero: {e.getNumero()}")
                        print(f"Nom: {e.getPrenom()}")
                        print(f"Prenom: {e.getNom()}")
                print("+------------------------------+")
            choix = 0
        elif choix == 8:
            if len(listeProjet) == 0 or len(listeEtudiant) == 0:
                if len(listeProjet) == 0:
                    print("Il n'y a pas de projet cree en d'abord")
                elif len(listeEtudiant) == 0:
                    print("Il n'y a pas d'etudiant cree en d'abord")
            else:
                numProjetE = None
                while numProjetE == None:
                    numProjet = int(input("Donner le numero du projet ? "))
                    for i in listeProjet:
                        if i.getNumProjet() == numProjet:
                            numProjetE = numProjet
                            break
                    if numProjetE == None:
                        print("Numero projet inexistant !")

                for e in listeEtudiant:
                    if e.getProjet().getNumProjet() == numProjetE:
                        print("+------------------------------+")
                        print(f"Numero: {e.getNumero()}")
                        print(f"Prenom: {e.getPrenom()}")
                        print(f"Nom: {e.getNom()}")
                print("+------------------------------+")
            choix = 0
        elif choix == 9:
            if len(listeEtudiant) == 0:
                print("Il n'y a pas d'etudiant cree en d'abord")
            else:
                for p in listeProjet:
                    for e in listeEtudiant:
                        if e.getProjet().getNumProjet() == p.getNumProjet():
                            print("+------------------------------+")
                            print(f"Numero: {e.getNumero()}")
                            print(f"Prenom: {e.getPrenom()}")
                            print(f"Nom: {e.getNom()}")
                            print(f"Numero section: {e.getSection().getNumSection()}")
                            print(f"Nom section: {e.getSection().getNomSection()}")
            choix = 0
        elif choix == 10:
            break
        else:
            print("Choix impossible !")
            choix = 0

main()