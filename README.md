
# Music Recommender Project

## Overview
This project is a music recommendation system that predicts music preferences based on user input such as age and gender. The system utilizes a machine learning model built with `scikit-learn` and deployed using `FastAPI`. Additionally, it is containerized using Docker and deployed to the cloud with Render.

## Part 1: Building the Machine Learning Model
### Objective
The first part of the project involves building and training a machine learning model to predict music genres based on user features such as age and gender.

### Steps:
1. Set up the environment with Anaconda.
2. Use Jupyter Notebook to develop the model and save it using `joblib`.
3. Train a Decision Tree model using the provided dataset `music.csv`.
4. Save the model as `music_recommender.joblib`.

### Requirements:
- pandas
- numpy
- scikit-learn
- joblib

---

## Part 2: Version Control with Git
### Objective
Track the project files using Git and push them to a remote repository on GitHub.

### Steps:
1. Initialize a Git repository.
2. Add files to the repository and commit.
3. Push the changes to GitHub.

---

## Part 3: Creating a Prediction Service with FastAPI
### Objective
Build a FastAPI web service that serves the trained model and provides predictions.

### Steps:
1. Install FastAPI and Uvicorn.
2. Create an API with a `POST` endpoint to predict music genre based on user input.
3. Test the FastAPI application locally.
4. Commit and push the changes to GitHub.

---

## Part 4: Containerization with Docker
### Objective
Containerize the FastAPI application using Docker.

### Steps:
1. Create a `Dockerfile` to define the environment.
2. Build the Docker image.
3. Test the containerized app.
4. Push the Docker image to Docker Hub.
5. Commit and push the `Dockerfile` to GitHub.

---

## Part 5: CI/CD Pipeline with GitHub Actions
### Objective
Automate the build and deployment process using GitHub Actions.

### Steps:
1. Create a CI/CD workflow file (`.github/workflows/ci-cd.yml`).
2. Configure Docker Hub credentials in GitHub Secrets.
3. Push the workflow file and verify the pipeline runs.

---

## Part 6: Cloud Deployment and Monitoring (Using Render)
### Objective
Deploy the FastAPI application to Render and monitor its performance.

### Steps:
1. Set up a Render account and link it to your GitHub repository.
2. Configure the environment and deploy the application.
3. Test the deployed application.
4. Monitor the logs for any issues.

---

## Requirements for Deployment
- Python 3.x
- FastAPI
- Uvicorn
- joblib
- scikit-learn
- pandas
- numpy

---

## Test the API
After deployment, you can test the prediction service by sending a `POST` request:

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"age": 21, "gender": 1}'
```

Expected response:
```json
{"genre": "HipHop"}
```

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
