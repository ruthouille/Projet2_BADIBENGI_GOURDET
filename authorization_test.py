import os
import requests
from requests.adapters import HTTPAdapter
from fastapi import HTTPException, status
from urllib3.util.retry import Retry
import sys
import urllib

# définition de l'adresse de l'API
api_port = 8000
adr= "http://172.50.0.6:8000"
sortie = ""

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


# Authorization tests

#Test if Alice has access to KNeighbors, DecisionTree and LogisticRegression predictions
def test_knn_predict_alice():
    url = adr + "/kneighbors/predict"
    # requête
    r = requests.get(url, auth=("alice", "wonderland"))
    # statut de la requête
    
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 1 knn predict - alice:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()

    return output


def test_dt_predict_alice():
    url = adr + "/dtree/predict"
    # requête
    r = requests.get(url, auth=("alice", "wonderland"))
    # statut de la requête
    
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 2 dt predict - alice:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()

    return output


def test_lr_predict_alice():
    url = adr + "/lr/predict"
    # requête
    r = requests.get(url, auth=("alice", "wonderland"))
    # statut de la requête
    
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 3 lr predict - alice:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()

    return output


#Test if Bob has access to KNeighbors, DecisionTree and LogisticRegression accuracy
def test_knn_accuracy_bob():
    url = adr + "/kneighbors/accuracy"

    # requête
    r = requests.get(url, auth=("bob", "builder"))

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 4 knn accuracy - bob:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output


def test_dt_accuracy_bob():
    url = adr + "/dtree/accuracy"

    # requête
    r = requests.get(url, auth=("bob", "builder"))

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 5 dt accuracy - bob:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output


def test_lr_accuracy_bob():
    url = adr + "/lr/accuracy"

    # requête
    r = requests.get(url, auth=("bob", "builder"))

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 6 lr accuracy - bob:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output



#Test if Clementine has access to the LogisticRegression balance accuracy, coefficient and intercept
def test_lr_baccuracy_clem():
    url = adr + "/lr/baccuracy"

    # requête
    r = requests.get(url, auth=("clementine", "mandarine"))

    # statut de la requête
    
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 7 lr balance acc - clementine:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output


def test_lr_coeff_clem():
    url = adr + "/lr/coeff"

    # requête
    r = requests.get(url, auth=("clementine", "mandarine"))

    # statut de la requête
    
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 8 lr coeff - clementine:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output


def test_lr_inter_clem():
    url = adr + "/lr/intercept"

    # requête
    r = requests.get(url, auth=("clementine", "mandarine"))

    # statut de la requête
    
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 9 lr intercept - clementine:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output


#Test if Jeff has not access to the odd ration and the confusion matrice results
def test_lr_oddr_jeff():
    url = adr + "/lr/odd_ratio"

    # requête
    r = requests.get(url, auth=("jeff", "hello"))

    # statut de la requête
    
    status_code = r.status_code

    # affichage des résultats
    if status_code == status.HTTP_401_UNAUTHORIZED:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 10 odd ratio - jeff:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output


def test_lr_cfm_jeff():
    url = adr + "/lr/cfm"

    # requête
    r = requests.get(url, auth=("jeff", "hello"))

    # statut de la requête
    
    status_code = r.status_code

    # affichage des résultats
    if status_code == status.HTTP_401_UNAUTHORIZED:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 11 cfm - jeff:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output


sortie = "Authorization\n" + test_knn_predict_alice() + test_dt_predict_alice() + test_lr_predict_alice() + test_knn_accuracy_bob() + test_dt_accuracy_bob() + test_lr_accuracy_bob() + test_lr_baccuracy_clem() + test_lr_coeff_clem() + test_lr_inter_clem() + test_lr_oddr_jeff() + test_lr_cfm_jeff() + "\n"

# impression dans un fichier
#if os.environ.get('LOG') == 1:
with open('api_test.log', 'a') as file:
        file.write(sortie)
