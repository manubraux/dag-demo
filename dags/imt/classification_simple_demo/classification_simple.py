# The DAG object; we'll need this to instantiate a DAG
from airflow.models.dag import DAG
from airflow.decorators import dag, task

from datetime import datetime, timedelta

from imt.classification_simple_demo.prepare_task import start_preparation
from imt.classification_simple_demo.train_task import start_training
from imt.classification_simple_demo.validation_task import start_evaluation

DATA_PATH = "/opt/airflow/data"
MODEL_PATH = "/opt/airflow/models"
METRICS_PATH = "/opt/airflow/metrics"

with DAG(
    "classification_basic_1",
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
    description="A basic DAG for a simple calssification task",
    catchup=False,
    tags=["demo", "classification"],
) as dag:

    prepare = start_preparation(DATA_PATH)
    train = start_training(DATA_PATH, MODEL_PATH)
    evaluation = start_evaluation(DATA_PATH, MODEL_PATH, METRICS_PATH)

    prepare >> train >> evaluation