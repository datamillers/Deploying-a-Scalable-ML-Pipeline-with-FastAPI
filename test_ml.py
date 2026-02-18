import pytest
import pandas as pd
import numpy as np

from ml.data import process_data
from ml.model import train_model, inference

# TODO: add necessary import above
CAT_FEATURES = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]

# TODO: implement the first test. Change the function name and input as needed
def test_process_data():
    """
    # add description for the first test
    Test process_data returns features and label arrays with matching row counts.
    """
    # Your code here
    data = pd.read_csv("data/census.csv").sample(100, random_state=42)

    X, y, encoder, lb = process_data(
        data,
        categorical_features=CAT_FEATURES,
        label="salary",
        training=True,
    )

    assert X.shape[0] > 0
    assert y.shape[0] > 0
    assert encoder is not None
    assert lb is not None


# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    """
    # add description for the second test
    Test train_model successfully returns a trained model object
    """
    # Your code here
    data = pd.read_csv("data/census.csv").sample(100, random_state=42)

    X, y, _, _ = process_data(
        data,
        categorical_features=CAT_FEATURES,
        label="salary",
        training=True,
    )

    model = train_model(X, y)

    assert model is not None
    assert hasattr(model, "predict")


# TODO: implement the third test. Change the function name and input as needed
def test_inference():
    """
    # add description for the third test
    Test inference returns a prediction for every input row, prediction matches
    number of samples passed to the inference function
    """
    # Your code here
    data = pd.read_csv("data/census.csv").sample(100, random_state=42)

    X, y, _, _ = process_data(
        data,
        categorical_features=CAT_FEATURES,
        label="salary",
        training=True,
    )

    model = train_model(X, y)
    preds = inference(model, X)

    assert isinstance(preds, np.ndarray)
    assert len(preds) == len(y)
