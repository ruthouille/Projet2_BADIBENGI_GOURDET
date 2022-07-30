from httplib2 import Authentication
from numpy import kaiser
import secrets
import pandas as pd
from re import sub
from unicodedata import name
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Optional
from random import seed
from random import choice
from random import shuffle
import numpy as np
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
    """Returns the 10 first KNeighborsClassifier predictions
    """
    return y_pred_test_knn[:10]

# GET '/dtree/predict' returns the prediction
@api.get("/dtree/predict", tags=["DecisionTreeClassifier"])
def read_dtree_predict(username: str = Depends(get_username)):
    """Returns the DecisionTreeClassifier prediction
    """
    return y_pred_clf

# GET '/lr/predict' returns the prediction
@api.get("/lr/predict", tags=["LogisticRegression"])
def read_lr_predict(username: str = Depends(get_username)):
    """Returns the LogisticRegression prediction
    """
    return y_pred


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
    return coeff

# GET '/lr/intercept' returns the intercept
@api.get("/lr/intercept", tags=["LogisticRegression"])
def read_lr_predict(username: str = Depends(get_username)):
    """Returns the LogisticRegression intercept
    """
    return intercept

# GET '/lr/odd_ratio' returns the intercept
@api.get("/lr/odd_ratio", tags=["LogisticRegression"])
def read_lr_predict(username: str = Depends(get_username)):
    """Returns the LogisticRegression odd ratios
    """
    return odd_ratios


# Performance

# Matrice de confusion
 
 # GET '/lr/cfm' returns the confusion matrice
@api.get("/lr/cfm", tags=["LogisticRegression"])
def read_lr_cm(username: str = Depends(get_username)):
    """Returns the confusion matrice
    """
    cfm = {
        "Vrai negatif": tn,
        "Faux positif": fp,
        "Faux negatif": fn,
        "Vrai positif": tp
        }
    return cfm