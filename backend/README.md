# Deploy

1) Build the docker image

```docker build -t lumen/backend .```
2) Run the docker image;
   - mount a directory containing the trained pytorch models
   - set the MODEL_PATH environment variable to the path of a saved pytorch model
   - expose port 8000 of the container

```docker run -d -p 8000:8000 -v /path/to/models:/models -e 'MODEL_PATH=/model/resnet50.ckpt lumen/backend```

# Test
Use the following `curl` command to test if the backend is running correctly:

```curl -X POST -F "file=@/path/to/audio.wav" http://localhost:8000/predict```