from airflow.decorators import dag, task
from pendulum import datetime, timedelta

@dag(
    dag_id="write_var_dag",
    start_date=datetime(2022,12,10),
    schedule_interval=timedelta(seconds=10),
    catchup=False,
)
def write_var():

    @task
    def set_var():
        return "bar"

    @task
    def retrieve_var(my_variable):
        print(my_variable)

    retrieve_var(set_var())

write_var()