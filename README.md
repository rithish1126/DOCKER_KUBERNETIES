# DOCKER_KUBERNETIES

# Docker task

1) Write a simple airflow dag to connect with db(postgres) and add entry in db for each execution (Time of dag execution)

SIMPLE AIRFLOW DAG TO CONNECT TO POSTGRES , CREATE TABLE AND INSERT VALUES TO THIS TABLE
```
with DAG(dag_id='postgres_task', start_date=datetime(2022, 1, 1), 
        schedule_interval='*/1 * * * *',  catchup=False) as dag:
        create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres_default',
        sql='''
            CREATE TABLE IF NOT EXISTS postgres_table (
                curr_time TIMESTAMP
            );
        '''
    )
    insert_records = PostgresOperator(
        task_id = 'insert_records',
        postgres_conn_id='postgres_default',
        sql = '''
                INSERT INTO postgres_table VALUES (CURRENT_TIMESTAMP);   
        '''
    )
    
    create_table >> insert_records
```
connection id was made on the airflow UI for postgres called "postgres_default"
## DAG
<img width="1440" alt="Screenshot 2023-06-15 at 4 18 44 PM" src="https://github.com/rithish1126/DOCKER_KUBERNETIES/assets/122535424/3aab92cb-b041-4113-a80e-5dae48e78594">
## Docker Container with the TABLE
<img width="1440" alt="Screenshot 2023-06-15 at 4 07 17 PM" src="https://github.com/rithish1126/DOCKER_KUBERNETIES/assets/122535424/63423804-a788-4801-ad4a-6fab9bd8755b">

# KUBERNETIES TASK
INSTALL MINIKUBE TO START A KUBERNETES CLUSTER

```
brew install minikube
minikube start
```
Using the "postgres-deployment.yaml" file a pod containing postgres container was created. 
```
kubectl apply -f postgres-deployment.yaml

```
Using the "airflow-deployment.yaml" file a pod containing airflow container was made.
```
kubectl apply -f airflow-deployment.yaml
```
Then access the postgres container pod using the following command 
```
minikube ssh
docker exec -it -u root {postgres-id}/bin/bash
```
Add the airflow and python dependecies in this container
```
apt-get -y update
apt-get  -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget 
wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz
tar -xf Python-3.7.12.tgz
cd /Python-3.7.12
./configure --enable-optimizations
make -j $(nproc)
make altinstall
# STEPS TO INSTALL AIRFLOW VERSION 2.5.0
apt-get install libpq-dev
pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"
export AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql://airflow:airflow@localhost:5432/airflow

airflow db init
airflow users create -u airflow -p airflow -f amit -l shukla -e amitshukla@gmail.com -r Admin
```
Created a service of type loadbalancer using "airflow-service.yaml" to access airflow webserver from the local system
```
kubectl apply -f airflow-service.yaml
```
Created a service of type clusterIP using "postgres-service.yaml" to give access to postgres pods inside the cluster.
```
kubectl apply -f postgres-service.yaml
```
Now again get into the the minikube cluster to create a dag in the airflow scheduler pod 

```
minikube ssh
docker exec -it -u root airflow-scheduler-id /bin/bash
cd dags
#Edited using VIM and added the same code of the simple dag above
vim postgres2.py
```
Now come to the local machine terminal and use "minikube service airflow" to run the airflow dag in the minikube.

<img width="1440" alt="Screenshot 2023-06-15 at 4 04 35 PM" src="https://github.com/rithish1126/DOCKER_KUBERNETIES/assets/122535424/949691a0-0644-4a26-85b6-58dd6e21c242">
We can then again get back into the postgres pod and run the psql command to get the tables created on airflow.

<img width="1440" alt="Screenshot 2023-06-15 at 4 20 29 PM" src="https://github.com/rithish1126/DOCKER_KUBERNETIES/assets/122535424/5144b7ba-6f36-4390-8565-a5a19ae3416c">


