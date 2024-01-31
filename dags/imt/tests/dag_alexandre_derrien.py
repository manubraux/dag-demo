import os
import sys
from time import sleep
# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG
from airflow.decorators import task

from datetime import timedelta

@task(task_id="test_task")
def simple_testask():
    print(sys.path)
    print("Hello, this is the test task")
    return "Done"

@task
def harder_task():
    print("wait for 5 seconds")
    return "You just lost 5 seconds"
with DAG(

    "sample_python_dag",
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
    description="A basic example DAG ",
    catchup=False,
    tags=["demo", "example", "test"],

) as dag:
    
    test_task = simple_testask()
    nd_task =  harder_task()

    test_task >> nd_task