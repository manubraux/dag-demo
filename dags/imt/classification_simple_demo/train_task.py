from airflow.decorators import task

import numpy as np
import pandas as pd
from pathlib import Path


from skimage.io import imread_collection
from skimage.transform import resize
from sklearn.linear_model import SGDClassifier
from joblib import dump
from sklearn.ensemble import RandomForestClassifier
"""

"""

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

@task(task_id="training")
def start_training(repo_path, model_path, **kwargs):
    repo_path = Path(repo_path)
    model_path = Path(model_path)
    train_csv_path = repo_path / "prepared/train.csv"
    train_data, labels = load_data(train_csv_path)
    sgd = RandomForestClassifier(**kwargs)
    trained_model = sgd.fit(train_data, labels)
    dump(trained_model, model_path / "model.joblib")
    return "Training done"

