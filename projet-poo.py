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
            print("+--------------Creation d'un etudiant----------------+")
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

            etudiant = Etudiant(numero, prenom, nom, section, projet)
            listeEtudiant.append(etudiant)
            print("+--------------Etudiant creer----------------+")
            choix = 0
        elif choix == 4:
            print("+--------------Liste des sections----------------+\n")
            for s in listeSection:
                print("+------------------------------+")
                print(s.getNumSection())
                print(s.getNomSection())
            print("+------------------------------+")
            choix = 0
        elif choix == 5:
            print("+--------------Liste des projets----------------+\n")
            for p in listeProjet:
                print("+------------------------------+")
                print(p.getNumProjet())
                print(p.getTheme())
            print("+------------------------------+")
            choix = 0
        elif choix == 6:
            print("+--------------Liste des etudiants----------------+\n")
            for e in listeEtudiant:
                print("+------------------------------+")
                print(e.getNumero())
                print(e.getPrenom())
                print(e.getNom())
                print("\t"+e.getSection().getNumSection())
                print("\t"+e.getSection().getNomSection())
                print("\t"+e.getProjet().getNumProjet())
                print("\t"+e.getProjet().getTheme())
            print("+------------------------------+")
            choix = 0
        elif choix == 7:
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
                    print(e.getNumero())
                    print(e.getPrenom())
                    print(e.getNom())
            print("+------------------------------+")
            choix = 0
        elif choix == 8:
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
                if e.getProjet().getNumSection() == numProjetE:
                    print("+------------------------------+")
                    print(e.getNumero())
                    print(e.getPrenom())
                    print(e.getNom())
            print("+------------------------------+")
            choix = 0
        elif choix == 9:
            for p in listeProjet:
                for e in listeEtudiant:
                    if e.getProjet().getNumProjet() == p.getNumProjet():
                        print("+------------------------------+")
                        print(e.getNumero())
                        print(e.getPrenom())
                        print(e.getNom())
                        print("\t" + e.getSection().getNumSection())
                        print("\t" + e.getSection().getNomSection())
            choix = 0
        elif choix == 10:
            break
        else:
            print("Choix impossible !")
            choix = 0

main()

