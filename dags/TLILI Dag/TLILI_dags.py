import os
import sys
import math as m 
# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG
from airflow.decorators import task

from datetime import timedelta

@task(task_id="carré_parfait")
def simple_testask1():
    print(sys.path)
    print("Hello, these are 10 perfect squares")
    for i in range(10):
        print(i*i)
    return "Done"

@task(task_id="sqrt")
def simple_testask2():
    print(sys.path)
    print("Hello, these are 10 square roots")
    for i in range(10):
        print(m.sqrt(i))
    return "Done"
with DAG(
    "Ramy_dag",
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
    
    t1 =simple_testask1()
    t2=simple_testask2()


    t1>>t2