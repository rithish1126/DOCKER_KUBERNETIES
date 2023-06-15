from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
# Created a Dag to run every minute
with DAG(dag_id='postgres_task', start_date=datetime(2022, 1, 1), 
        schedule_interval='*/1 * * * *',  catchup=False) as dag: 
#Postgres Operator with respective airflow connection id, to create a table with only one attribute\
#curr_time TIMESTAMP
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres_default',
        sql='''
            CREATE TABLE IF NOT EXISTS postgres_table (
                curr_time TIMESTAMP
            );
        '''
    )
#Postgres Operator with respective airflow connection id, to insert into the above table 
    insert_records = PostgresOperator(
        task_id = 'insert_records',
        postgres_conn_id='postgres_default',
        sql = '''
                INSERT INTO postgres_table VALUES (CURRENT_TIMESTAMP);   
        '''
    )
#dependencies 
    create_table >> insert_records
