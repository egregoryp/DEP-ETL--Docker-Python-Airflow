from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime

args = {"owner":"epena", "start_date":days_ago(1)}

dag = DAG(
    dag_id="test_dags",
    default_args=args,
    schedule_interval='@once' # * * * * * * cron example
)

with dag:
    run_script_print = BashOperator(
        task_id="run_script_print",
        bash_command='python "/user/app/ProyectoEndToEndPython/Clases/3.Data Scheduling/test_dags.py"'
    )