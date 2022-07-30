from httplib2 import Authentication
import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import json
from pydantic import BaseModel
from churn_de_badibengi_gourdet import  y_pred_test_knn, y_pred_clf, y_pred, accuracy_knn, accuracy_clf, accuracy_lr, balance_accuracy, coeff, intercept, odd_ratios, tn, fp, fn, tp


#My API


api = FastAPI(title="Modèle de machine Learning - Churn, for a supervised learning", openapi_tags=[
    {
        'name': 'Home',
        'description': 'Confirm that the API works'
    },
    {
        'name': 'KNeighborsClassifier',
        'description': 'K nearest neighbors algorithm'
    },
    {
        'name': 'DecisionTreeClassifier',
        'description': 'Decision tree algorithm'
    },
    {
        'name': 'LogisticRegression',
        'description': 'Logistic regression algorithm'
    },
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
    return {"data": "Welcome to our API"}  

# GET '/users/me' returns the name of the user connected
@api.get("/users/me", tags=["Home"])
def read_current_user(username: str = Depends(get_username)):
    """Returns the name of the connected user account
    """
    return {"username": username}

# Predictions

# GET '/kneighbors/predict' returns the prediction
@api.get("/kneighbors/predict", tags=["KNeighborsClassifier"])
def read_kneighbors_predict(username: str = Depends(get_username)):
    """Returns the the 10 first KNeighborsClassifier predictions
    """
    l = []
    for i in range(0,y_pred_test_knn.shape[0]):
       l.append(int(y_pred_test_knn[i]))

    return l[:10]

# GET '/dtree/predict' returns the prediction
@api.get("/dtree/predict", tags=["DecisionTreeClassifier"])
def read_dtree_predict(username: str = Depends(get_username)):
    """Returns the 10 first DecisionTreeClassifier predictions
    """
    l = []
    for i in range(y_pred_clf.shape[0]):
       l.append(int(y_pred_clf[i]))
    return l[:10]
    
    

# GET '/lr/predict' returns the prediction
@api.get("/lr/predict", tags=["LogisticRegression"])
def read_lr_predict(username: str = Depends(get_username)):
    """Returns the 10 first LogisticRegression predictions
    """
    l = []
    for i in range(0,y_pred.shape[0]):
       l.append(int(y_pred[i]))

    return l[:10]


#Accuracy

# GET '/kneighbors/accuracy' returns the accuracy
@api.get("/kneighbors/accuracy", tags=["KNeighborsClassifier"])
def read_kneighbors_acc(username: str = Depends(get_username)):
    """Returns the KNeighborsClassifier accuracy
    """
    return accuracy_knn

# GET '/dtree/accuracy' returns the accuracy
@api.get("/dtree/accuracy", tags=["DecisionTreeClassifier"])
def read_dtree_acc(username: str = Depends(get_username)):
    """Returns the DecisionTreeClassifier accuracy
    """
    return accuracy_clf

# GET '/lr/accuracy' returns the accuracy
@api.get("/lr/accuracy", tags=["LogisticRegression"])
def read_lr_acc(username: str = Depends(get_username)):
    """Returns the LogisticRegression accuracy
    """
    return accuracy_lr

# GET '/lr/baccuracy' returns the balance accuracy
@api.get("/lr/baccuracy", tags=["LogisticRegression"])
def read_lr_bacc(username: str = Depends(get_username)):
    """Returns the LogisticRegression balance accuracy
    """
    return balance_accuracy


# Coeff, intercept, odd ratio

# GET '/lr/coeff' returns the coefficients
@api.get("/lr/coeff", tags=["LogisticRegression"])
def read_lr_predict(username: str = Depends(get_username)):
    """Returns the LogisticRegression coefficients
    """
    l = []
    for i in range(0,coeff.shape[1]):
       l.append(coeff[0][i])
   
    return l


# GET '/lr/intercept' returns the intercept
@api.get("/lr/intercept", tags=["LogisticRegression"])
def read_lr_predict(username: str = Depends(get_username)):
    """Returns the LogisticRegression intercept
    """
    
    intercept_json = json.dumps(str(intercept), indent = 4)
    return intercept[0]


# GET '/lr/odd_ratio' returns the odd ratios
@api.get("/lr/odd_ratio", tags=["LogisticRegression"])
def read_lr_predict(username: str = Depends(get_username)):
    """Returns the LogisticRegression odd ratios
    """
    l = []
    for i in range(0,odd_ratios.shape[1]):
       l.append(odd_ratios[0][i])

    return l


# Performance

# Matrice de confusion
 
 # GET '/lr/cfm' returns the confusion matrice
@api.get("/lr/cfm", tags=["LogisticRegression"])
def read_lr_cm(username: str = Depends(get_username)):
    """Returns the confusion matrice
    """
    cfm = {
        "Vrai negatif": int(tn),
        "Faux positif": int(fp),
        "Faux negatif": int(fn),
        "Vrai positif": int(tp)
        }

    cfm_json = json.dumps(str(cfm), indent = 4)

    return cfm_json
