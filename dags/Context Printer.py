from datetime import datetime

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

def print_context(**context):
    pprint(context)

with DAG(
    dag_id="context_printer",
    start_date=datetime(year=2025, month=3, day=1),
    end_date=datetime(year=2025, month=3, day=2),
    schedule="@daily",
):
    procure_rocket_material = PythonOperator(task_id="demo_templating", python_callable=_print_context)