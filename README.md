# Projet2_BADIBENGI_GOURDET
Depo for our second datascience project

API

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
    Si on veut lancer l'api seule, il est possible de lancer la commande suivante:
    • docker build . -t api_churn:latest

    Cette commande va créer l'image de notre API à partir de notre Dockerfile. 

    On pourra lancer la commande suivante afin de lancer notre API:
    • docker container run -it api_churn:latest

    Ainsi, notre API sera en marche.


- Etape 2:
    Afin de lancer l'api en même temps que les tests, il faut lancer la commande suivante:
        • sh setup.sh
    Cela va lancer un docker-compose, et creer 4 containers:
        - l'API
        - Test 1: qui est le test d'authentification
        - Test 2: qui est le test d'autorisation
        - Test 3: qui verifie que les bonnes valeurs sont obtenues 
    
- Dockerfile permet de créer l'image de notre API
- Dockerfile 2 permet de créer l'image du test d'authentification
- Dockerfile 3 permet de créer l'image du test d'authorisation
- Dockerfile 2 permet de créer l'image du test des valeurs


Kubernetes

Attention, les images ont déjà été ajouté sur Dockerhuh, on peut voir le nom des images dans les fichiers my_deployment.yml ainsi que my_service.yml. Donc, tout a été fait au préalable.

Nous avons utilisé les commandes suivantes pour ajouter l'API sur Dockerhub :
• docker login --username lgourdet--password ...
• docker tag api_churn lgourdet/api_churn
• docker image push lgourdet/api_churn:latest

Pour permettre le déploiement de l'API sur 3 Pods un fichier de déploiement, un service et un ingress
ont été créés dans le répertoire.

Afin d'effectuer le déploiement k8s nous avons utilisé les commandes suivantes:

• minikube start
• minikube addons enable ingress
• minikube dashboard --url=true
• VM : kubectl proxy --address='0.0.0.0' --disable-filter=true
• kubectl create -f my_deployment.yml
• kubectl create -f my_service.yml
• kubectl create -f my_ingress.yml
• VM : ouvrir un tunnel : 
ssh -i "data_enginering_machine.pem" ubuntu@(ip VM) -fNL 
8000:192.168.49.2:80
• API disponible sur : http://127.0.0.1:8000/docs
• VM : Dashboard k8s disponible sur : 
http://(ip_VM):8001/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy
