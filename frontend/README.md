# Deploy

1) Build the docker image

```docker build -t lumen/frontend .```
2) Run the docker image;
   - set the BACKEND_URL environment variable to the url of the backend
   - expose port 8501 of the container

```docker run -d -p 8501:8501 -e 'BACKEND_URL=http://backend:8000' lumen/frontend```

# Use
Open the frontend url in your browser and upload an audio file to classify.