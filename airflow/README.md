# Running task(s) in airflow locally with Kubernetes

---

### Steps
1. Have your kubernetes set up locally (docker-desktop)
2. Create a virtual environment
  - python3 -m venv .airflow
3. Run pip3 install -r requirements.txt
4. Save the kubeconfig into include directory
  - kubectl config view --minify --raw > include/.kube
  - convert the .kube file into json format
5. Add the json file content into airflow connection
  - admin panel => connection
  - ID: k8s_conn
  - connection type: kubernetes