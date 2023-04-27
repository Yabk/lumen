import io
import os

import librosa as lr
import matplotlib.pyplot as plt
import numpy as np
import requests
import streamlit as st

BACKEND_URL = os.environ.get('BACKEND_URL', 'http://localhost:8000')

plt.style.use('dark_background')


def query_api(file: bytes) -> dict:
    """Query the backend API with the given audio file."""
    # Create the multipart-encoded form data
    files = {'file': ('file.wav', file, 'audio/wav')}
    response = requests.post(f'{BACKEND_URL}/predict', files=files)

    # Raise exception if the API call fails
    response.raise_for_status()

    return response.json()


def prediction_chart(predictions: dict, threshold: float = 0.5) -> None:
    """Create a bar chart of the predictions."""
    fig, ax = plt.subplots()
    x = np.arange(len(predictions))
    bars = ax.bar(x, predictions.values(), align='center')
    ax.set_xticks(x)
    ax.set_xticklabels(predictions.keys())
    plt.ylim([0, 1])
    plt.title('Predictions')

    # Color the bars differently based on threshold
    values = list(predictions.values())
    for i, bar in enumerate(bars):
        if values[i] >= threshold:
            bar.set_color('green')
        else:
            bar.set_color('red')
    ax.axhline(y=threshold, color='r', linestyle='--')

    st.pyplot(fig)


def spectrogram(file: bytes) -> None:
    signal, sr = lr.load(io.BytesIO(file), sr=22050, mono=True)
    fig, ax = plt.subplots()
    plt.specgram(signal, Fs=sr, cmap='inferno')
    plt.title('Spectrogram')
    st.pyplot(fig)
