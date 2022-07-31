import os
import requests
from requests.adapters import HTTPAdapter
from fastapi import HTTPException, status
from urllib3.util.retry import Retry
import sys
import urllib

# définition de l'adresse de l'API
api_address = '127.0.0.1'
# port de l'API
api_port = 8000

sortie = ""
url = "http://127.0.0.1:8000/users/me"
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)


def test_account1():
    # requête
    r = requests.get(url, auth=("alice", "wonderland"))
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



def test_account2():
    # requête
    r = requests.get(url, auth=("bob", "builder"))

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



def test_account3():
    # requête
    r = requests.get(url, auth=("clementine", "mandarine"))

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
    

def test_account4():
    # requête
    r = requests.get(url, auth=("jeff", "hello"))

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

test_account1()