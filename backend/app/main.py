import io
import os
import sys
from typing import Tuple

import librosa
import numpy as np
from fastapi import FastAPI, UploadFile

from .notebook_finder import NotebookFinder

sys.meta_path.append(NotebookFinder())

from .model.full_model import FullModel

try:
    MODEL_CHECKPOINT_PATH = os.environ['MODEL_PATH']
except KeyError as e:
    print('Set the environment variable MODEL_PATH to point to the model checkpoint.')
    raise e

model = FullModel(MODEL_CHECKPOINT_PATH)

app = FastAPI()

# Define the class labels for the model
LABELS = ("cel", "cla", "flu", "gac", "gel", "org", "pia", "sax", "tru", "vio", "voi")


def preprocess_audio(audio_bytes: bytes) -> Tuple[np.ndarray, int]:
    """Preprocess the audio file to meet the requirements of the model."""
    with io.BytesIO(audio_bytes) as f:
        signal, sr = librosa.load(f, sr=22050, mono=True)

    return signal, sr


@app.post("/predict")
async def predict(file: UploadFile):
    """Predict API endpoint."""
    audio_bytes = await file.read()

    audio, sr = preprocess_audio(audio_bytes)
    predictions = model.predict(audio, sr)

    return predictions
