import json
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
import numpy as np
import mlflow
from mlflow.models import make_metric
import matplotlib.pyplot as plt
import os

# loading the California housing dataset
cali_housing = fetch_california_housing(as_frame=True)

# split the dataset into train and test partitions
X_train, X_test, y_train, y_test = train_test_split(
    cali_housing.data, cali_housing.target, test_size=0.2, random_state=123
)

# train the model
lin_reg = LinearRegression().fit(X_train, y_train)

# creating the evaluation dataframe
eval_data = X_test.copy()
eval_data["target"] = y_test


def custom_metric(eval_df, _builtin_metrics):
    return np.sum(np.abs(eval_df["prediction"] - eval_df["target"] + 1) ** 2)


class ExampleClass:
    def __init__(self, x):
        self.x = x


def custom_artifact(eval_df, builtin_metrics, _artifacts_dir):
    example_np_arr = np.array([1, 2, 3])
    example_df = pd.DataFrame({"test": [2.2, 3.1], "test2": [3, 2]})
    example_dict = {"hello": "there", "test_list": [0.1, 0.3, 4]}
    example_dict.update(builtin_metrics)
    example_dict_2 = '{"a": 3, "b": [1, 2, 3]}'
    example_image = plt.figure()
    plt.scatter(eval_df["prediction"], eval_df["target"])
    plt.xlabel("Targets")
    plt.ylabel("Predictions")
    plt.title("Targets vs. Predictions")
    example_custom_class = ExampleClass(10)

    return {
        "example_np_arr_from_obj_saved_as_npy": example_np_arr,
        "example_df_from_obj_saved_as_csv": example_df,
        "example_dict_from_obj_saved_as_json": example_dict,
        "example_image_from_obj_saved_as_png": example_image,
        "example_dict_from_json_str_saved_as_json": example_dict_2,
        "example_class_from_obj_saved_as_pickle": example_custom_class,
    }


with mlflow.start_run() as run:
    mlflow.sklearn.log_model(lin_reg, "model")
    model_uri = mlflow.get_artifact_uri("model")
    result = mlflow.evaluate(
        model=model_uri,
        data=eval_data,
        targets="target",
        model_type="regressor",
        evaluators=["default"],
        custom_metrics=[
            make_metric(
                eval_fn=custom_metric,
                greater_is_better=False,
            )
        ],
        custom_artifacts=[
            custom_artifact,
        ],
    )

print(f"metrics:\n{result.metrics}")
print(f"artifacts:\n{result.artifacts}")
