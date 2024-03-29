import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "project2"

list_of_files = [
            f"src/{project_name}/__init__.py",
            f"src/{project_name}/component/data_ingestion.py",
            f"src/{project_name}/component/data_transformation.py",
            f"src/{project_name}/component/model_trainer.py",
            f"src/{project_name}/component/model_monitoring.py",
            f"src/{project_name}/pipelines/__init__.py",
            f"src/{project_name}/pipelines/training_pipeline.py",
            f"src/{project_name}/pipelines/prediction_pipeline.py",
            f"src/{project_name}/exception.py",
            f"src/{project_name}/logger.py",
            f"src/{project_name}/utils.py",
            'app.py',
            'DockerFile'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory {filedir} for the filename {filename}")
    if ((not os.path.exists(filepath)) or (os.path.getsize==0)):
        with open(filepath,"w") as f:
            pass
            logging.info(f"creating empty file {filepath}")
    else:
        logging.info(f"{filename} already exist ")