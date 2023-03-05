# Learning From Example

![Logo](https://mlflow.org/images/MLflow-header-pic@2x.png)

- Create Date: 2023-03-05
- Author: Chris Cui

This repository contains a collection of examples of how to use the advanced package related to Machine Learning and AI.

- [Learning From Example](#learning-from-example)
  - [Python Enveronment Setup](#python-enveronment-setup)
  - [Learning Python Environment Setup](#learning-python-environment-setup)
    - [Example: Recommender](#example-recommender)
  - [Learning Example List](#learning-example-list)

## Python Enveronment Setup

This repo use `pyenv` for managing python version. To install `pyenv` on your machine, please follow the instruction on [pyenv](https://realpython.com/intro-to-pyenv/)

After installing `pyenv`, you can install the python version (3.9.16) used in this repo by running the following command:

```bash
pyenv install 3.9.16
```

In the root folder of this repo, you can setup the default local python environmnet by running the following command:

```bash
pyenv local 3.9.16
```

You can check the current python version by running the following command:

```bash
# python --version or python -V
pyenv which python
```

## Learning Python Environment Setup

In each example folder, you can find(create) a `setup.sh` file. Then, setup a new virtual environment for learning. Customise the `setup.sh` file to your needs. Here is an example of the `setup.sh` of the recommender example:

### Example: Recommender

The `setup.sh` file will create a virtual environment and install all the required packages for the example.

```bash
# get into the recommender example folder
cd recommender_example 
# make the setup.sh file executable
chmod +x setup.sh 
# run the setup.sh file
./setup.sh
```

Here is the content of the `setup.sh` file:

```bash
# Create a virtual environment with pyenv
PYTHON=3.9.16
ENV_NAME=recommender-example
pyenv virtualenv $PYTHON $ENV_NAME
pyenv local $ENV_NAME

# Install packages
pip install --upgrade pip
pip install --upgrade setuptools
pip install jupyterlab
pip install recommenders[all]

# Register environment with Jupyter (optional):
pip install ipykernel
python -m ipykernel install --user --name $ENV_NAME --display-name "$ENV_NAME $PYTHON"

# Start JupyterLab
jupyter lab
```

This will create a new virtual environment and install all the required packages for the example.

## Learning Example List

This repo contains the following examples:

1. [Recommender Example](recommender_example/README.md)
![workflow](https://recodatasets.z20.web.core.windows.net/images/reco_workflow.png)
2. [MLflow Example](mlflow_example/README.md)
3. [Ray Example](ray_example/README.md)
![Ray AIR](https://docs.ray.io/en/latest/_images/ray-air.svg)
![Why AIR](https://docs.ray.io/en/latest/_images/why-air.svg)

