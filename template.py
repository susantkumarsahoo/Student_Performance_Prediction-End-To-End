import os
from pathlib import Path

# Define project name (main source folder)
project_name = "src"

# Define additional folders
cicd_folder = ".github/workflows"
configs_folder = "configs"
data_folder = "data"
notebooks_folder = "notebooks"
static_css_folder = "static/css"
templates_folder = "templates"
tests_folder = "tests"
scripts_folder = "scripts"

# List of files & folders to create
list_of_files = [
    # Source code (directly inside project_name)
    f"{project_name}/__init__.py",

    f"{project_name}/config/__init__.py",
    f"{project_name}/config/config_manager.py",
    f"{project_name}/config/project_config.yaml",

    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/aws_configuration_manager.py",
    f"{project_name}/configuration/mango_configuration_manager.py",
    f"{project_name}/configuration/sql_configuration_manager.py",

    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/aws_db_api_model_key.py",

    f"{project_name}/connections/__init__.py",
    f"{project_name}/connections/aws_connection.py",
    f"{project_name}/connections/db_connection.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",

    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_preprocessing.py",
    f"{project_name}/components/feature_transformer.py",

    f"{project_name}/models/__init__.py",
    f"{project_name}/models/model_train.py",
    f"{project_name}/models/model_evaluate.py",
    f"{project_name}/models/model_predict.py",
    f"{project_name}/models/model_save_load.py",

    f"{project_name}/pipelines/__init__.py",
    f"{project_name}/pipelines/training_pipeline.py",
    f"{project_name}/pipelines/prediction_pipeline.py",
    f"{project_name}/pipelines/deployment_pipeline.py",

    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/logger.py",

    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",

    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_handler.py",
    f"{project_name}/utils/perm_metrics.py",
    f"{project_name}/utils/helpers.py",

    f"{project_name}/visualization/__init__.py",
    f"{project_name}/visualization/plots.py",
    f"{project_name}/visualization/dashboard.py",

    # Cloud storage
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws.py",

    f"{project_name}/monitoring/__init__.py",
    f"{project_name}/monitoring/data_drift.py",
    f"{project_name}/monitoring/model_drift.py",

    # Outside project_name
    f"{cicd_folder}/github_actions.yml",
    f"{configs_folder}/ml_config.yaml",
    f"{data_folder}/.gitkeep",
    f"{notebooks_folder}/01_EDA.ipynb",

    f"{templates_folder}/project.html",
    f"{static_css_folder}/style.css",

    # Scripts
    f"{scripts_folder}/data_automation.py",
    f"{scripts_folder}/run_pipeline.sh",
    f"{scripts_folder}/db_backup.py",

    # Tests
    f"{tests_folder}/__init__.py",
    f"{tests_folder}/test_models.py",

    # Root-level files
    "README.md",
    "requirements.txt",
    ".env",
    "setup.py",
    ".gitignore",
    ".dockerignore",
    "Dockerfile",
    "app.py",
    "demo.py",
]

# Create files and directories
for filepath in list_of_files:
    file_path = Path(filepath)
    dir_path = file_path.parent
    os.makedirs(dir_path, exist_ok=True)  # Create directories
    if not file_path.exists():
        file_path.touch()  # Create empty file
        print(f"Created: {file_path}")
    else:
        print(f"Already exists: {file_path}")

































