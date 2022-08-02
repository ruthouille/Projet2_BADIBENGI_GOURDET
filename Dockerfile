FROM ubuntu:20.04

ADD api_myapi/requirements.txt api_myapi/MyAPI.py api_myapi/churn_de_badibengi_gourdet.py ./

RUN apt update && apt install python3-pip -y && pip install -r requirements.txt

EXPOSE 8000
CMD uvicorn MyAPI:api

