import os
from joblib import load
import json
from pathlib import Path
import numpy as np
import pandas as pd
from skimage.io import imread_collection
from skimage.transform import resize
from sklearn.metrics import accuracy_score
from airflow.decorators import task

def load_images(data_frame, column_name):
    filelist = data_frame[column_name].to_list()
    image_list = imread_collection(filelist)
    return image_list


def load_labels(data_frame, column_name):
    label_list = data_frame[column_name].to_list()
    return label_list


def preprocess(image):
    resized = resize(image, (100, 100, 3))
    reshaped = resized.reshape((1, 30000))
    return reshaped


def load_data(data_path):
    df = pd.read_csv(data_path)
    labels = load_labels(data_frame=df, column_name="label")
    raw_images = load_images(data_frame=df, column_name="filename")
    processed_images = [preprocess(image) for image in raw_images]
    data = np.concatenate(processed_images, axis=0)
    return data, labels

@task(task_id="evaluation")
def start_evaluation(repo_path, model_path, metrics_path, **kwargs):   
    repo_path = Path(repo_path)
    model_path = Path(model_path)
    metrics_path = Path(metrics_path)
    test_csv_path = repo_path / "prepared/test.csv"
    test_data, labels = load_data(test_csv_path)
    model = load(model_path / "model.joblib")
    predictions = model.predict(test_data)
    accuracy = accuracy_score(labels, predictions)
    metrics = {"accuracy": accuracy}
    accuracy_path = metrics_path / "accuracy.json"
    accuracy_path.write_text(json.dumps(metrics))
    return ("Done. This is the accuracy of the model: %2.5f" % (accuracy)) 

if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    start_evaluation(repo_path)
