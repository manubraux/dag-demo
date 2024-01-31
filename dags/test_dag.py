import os
import sys
# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG
from airflow.decorators import task

from datetime import timedelta


@task(task_id="hello")
def hello_task():
    print(sys.path)
    print("Hello, this is the test task from gatien")
    return "Done"


@task(task_id="bye")
def bye_task():
    print("bye")
    return "Done"


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
b
    t1 = hello_task()
    t2 = bye_task()

    t1 >> t2
