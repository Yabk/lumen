import streamlit as st

import utils

st.title('Instrument Classifier')

# Create file upload widget
uploaded_file = st.file_uploader('Choose a WAV file', type='wav')

if uploaded_file is not None:

    # Get file contents as bytes
    file_content = uploaded_file.read()

    # Display the file
    st.audio(file_content, format='audio/wav')

    # Query the API with the file contents
    predictions = utils.query_api(file_content)

    # Draw the predictions as a bar chart
    utils.prediction_chart(predictions)

    # Draw the spectrogram of the audio file
    utils.spectrogram(file_content)