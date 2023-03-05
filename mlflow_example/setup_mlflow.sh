# create a virtual environment with pyenv
PYTHON=3.9.16
ENV_NAME=mlflow-example
pyenv virtualenv $PYTHON $ENV_NAME
pyenv local $ENV_NAME
# pyenv activate $ENV_NAME

# install packages
pip install mlflow
pip install scikit-learn
pip install pandas
pip install ipykernel 
