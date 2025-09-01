# Installation of Kubeflow Pipelines

The guide to install Kubeflow or any of its components is the official documentation. 

-----------------------------

### Deploy Kubeflow Pipeline
References:
- [Official Doc](https://www.kubeflow.org/docs/components/pipelines/legacy-v1/installation/localcluster-deployment/#deploying-kubeflow-pipelines)

Steps:
```
### Run the following in your terminal

PIPELINE_VERSION=2.14.0

kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic?ref=$PIPELINE_VERSION"

### View the dashboard locally
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
```

### Install Python kfp module
My current Python version is 3.13.5, so don't get when you import/install base_image, it should be the same or similar version for python file
1. Create a desier folder at your directory - `mkdir kfp`
2. Create a Python virtual environment - `python3 -m venv .kfp`
3. Source the virtual environment - `source .kfp/bin/activate`
4. Install the package - `pip3 install kfp`










