# End to End MLOps project with MLflow

# workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update constant (only one time)
5. Update the entity
6. Update the config manager in src config
7. Update the components
8. Update the pipeline
9. Update the main.py
10. Update the dvc.yaml


# Steps to run this project
clone this repository
```
git clone https://github.com/maharengarajan/End_To_End_MLOps_Project_with_MLflow.git
```

create virtual env
```
conda create -p venv python=3.10 -y
```

activate virtual environment
```
conda activate venv/
```

install requirements
```
pip install -r requirements.txt
```

Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/maharengarajan/End_To_End_MLOps_Project_with_MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=maharengarajan 

export MLFLOW_TRACKING_PASSWORD=d0af8cae7f0c8d195c580ac69666dfe9456157e1    
```

finally run the command
```
python main.py
```

# copy this below from dagshub remote
MLFLOW_TRACKING_URI=https://dagshub.com/maharengarajan/End_To_End_MLOps_Project_with_MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=maharengarajan \
MLFLOW_TRACKING_PASSWORD=d0af8cae7f0c8d195c580ac69666dfe9456157e1 \
python script.py
