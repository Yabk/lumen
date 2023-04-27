# Use an official Python runtime as a parent image
FROM python:3.10-bullseye

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the frontend code into the container at /app
COPY . /app

# Expose the port that the frontend will be running on
EXPOSE 8501

# Start the frontend server
CMD ["streamlit", "run", "src/app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
