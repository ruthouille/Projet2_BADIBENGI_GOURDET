# Projet2_BADIBENGI_GOURDET
Depo for our second datascience project

Commandes pour construire le container docker dans le répertoire racine :

1) Renommer le répertoire "api_churn"

2) Utiliser la commande suivante: 
• docker build . -t api_churn

Commandes pour ajouter l'API sur dockerhub :
• docker login --username lgourdet--password ...
• docker tag api_churn lgourdet/api_churn
• docker image push lgourdet/api_churn:latest

Kubernetes
Pour permettre le déploiement de l'API sur 3 Pods un fichier de déploiement, un service et un ingress
ont été créés dans le répertoire.

Commandes pour construire le déploiement k8s :

• minikube start
• minikube addons enable ingress
• minikube dashboard --url=true
• VM : kubectl proxy --address='0.0.0.0' --disable-filter=true
• kubectl create -f deployment.yml
• kubectl create -f service.yml
• kubectl create -f ingress.yml
• VM : ouvrir un tunnel : 
ssh -i "data_enginering_machine.pem" ubuntu@(ip VM) -fNL 
8000:192.168.49.2:80
• API disponible sur : http://127.0.0.1:8000/docs
• VM : Dashboard k8s disponible sur : 
http://(ip_VM):8001/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy
