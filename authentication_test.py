import os
import requests
from requests.adapters import HTTPAdapter
from fastapi import HTTPException, status
from urllib3.util.retry import Retry
import sys
import urllib
import time

# définition de l'adresse de l'API
sortie = ""
url = "http://172.50.0.3:8000/users/me"
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Authentication tests
time.sleep(6)
#Test if Alice has access to the API
def test_account1():
    # requête
    r = session.get(url, auth=("alice", "wonderland"), proxies=urllib.request.getproxies(), timeout=(10,3))

    # statut de la requête  
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 1 - alice:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()

    return output



#Test if Bob has access to the API
def test_account2():
    # requête
    r = session.get(url, auth=("bob", "builder"), proxies=urllib.request.getproxies(), timeout=(10,3))

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 2 - bob:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output



#Test if Clementine has access to the API
def test_account3():
    # requête
    r = session.get(url, auth=("clementine", "mandarine"), proxies=urllib.request.getproxies(), timeout=(10,3))

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 3 - clementine:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output
    

#Test if Jeff has not access to the API
def test_account4():
    # requête
    r = session.get(url, auth=("jeff", "hello"), proxies=urllib.request.getproxies(), timeout=(10,3))

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == status.HTTP_401_UNAUTHORIZED:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    output = "Test 4 - jeff:\nStatus code = " + str(status_code) + " et Test status = " + test_status + "\n"
    r.close()
    return output


sortie = "Authentication\n" + test_account1() + test_account2() + test_account3() + test_account4() + "\n"

# impression dans un fichier
#if os.environ.get('LOG') == 1:
with open('api_test.log', 'a') as file:
        file.write(sortie)

session.cookies.keys()