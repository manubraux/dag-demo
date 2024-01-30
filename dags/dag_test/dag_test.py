#AIT MBARK AYMANE
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import timedelta
from airflow.utils.dates import days_ago

def simple_test_task():
    print("Hello, this is the test task")
    return("Done")
def compteur():
    for number in range(100):
        print(number)
    return("Done")

def utilisateur():
    print('Aymane')
    return("Done")
# Définissez votre DAG
with DAG(
    "sample_python_dag",
    default_args={
        "depends_on_past": False,
        "email": ["ledatascientist@ds.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5)
    },
    description="A basic example DAG",
    schedule_interval=None,  # Définissez ici votre planification
    start_date=days_ago(1),  # Modifiez la date de début en fonction de vos besoins
    catchup=False,
    tags=["demo", "example", "test"],
) as dag:

    # Créez des opérateurs Python pour vos tâches
    test_task = PythonOperator(
        task_id="test_task",
        python_callable=simple_test_task,
    )

    test_compteur_task = PythonOperator(
        task_id="test_compteur_task",
        python_callable=compteur,
    )

    test_utilisateur_task = PythonOperator(
        task_id="test_utilisateur_task",
        python_callable=utilisateur,
    )

    # Définissez les dépendances entre les tâches
    test_task >> test_compteur_task >> test_utilisateur_task
