import os
import sys
# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG
from airflow.decorators import task

from datetime import timedelta

@task(task_id="hello_testtask")
def hello_testask():
    print(sys.path)
    print("Hello")
    return "Done"

@task(task_id="sentence_testtask")
def sentence_testask():
    print(sys.path)
    print("This is my version of DAG")
    return "Done"

with DAG(
    "sample_python_dag_Ali",
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["ledatascientist@ds.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5)
    },
    description="Is DAG going to work",
    catchup=False,
    tags=["demo", "example", "test"],
) as dag:
    
    test_task_hello = hello_testask()
    test_task_sentence = sentence_testask()


    test_task_hello >> test_task_sentence