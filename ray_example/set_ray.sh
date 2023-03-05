# create a virtual environment with pyenv
PYTHON=3.9.16
ENV_NAME=ray-example
pyenv virtualenv $PYTHON $ENV_NAME
pyenv local $ENV_NAME
# pyenv activate $ENV_NAME

# install packages
# pip install ray
pip install "ray[air]"
pip install xgboost_ray
pip install "ray[tune]"


pip install ipykernel
pip install pandas 
pip install torch
pip install numpy
pip install tensorflow
pip install pyarrow
pip install xgboost
pip install tqdm

