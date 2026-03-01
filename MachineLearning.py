import pandas as pd
import numpy as np
data_Titanic = pd.read_csv("titanic_Filter.csv")
age = [
    (0, 20),
    (21, 40),
    (41, 60),
    (61, 100)]
classe = [1, 2, 3]
Index_Ligne = 0
Index_Colonne = 0
Age_Utilisateur = 0
Classe_Utilisateur = 0
Sex_Utilisateur = ""
age_min = 0
age_max = 0
Survie_homme = np.zeros((len(classe), len(age)))
Survie_femme = np.zeros((len(classe), len(age)))

for classe_Tableau_male,classe_male in enumerate(classe):
    for age_Tableau_male,(age_min, age_max) in enumerate(age):

        data_homme_Survie = data_Titanic[
            (data_Titanic['Sex'] == "male") &
            (data_Titanic['Pclass'] == classe_male) &
            (data_Titanic['Age'] >= age_min) &
            (data_Titanic['Age'] <= age_max)
        ]
        if len(data_homme_Survie) > 0:
            Survie_homme[classe_Tableau_male, age_Tableau_male] = data_homme_Survie['Survived'].mean() * 100
            homme_survie = data_homme_Survie['Survived'].mean() * 100 
        else:
            homme_survie = 0
        print("Classe:", classe_male, "Âge >", age_min, "-", age_max, ":", homme_survie, "%")
        Survie_homme[classe_Tableau_male, age_Tableau_male] = homme_survie

print(Survie_homme) #[[36.8852459  35.65217391 27.41935484  7.69230769] tableau obtenu à partir du code ci-dessus classe 1
                    #[15.74074074  7.95454545  9.09090909 33.33333333] classe 2
                    #[13.70262391 11.66666667  5.26315789  0.        ]] classe 3


for classe_Tableau_femme,classe_femme in enumerate(classe):
    for age_Tableau_femme,(age_min, age_max) in enumerate(age):

        data_femme_Survie = data_Titanic[
            (data_Titanic['Sex'] == "female") &
            (data_Titanic['Pclass'] == classe_femme) &
            (data_Titanic['Age'] >= age_min) &
            (data_Titanic['Age'] <= age_max)
        ]
        if len(data_femme_Survie) > 0:
            Survie_femme[classe_Tableau_femme, age_Tableau_femme] = data_femme_Survie['Survived'].mean() * 100
            femme_survie = data_femme_Survie['Survived'].mean() * 100 
        else:
            femme_survie = 0
        print("Classe:", classe_femme, "Âge >", age_min, "-", age_max, ":", femme_survie, "%")
        Survie_femme[classe_Tableau_femme, age_Tableau_femme] = femme_survie

print(Survie_femme)#[[ 96.80851064  97.5         96.875      100.        ] tableau obtenu à partir du code ci-dessus classe 1
                   #[ 92.10526316  90.          85.71428571   0.        ] classe 2
                   #[ 50.          50.          10.          50.        ]] classe 3

Age_Utilisateur = int(input("Entrez votre âge : "))

if Age_Utilisateur < 20:
    Index_Colonne = 0
elif Age_Utilisateur < 40:
    Index_Colonne = 1
elif Age_Utilisateur <= 60:
    Index_Colonne = 2
elif Age_Utilisateur > 60:
    Index_Colonne = 3

Classe_Utilisateur = int(input("Entrez votre classe (1, 2 ou 3) : "))
if Classe_Utilisateur == 1:
    Index_Ligne = 0
elif Classe_Utilisateur == 2:
    Index_Ligne = 1
elif Classe_Utilisateur == 3:
    Index_Ligne = 2

Probabilite_Survie_homme = round(Survie_homme[Index_Ligne, Index_Colonne],3)
Probabilite_Survie_femme = round(Survie_femme[Index_Ligne, Index_Colonne],3)

Sex_Utilisateur = input("Entrez votre sexe:"      )
if Sex_Utilisateur.lower() == "homme":    
    print("Votre % de survie est estimé à :", Probabilite_Survie_homme, "%")
elif Sex_Utilisateur.lower() == "femme":
    print("Votre % de survie est estimé à :", Probabilite_Survie_femme, "%")
