from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd
import sys
sys.path.append("..")
from customer_review_func import (get_customer_data, data_clean_up, push_to_s3, install_required_libraries)

import os
from airflow.sdk import Variable

default_args = {
  "owner": "airflow",
  "depends_on_past": False,
  "start_date": datetime(2025, 9, 2),
  "email_on_failure": False,
  "email_on_rretry": False,
  "retries": 1,
  "retry_delay": timedelta(minutes=1)
}

dag = DAG("customer_review_data", default_args=default_args, description="amazon products review")

install_libraries_task = PythonOperator(task_id="install_libraries", python_callable=install_required_libraries, dag=dag)

run_etl = PythonOperator(task_id = "get_raw_data", python_callable=get_customer_data, dag=dag)

transform_task = PythonOperator(task_id = "data_cleanup", python_callable=data_clean_up, dag=dag)