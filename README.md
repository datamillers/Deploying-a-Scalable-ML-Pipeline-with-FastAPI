# Census Classification Model

This project builds and deploys a machine learning model that predicts whether a person earns `<=50K` or `>50K` using census data.
---
## Repository
https://github.com/datamillers/Deploying-a-Scalable-ML-Pipeline-with-FastAPI

## Project Overview

- Train a classification model on census data
- Evaluate model performance and slice metrics
- Write unit tests for the ML pipeline
- Deploy the model using FastAPI
- Test the API locally

---

## Training the Model

Run the training script:

python train_model.py

This will:
- Train the model
- Save model artifacts
- Generate slice performance metrics in `slice_output.txt`

---

## Unit Tests

Run unit tests with:

pytest

All tests should pass.

---

## API Usage

Start the API:

uvicorn main:app --reload

### Root Endpoint
- GET /
- Returns a simple greeting message

### Inference Endpoint
- POST /data/
- Accepts census feature data
- Returns a prediction (`<=50K` or `>50K`)

The API can be tested using Swagger UI at `/docs`.

---

## Notes

This project is for educational purposes only and is not intended for real-world deci


Working in a command line environment is recommended for ease of use with git and dvc. If on Windows, WSL1 or 2 is recommended.

# Environment Set up (pip or conda)
* Option 1: use the supplied file `environment.yml` to create a new environment with conda
* Option 2: use the supplied file `requirements.txt` to create a new environment with pip
    
## Repositories
* Create a directory for the project and initialize git.
    * As you work on the code, continually commit changes. Trained models you want to use in production must be committed to GitHub.
* Connect your local git repo to GitHub.
* Setup GitHub Actions on your repo. You can use one of the pre-made GitHub Actions if at a minimum it runs pytest and flake8 on push and requires both to pass without error.
    * Make sure you set up the GitHub Action to have the same version of Python as you used in development.

# Data
* Download census.csv and commit it to dvc.
* This data is messy, try to open it in pandas and see what you get.
* To clean it, use your favorite text editor to remove all spaces.

# Model
* Using the starter code, write a machine learning model that trains on the clean data and saves the model. Complete any function that has been started.
* Write unit tests for at least 3 functions in the model code.
* Write a function that outputs the performance of the model on slices of the data.
    * Suggestion: for simplicity, the function can just output the performance on slices of just the categorical features.
* Write a model card using the provided template.

# API Creation
*  Create a RESTful API using FastAPI this must implement:
    * GET on the root giving a welcome message.
    * POST that does model inference.
