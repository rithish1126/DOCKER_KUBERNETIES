from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(dag_id='postgres_task', start_date=datetime(2022, 1, 1), 
        schedule_interval='@daily',  catchup=False) as dag:

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