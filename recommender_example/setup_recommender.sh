# Create a virtual environment with pyenv
PYTHON=3.9.16
ENV_NAME=recommender-example
pyenv virtualenv $PYTHON $ENV_NAME
pyenv local $ENV_NAME
# pyenv activate $ENV_NAME

# Install packages
pip install --upgrade pip
pip install --upgrade setuptools
pip install jupyterlab
pip install ipykernel
pip install recommenders[all]

# Register environment with Jupyter:
# PYTHON=3.9.16
# ENV_NAME=recommender-example
python -m ipykernel install --user --name $ENV_NAME --display-name "$ENV_NAME $PYTHON"

# Start JupyterLab
jupyter lab