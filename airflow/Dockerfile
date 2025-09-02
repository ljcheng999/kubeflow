FROM apache/airflow


COPY dags /opt/airflow/dags
COPY requirements.txt /

RUN pip3 install --no-cache-dir -r /requirements.txt