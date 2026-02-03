from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2026, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="crypto_dag",
    default_args=default_args,
    schedule=timedelta(minutes=10),
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id="extract_data_from_api",
        bash_command=(
            "python3 /opt/airflow/scripts/extract_crypto.py "
            "{{ var.value.COINGECKO_API_KEY }}"
        ),
    )

    extract_task
