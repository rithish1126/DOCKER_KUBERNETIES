# Amit's Review

Docker TASK 1

* Write a simple airflow dag to connect with db(postgres) and add entry in db for each execution (Time of dag execution)
* Add the given dag into the container and install dependencies.
* Use docker compose to launch airflow and postgres
* Schedule the dag
* Validate entry in postgres

## Approach:

* Used the official airflow docker compose file available online.
* Made a postgres connection in the Airflow UI.
* Used Postgres operator for creating table and inserting values in it.

Kubernetes Task 2

* Create deployment and service for above airflow and postgres (you can use postgres helm chart for postgres deployment)
* Deploy airflow and postgres
* Schedule the dag
* Validate entry in postgres

## Aproach:

* installed minikube to create kubernetes cluster.
* Created a pod containing postgres container using "postgres-deployment" file.
* Got into the clusters that were created using "minikube ssh"
* then executed the created postgres pod in the cluster
* ran some commands to install airflow and intialise a database and user.
* Created a postgres service to access postgres, 
* ran an airflow deployment file to create a pod containing airflow container 
* created an airflow service to access the airflow container inside the pod.
* Went inside the airflow container and created dag with the same code.
* Accessed the airflow webserver on localhost using minikube service airflow

# Dhruv's Review

Docker Task 1
* Write a simple airflow dag to connect with db(postgres) and add entry in db for each execution (Time of dag execution)
* Add the given dag into the container and install dependencies.
* Use docker compose to launch airflow and postgres
* Schedule the dag
* Validate entry in postgres

# Approach

* Used the official airflow docker compose file available online.
* Made a postgres connection in the Airflow UI.
* Used Postgres operator for creating table and inserting values in it.


Kubernetes Task 2

* Create deployment and service for above airflow and postgres (you can use postgres helm chart for postgres deployment)
* Deploy airflow and postgres
* Schedule the dag
* Validate entry in postgres

## Approach

* Installed minikube to create kubernetes cluster.
* Created a pod containing postgres container using postgres deployment file.
* Ran a bash script to install airflow and intialise a database and user in the postgrest container
* Created a postgres service to access postgres, ran an airflow deployment file to create a pod containing airflow container and finally created an airflow service to access the airflow container inside the pod.
* Went inside the airflow container and created dag containing code
* Accessed the airflow webserver on localhost using minikube service airflow
