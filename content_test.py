import os
import requests
from requests.adapters import HTTPAdapter
from fastapi import HTTPException, status
from urllib3.util.retry import Retry
import sys
import urllib
from churn_de_badibengi_gourdet import  y_pred_test_knn, y_pred_clf, y_pred, accuracy_knn, accuracy_clf, accuracy_lr, balance_accuracy, coeff, intercept, odd_ratios, tn, fp, fn, tp


# définition de l'adresse de l'API
# TO BE MODIFY FOR DOCKER-COMPOSE
api_address = '127.0.0.1'
# port de l'API
api_port = 8000
adr= "http://127.0.0.1:8000"
sortie = ""

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


# Authorization tests

#Test the content for KNeighbors, DecisionTree and LogisticRegression predictions with the account of alice
def test_knn_predict_alice():
    url = adr + "/kneighbors/predict"
    # requête
    r = requests.get(url, auth=("alice", "wonderland"))
    
    l = []

    # format json de la reponse 
    results = r.json()

    for i in range(0,y_pred_test_knn.shape[0]):
        l.append(int(y_pred_test_knn[i]))

    # affichage des résultats
    if results == l[:10]:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 1 knn predict - alice:\nContent test status = " + test_status + "\n"

    r.close()

    return output


def test_dt_predict_alice():
    url = adr + "/dtree/predict"
    # requête
    r = requests.get(url, auth=("alice", "wonderland"))
    l = []

    # format json de la reponse    
    results = r.json()

    for i in range(y_pred_clf.shape[0]):
        l.append(int(y_pred_clf[i]))

    # affichage des résultats
    if results == l[:10]:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 2 dt predict - alice:\nContent test status = " + test_status + "\n"

    r.close()

    return output


def test_lr_predict_alice():
    url = adr + "/lr/predict"
    # requête
    r = requests.get(url, auth=("alice", "wonderland"))
    l = []

    # format json de la reponse    
    results = r.json()

    for i in range(0,y_pred.shape[0]):
        l.append(int(y_pred[i]))

    # affichage des résultats
    if results == l[:10]:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 3 lr predict - alice:\nContent test status = " + test_status + "\n"

    r.close()

    return output


#Test the content for KNeighbors, DecisionTree and LogisticRegression accuracy with the account of bob
def test_knn_accuracy_bob():
    url = adr + "/kneighbors/accuracy"

    # requête
    r = requests.get(url, auth=("bob", "builder"))

    # format json de la reponse  
    results = r.json()

    # affichage des résultats
    if results == accuracy_knn:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 4 knn accuracy - bob:\nContent test status = " + test_status + "\n"
    r.close()
    return output


def test_dt_accuracy_bob():
    url = adr + "/dtree/accuracy"

    # requête
    r = requests.get(url, auth=("bob", "builder"))

    # format json de la reponse  
    results = r.json()

    # affichage des résultats
    if round(results) == round(accuracy_clf):
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 5 dt accuracy - bob:\nContent test status = " + test_status + "\n"
    r.close()
    return output


def test_lr_accuracy_bob():
    url = adr + "/lr/accuracy"

    # requête
    r = requests.get(url, auth=("bob", "builder"))

    # format json de la reponse  
    results = r.json()

    # affichage des résultats
    if results == accuracy_lr:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 6 lr accuracy - bob:\nContent test status = " + test_status + "\n"
    r.close()
    return output


#Test the content for the LogisticRegression balance accuracy, coefficient, odd ratio and intercept with the account of clementine
def test_lr_baccuracy_clem():
    url = adr + "/lr/baccuracy"

    # requête
    r = requests.get(url, auth=("clementine", "mandarine"))

   # format json de la reponse  
    results = r.json()

    # affichage des résultats
    if results == balance_accuracy:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 7 lr balance acc - clementine:\nContent test status = " + test_status + "\n"
    r.close()
    return output


def test_lr_coeff_clem():
    url = adr + "/lr/coeff"

    # requête
    r = requests.get(url, auth=("clementine", "mandarine"))
    l = []

    # format json de la reponse  
    results = r.json()

    for i in range(0,coeff.shape[1]):
        l.append(coeff[0][i])

    # affichage des résultats
    if results == l:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 8 lr coefficient - clementine:\nContent test status = " + test_status + "\n"
    r.close()
    return output


def test_lr_inter_clem():
    url = adr + "/lr/intercept"

    # requête
    r = requests.get(url, auth=("clementine", "mandarine"))

   # format json de la reponse  
    results = r.json()

    # affichage des résultats
    if results == intercept[0]:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 9 lr intercept - clementine:\nContent test status = " + test_status + "\n"
    r.close()
    return output


def test_lr_oddr_clem():
    url = adr + "/lr/odd_ratio"

    # requête
    r = requests.get(url, auth=("clementine", "mandarine"))
    l = []

    # format json de la reponse  
    results = r.json()

    for i in range(0,odd_ratios.shape[1]):
        l.append(odd_ratios[0][i])

    # affichage des résultats
    if results == l:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 10 lr odd ratio - clementine:\nContent test status = " + test_status + "\n"
    r.close()
    return output


sortie = "Content\n" + test_knn_predict_alice() + test_dt_predict_alice() + test_lr_predict_alice() + test_knn_accuracy_bob() + test_dt_accuracy_bob() + test_lr_accuracy_bob() + test_lr_baccuracy_clem() + test_lr_coeff_clem() + test_lr_inter_clem() + test_lr_oddr_clem() + "\n"

# impression dans un fichier
#if os.environ.get('LOG') == 1:
with open('api_test.log', 'a') as file:
        file.write(sortie)
