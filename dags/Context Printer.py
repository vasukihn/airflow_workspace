from datetime import datetime
from pprint import pprint
from airflow.models import DAG
from airflow.operators.python import PythonOperator

def print_context(**context):
    pprint(context)

with DAG(
    dag_id="context_printer",
    start_date=datetime(year=2025, month=3, day=1),
    end_date=datetime(year=2025, month=3, day=2),
    schedule="@daily",
):
    print_context_var = PythonOperator(task_id="context_printer_task_id", python_callable=print_context)
