from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime

args = {"owner":"epena", "start_date":days_ago(1)}

dag = DAG(
    dag_id="ingesta_dag",
    default_args=args,
    schedule_interval='@once' # * * * * * * cron example
)

with dag:
    run_script_ingest = BashOperator(
        task_id="run_script_ingest",
        bash_command='python "/user/app/ProyectoEndToEndPython/Proyecto/Ingesta.py"'
    )    

    run_script_transform = BashOperator(
        task_id="run_script_transform",
        bash_command='python "/user/app/ProyectoEndToEndPython/Proyecto/Transformacion.py"'
    )

    run_script_load = BashOperator(
        task_id="run_script_load",
        bash_command='python "/user/app/ProyectoEndToEndPython/Proyecto/Carga.py"'
    )

    run_script_ingest >> run_script_transform >> run_script_load