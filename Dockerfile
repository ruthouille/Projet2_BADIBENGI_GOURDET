FROM ubuntu:20.04

ADD requirements.txt MyAPI.py churn_de_badibengi_gourdet.py ./

RUN apt update && apt install python3-pip -y && pip3 install -r requirements.txt

EXPOSE 8000
CMD uvicorn MyAPI:api --host 172.50.0.3