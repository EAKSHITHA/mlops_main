Steps followed:
https://c17hawke.github.io/wafer_mlops_docs/stage1_init_setup/

Environment 'wafer3' created using venv (and not conda)

Questions asked while creatin the project:
project_name [project_name]: mlops_main
repo_name [mlops_main]: mlops_main
author_name [Your name (or your organization/company/team)]: c17hawke
description [A short description of the project.]: its a wafer project using mlops
Select open_source_license:
1 - MIT
2 - BSD-3-Clause
3 - No license file
Choose from 1, 2, 3 [1]: 1
s3_bucket [[OPTIONAL] your-bucket-for-syncing-data (do not include 's3://')]: 
aws_profile [default]: 
Select python_interpreter:
1 - python3
2 - python
Choose from 1, 2 [1]: 1

- .gitkeep is present to maintain the directory structure as github does not accept empty directory, hence gitkeep

- .env file is to declare keys, config file, and . meaning its hidden file

- setup.py is used to convert all the development process that is present in src dir and use it as a package in this file (due to presence of __init__.py) and when we run setup.py, it install the src dir as a package with the help of requirements.txt (# local package -e .)

-tox.ini : will used to testing and building process locally
    flake8 - lenting property - to check the code quality of python packages

https://dvc.org/doc/install/windows - to install dvc inside 'mlops_main' repo

- dvc init - creates .dvc and .dvccignore files

- to commit to git that is public and also keep it secret from public, we git it as secret in git
  go to settings in git -> then secrets -> new repository secrets

- inside src, create a file named pipeline_01_data_preparation.py

- inside config, create three files:

params.yaml : all configurations in the entire project is centralized to one file : this is the config file that enters into args.config
schema_training.json : 
schema_prediction.json : 