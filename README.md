# Running
Simplest way to run the project is using docker and docker-compose.
You can use the provided `docker-compose-example.yml` file as a reference.

You will have 2 running containers:
1) Backend
   - Exposes port `8000` and expects a mounted directory containing the trained pytorch models.
   - Also, expects the `MODEL_PATH` environment variable to be set to the path of a saved pytorch model.
2) Frontend
   - Exposes port `8501` and expects the `BACKEND_URL` environment variable to be set to the url of the backend.

Once both containers are up and running, you can access the frontend via any internet browser and upload an audio file to classify.

In `backend` and `frontend` directories you can find README.md files with more detailed instructions on how to run each service individually.