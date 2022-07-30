from httplib2 import Authentication
from numpy import kaiser
import secrets
import pandas as pd
from re import sub
from unicodedata import name
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from Myfunction import extract_questions, extract_subject
from typing import Optional
from random import seed
from random import choice
from random import shuffle
import numpy as np
from pydantic import BaseModel
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import tree
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression 
import numpy as np 
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score




df = pd.read_csv("https://assets-datascientest.s3-eu-west-1.amazonaws.com/de/total/churn.csv", index_col="customerID")


df.isna().sum()

print("Il y a", df.isna().any().sum(), "valeur manquante")

"""> Aucune valeur manquante n'a été détectée.

*   Détection des valeurs abérrantes
"""

# On a fait la même chose pour toutes les autres colonnes

df.loc[(df["SeniorCitizen"] != 0 ) & (df["SeniorCitizen"] != 1)]
df.loc[(df["StreamingMovies"] != "Yes" ) & (df["StreamingMovies"] != "No") & (df["StreamingMovies"] != "No internet service")]

"""*   On remplace les valeurs "Yes", "No", "No internet service", "No phone service", "Femal", "Male", "Fiber optic" et "DSL" par 1 ou 0.

*   De plus, on s'interesse à la colonne "Contract" qui contient les valeurs "Two year", "Month-to-month", "One year". On décide donc de remplacer "Two year" par 730, car il y a 730 jours dans deux années, "Month-to-month" est remplacé par 30 jours et enfin, "One year" par 365 jours.
"""

#On remplace les valeurs "Yes", "No", "No internet service", "No phone service", "Femal", "Male", "Fiber optic" et "DSL" par 1 ou 0.
df = df.replace(to_replace = ["Yes", "No", "No internet service", "No phone service", "Female", "Male", "Fiber optic", "DSL"],
                   value=[1, 0, 0, 0,1,0,1,1])

#On remplace "Two year" par 730 et "Month-to-month" par 30
df = df.replace(to_replace=["Two year", "Month-to-month", "One year"], value=[730, 30, 365])


#On verifie que seul ces trois valeurs sont présentes dans cette colonne
df.loc[(df["Contract"] != 730 ) & (df["Contract"] != 30) & (df["Contract"] != 365)]

df.head()

"""
*  Pour la colonne "PaymentMethod" nous allons utiliser la technique de l'encodage one-hot, grâce à la fonction OneHotEncoder de sklearn.preprocessing. Cette fonction va donc nous permettre d'encoder les valeurs de cette colonne par 1 ou 0.

"""

df_new = df.copy()

transformer = make_column_transformer(
    (OneHotEncoder(), ['PaymentMethod']),
    remainder='passthrough')

transformed = transformer.fit_transform(df_new)
df_new = pd.DataFrame(transformed,columns=transformer.get_feature_names())

#On renomme le nom des nouvelles colonnes encodées
dico = {"onehotencoder__x0_Bank transfer (automatic)": "Bank transfer (automatic)",
        "onehotencoder__x0_Credit card (automatic)": "Credit card (automatic)",
        "onehotencoder__x0_Electronic check": "Electronic check",
        "onehotencoder__x0_Mailed check": "Mailed check"}
df_new = df_new.rename(dico, axis=1)

#On change le type des nouvelles colonnes
dico2 = {"Bank transfer (automatic)":"int",
         "Credit card (automatic)":"int",
         "Electronic check":"int",
         "Mailed check":"int"}
df_new = df_new.astype(dico2)

df_new.index = df.index
df_new.head(5)

"""

*   Les valeurs de la colonne "TotalCharges" ne sont pas toutes au même format. En effet, cette colonne est au format str et on y trouve des valeurs avec des points, ainsi que des valeurs sans points. Nous ne pouvons donc pas convertir cette colonne directement en utilisant une fonction telle que astype car cela nous génère une erreur. 

*   Nous allons donc convertir cette colonne au format numérique en utilisant "to_numeric".



"""

y = df_new

y = pd.to_numeric(y["TotalCharges"], errors='coerce')
df_new["TotalCharges"] = y

#On verifie encore une fois s'il y a des valeurs manquantes
df_new.isna().sum()

"""*   Nous pouvons remarquer que la colonne "TotalCharges" contient 10 valeurs manquantes.


"""

# On affiche les lignes avec des valeurs manquantes
df_new[df_new.isnull().any(axis=1)]

"""*   On remplace les valeurs manquantes de la colonne "TotalCharges" par sa mediane."""

#On remplace les valeurs manquantes par la valeur 0
df_new["TotalCharges"] = df_new["TotalCharges"].fillna(df_new["TotalCharges"].median())

#On affiche les lignes qui contiennent des valeurs manquantes
df_new[df_new.isnull().any(axis=1)]




# Application d'un algorithme de Régression Logistique

X = df_new.drop(["Churn"], axis = 1)

y = df_new["Churn"]
y=y.astype('int')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state = 42, stratify = y)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


#Classification non-linéaire: modèle des K-Nearest Neighbors
# Instanciation du modèle
knn = KNeighborsClassifier(n_neighbors = 6)

# Entraînement du modèle sur le jeu d'entraînement
knn.fit(X_train, y_train)

# Prédiction sur les données de test
y_pred_test_knn = knn.predict(X_test)

# Affichage des 10 premières prédictions
print(y_pred_test_knn[:10])

# On créer un decision tree de type Classifier car on est dans une problématique d'apprentissage supervisé de type régression logistique (classification)
clf = tree.DecisionTreeClassifier()

# On entraîne notre modèle
clf = clf.fit(X_train, y_train)

# On decide de faire une predicition pour notre variable test
y_pred_clf = clf.predict(X_test)

# On affiche l'accuracy de notre decision tree
print("Accuracy:", metrics.accuracy_score(y_test, y_pred_clf))

#Entraînement du modèle 

# A partir du module linear_model de la librairie scikit learn on importe la fonction LogisticRegression

from sklearn.linear_model import LogisticRegression 
import numpy as np 
#On instancie le modèle et on l'entraîne 
model_log = LogisticRegression(solver="newton-cg").fit(X_train, y_train)

#On prédit les y à partir de X_test et X_train
y_pred = model_log.predict(X_test)

#On affiche les coefficients obtenus 
coeff = model_log.coef_
#On affiche la constance 
intercept = model_log.intercept_ 

#On calcule les odd ratios 
odd_ratios = np.exp(model_log.coef_)

#On crée un dataframe qui combine à la fois variables, oddrations et coefficients

resultats = pd.DataFrame(X.columns, columns=['Variables'])
resultats['Coefficients'] = model_log.coef_.tolist()[0]
resultats['Odd_Ratios'] = np.exp(model_log.coef_).tolist()[0]

#On choisit d'afficher les variables avec le coefficient le plus élevé et le plus faible 
resultats.loc[(resultats['Odd_Ratios']== max(resultats["Odd_Ratios"]))|(resultats['Odd_Ratios']== min(resultats["Odd_Ratios"]))]


#Matrice de confusion 
# Insérez votre code

confusion_matrix(y_test, y_pred)

tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
print("\n Vrais négatifs:",tn,"\n Faux positifs:",fp,"\n Faux négatifs:",fn,"\n Vrais positifs:",tp)

#Accuracy score 

print("Accuracy score: " ,accuracy_score(y_test, y_pred))

# On importe la fonction balanced_accuracy_score du module metrics de la librairie Scikit Learn



# On vérifie la répartition des classes

print("Répartition des classes : \n",y.value_counts(),"\n")

# La classe négative est surreprésentée par rapport à la classe 1.

# On affiche la balanced accuracy du modèle 

print("Balanced accuracy:",balanced_accuracy_score(y_test,y_pred))

# Les résultats obtenus avec la balanced accuracy sont  plus faibles que ceux obtenus avec 
# l'accuracy : 0.70 contre 0.79. 

# On peut donc dire que le modèle souffre du déséquilibre de classes.




#My API


api = FastAPI(title="Modèle de machine Learning - Churn", openapi_tags=[
    {
        'name': 'Home',
        'description': 'Confirm that the API works'
    }
])

# To use a basic authentication
security = HTTPBasic()
pswd_db = {"alice": "wonderland",
        "bob": "builder",
        "clementine": "mandarine"}


def get_username(credentials: HTTPBasicCredentials = Depends(security)):
    for i in pswd_db.keys():
        if i == credentials.username:
            correct_username = secrets.compare_digest(credentials.username, i)
            correct_password = secrets.compare_digest(credentials.password, pswd_db[i])
    
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


# GET '/' returns a Welcome to verify that the API works
@api.get("/", tags=["Home"])
def get_index():
    """Endpoint to verify that the API works
    """
    return {"data": "Welcome to our survey"}  


@api.get("/users/me", tags=["Account"])
def read_current_user(username: str = Depends(get_username)):
    """Returns the name of the connected user account
    """
    return {"username": username}