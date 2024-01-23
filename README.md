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


# overview of deployment
```
#with specific access
1. EC2 access : It is virtual machine
2. ECR: Elastic Container registry to save your docker image in aws

#Description: About the deployment
1. Build docker image of the source code
2. Push your docker image to ECR
3. Launch Your EC2 
4. Pull Your image from ECR in EC2
5. Lauch your docker image in EC2
```

# AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS account
2. Create IAM user for deployment
```
#Policy:

1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess
```
3. Create ECR repo to store/save docker image
```
ECR repo URI: 920535735578.dkr.ecr.us-east-1.amazonaws.com/mlops
```
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine
```
#optinal
sudo apt-get update -y
sudo apt-get upgrade

#required
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
6. Configure EC2 as self-hosted runner
```
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```
7. Setup github secrets
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION = us-east-1
AWS_ECR_LOGIN_URI = demo>>  920535735578.dkr.ecr.us-east-1.amazonaws.com
ECR_REPOSITORY_NAME = mlops
```
8. push codes to github and check actions
9. check the EC2 running instance there public ip will be available