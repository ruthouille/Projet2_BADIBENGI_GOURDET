# Projet2_BADIBENGI_GOURDET
Depo for our second datascience project

#Description:
    L'API contient 13 chemins:
        - "/": est le "endpoint" qui verifie que l'API fonctionne correctement et retourne "Welcome to our API"

        - "/users/me": retourne le nom de l'utilisateur qui est connecté
        - "/kneighbors/predict": retourne les predictions KNeighborsClassifier de notre modèle
        - "/dtree/predict": retourne les predictions DecisionTreeClassifier de notre modèle
        - "/lr/predict": retourne les predictions LogisticRegression de notre modèle

        - "/kneighbors/accuracy": retourne l'accuracy du KNeighborsClassifier de notre modèle
        - "/dtree/accuracy": retourne l'accuracy du DecisionTreeClassifier de notre modèle
        - "/lr/accuracy": retourne l'accuracy de la LogisticRegression de notre modèle
        - "/lr/baccuracy": retourne la balance accuracy de la LogisticRegression de notre modèle

        - "/lr/coeff": retourne le coefficient de notre modèle
        - "/lr/intercept": retourne l'intercept de notre modèle
        - "/lr/odd_ratio": retourne le odd ratio de notre modèle
        - "/lr/cfm": retourne la matrice de confusion de notre modèle


#Instructions:
- Etape 1:
    Afin de lancer l'api en même temps que les tests, il faut lancer la commande suivante:
        sh setup.sh
    Cela va lancer un docker-compose, et creer 4 containers:
        - l'API
        - Test 1: qui est le test d'authentification
        - Test 2: qui est le test d'autorisation
        - Test 3: qui verifie que les bonnes valeurs sont obtenues 
    