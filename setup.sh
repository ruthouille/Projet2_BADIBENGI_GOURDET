#!/bin/bash

docker image pull datascientest/fastapi:1.0.0

mkdir api_myapi
mkdir authen_test
mkdir autho_test
mkdir content_test

cp churn_de_badibengi_gourdet.py churn_de_badibengi_gourdet2.py

cp requirements.txt requirements2.txt
cp requirements.txt requirements3.txt
cp requirements.txt requirements4.txt


mv MyAPI.py api_myapi
mv churn_de_badibengi_gourdet.py api_myapi
mv authentication_test.py authen_test
mv authorization_test.py autho_test
mv content_test.py content_test
mv churn_de_badibengi_gourdet2.py content_test

mv requirements3.txt autho_test

mv requirements.txt api_myapi
mv requirements2.txt authen_test

mv requirements4.txt content_test


mv Dockerfile api_myapi
mv Dockerfile2 authen_test
mv Dockerfile3 autho_test
mv Dockerfile4 content_test

mv authen_test/Dockerfile2 authen_test/Dockerfile
mv autho_test/Dockerfile3 autho_test/Dockerfile
mv content_test/Dockerfile4 content_test/Dockerfile
mv content_test/churn_de_badibengi_gourdet2.py content_test/churn_de_badibengi_gourdet.py


mv authen_test/requirements2.txt authen_test/requirements.txt
mv autho_test/requirements3.txt autho_test/requirements.txt
mv content_test/requirements4.txt content_test/requirements.txt


#cd api_myapi
#docker image build . -t ml_api:1.0.0

#cd ../authen_test
#docker image build . -t test1:1.0.0

#cd ../autho_test
#docker image build . -t test2:1.0.0

#cd ../content_test
#docker image build . -t test3:1.0.0

#cd ../

mkdir data
docker volume create my_vol

docker-compose up