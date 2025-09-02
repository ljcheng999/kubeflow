from pendulum import datetime
from airflow import DAG
# from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator


with DAG(
  dag_id="example_kubernetes_pod",
  schedule="@once",
  start_date=datetime(2025, 9, 2),
) as dag:
  ### Reference:
  # https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/_api/airflow/providers/cncf/kubernetes/operators/pod/index.html
  # https://airflow.apache.org/docs/apache-airflow-providers-cncf-kubernetes/stable/operators.html
  example_kpo = KubernetesPodOperator(
    kubernetes_conn_id="k8s_conn",
    image="hello-world",
    name="airflow-test-pod",
    task_id="airflow-test-pod-1",
    cluster_context="docker-desktop",
    is_delete_operator_pod=True, # if you don't want the pod being deleted after task is done, set this to false
    get_logs=True,
  )

  example_kpo