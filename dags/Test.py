from datetime import datetime

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

def createEmptyOperator(taskId):
        return EmptyOperator(task_id= taskId )

with DAG(
    dag_id="launch_dag",
    start_date=datetime(year=2025, month=3, day=1),
    end_date=datetime(year=2025, month=3, day=2),
    schedule="@daily",
):
    procure_rocket_material = createEmptyOperator("procure_rocket_material")
    procure_fuel = createEmptyOperator("procure_fuel")
    build_stage_1 = createEmptyOperator("build_stage_1")
    build_stage_2 = createEmptyOperator("build_stage_2")
    build_stage_3 = createEmptyOperator("build_stage_3")
    launch = createEmptyOperator("launch")

    procure_rocket_material >> [build_stage_1, build_stage_2, build_stage_3] >> launch
    procure_fuel >> build_stage_3 >> launch
