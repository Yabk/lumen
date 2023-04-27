import io
import random
from typing import List, Tuple

import librosa
import numpy as np
from fastapi import FastAPI, UploadFile

app = FastAPI()

# Define the class labels for the model
LABELS = ("cel", "cla", "flu", "gac", "gel", "org", "pia", "sax", "tru", "vio", "voi")


def preprocess_audio(audio_bytes: bytes) -> Tuple[np.ndarray, int]:
    """Preprocess the audio file to meet the requirements of the model."""
    with io.BytesIO(audio_bytes) as f:
        signal, sr = librosa.load(f, sr=22050, mono=True)

    return signal, sr


def dummy_predict(audio: np.ndarray, sr: int) -> List[float]:
    """Return a random prediction for each class label."""
    predictions = [random.uniform(0, 1) for i in range(len(LABELS))]
    return predictions


@app.post("/predict")
async def predict(file: UploadFile):
    """Predict API endpoint."""
    audio_bytes = await file.read()

    audio, sr = preprocess_audio(audio_bytes)
    predictions = dummy_predict(audio, sr)
    label_probabilities = {LABELS[i]: float(predictions[i]) for i in range(len(LABELS))}

    return label_probabilities
