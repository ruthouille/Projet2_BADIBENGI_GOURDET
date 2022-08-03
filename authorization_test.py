import os
import requests
from requests.adapters import HTTPAdapter
from fastapi import HTTPException, status
from urllib3.util.retry import Retry
import sys
import urllib


# définition de l'adresse de l'API
api_port = 8000
adr= "http://172.50.0.3:8000"
sortie = ""

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)



# Authorization tests

#Test if Alice has access to KNeighbors, DecisionTree and LogisticRegression predictions
def test_knn_predict_alice_auth():

    url = adr + "/kneighbors/predict"
    # requête
    
    r = session.get(url, auth=("alice", "wonderland"), proxies=urllib.request.getproxies(), timeout=(10,3))
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



def test_dt_predict_alice_auth():
    url = adr + "/dtree/predict"
    # requête
    r = session.get(url, auth=("alice", "wonderland"), proxies=urllib.request.getproxies(), timeout=(10,3))
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


def test_lr_predict_alice_auth():
    url = adr + "/lr/predict"
    # requête
    r = session.get(url, auth=("alice", "wonderland"), proxies=urllib.request.getproxies(), timeout=(10,3))
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
def test_knn_accuracy_bob_auth():
    url = adr + "/kneighbors/accuracy"

    # requête
    r = session.get(url, auth=("bob", "builder"), proxies=urllib.request.getproxies(), timeout=(10,3))

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


def test_dt_accuracy_bob_auth():
    url = adr + "/dtree/accuracy"

    # requête
    r = session.get(url, auth=("bob", "builder"), proxies=urllib.request.getproxies(), timeout=(10,3))

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


def test_lr_accuracy_bob_auth():
    url = adr + "/lr/accuracy"

    # requête
    r = session.get(url, auth=("bob", "builder"), proxies=urllib.request.getproxies(), timeout=(10,3))

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
def test_lr_baccuracy_clem_auth():
    url = adr + "/lr/baccuracy"

    # requête
    r = session.get(url, auth=("clementine", "mandarine"), proxies=urllib.request.getproxies(), timeout=(10,3))

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


def test_lr_coeff_clem_auth():
    url = adr + "/lr/coeff"

    # requête
    r = session.get(url, auth=("clementine", "mandarine"), proxies=urllib.request.getproxies(), timeout=(10,3))

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


def test_lr_inter_clem_auth():
    url = adr + "/lr/intercept"

    # requête
    r = session.get(url, auth=("clementine", "mandarine"), proxies=urllib.request.getproxies(), timeout=(10,3))

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
def test_lr_oddr_jeff_auth():
    url = adr + "/lr/odd_ratio"

    # requête
    r = session.get(url, auth=("jeff", "hello"), proxies=urllib.request.getproxies(), timeout=(10,3))

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


def test_lr_cfm_jeff_auth():
    url = adr + "/lr/cfm"

    # requête
    r = session.get(url, auth=("jeff", "hello"), proxies=urllib.request.getproxies(), timeout=(10,3))

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


sortie = "Authorization\n" + test_knn_predict_alice_auth() + test_dt_predict_alice_auth() + test_lr_predict_alice_auth() + test_knn_accuracy_bob_auth() + test_dt_accuracy_bob_auth() + test_lr_accuracy_bob_auth() + test_lr_baccuracy_clem_auth() + test_lr_coeff_clem_auth() + test_lr_inter_clem_auth() + test_lr_oddr_jeff_auth() + test_lr_cfm_jeff_auth() + "\n"

# impression dans un fichier
#if os.environ.get('LOG') == 1:
with open('api_test.log', 'a') as file:
        file.write(sortie)
