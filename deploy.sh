#!/bin/bash

project_name=1385plague 
#build server
docker build -t ${project_name}_server server

#build days_api
docker build -t ${project_name}_days days_api

#build outcome_api
docker build -t ${project_name}_outcome outcome_api

#build network
docker network create ${project_name}_network 

#run containers
docker run -d -p 5000:5000 --name ${project_name}_server --network ${project_name}_network ${project_name}_server
docker run -d -p 5001:5001 --name ${project_name}_days --network ${project_name}_network ${project_name}_days
docker run -d -p 5002:5002 --name ${project_name}_outcome --network ${project_name}_network ${project_name}_outcome