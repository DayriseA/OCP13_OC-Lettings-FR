#####
CI-CD
#####

Main CI/CD Pipeline
===================


Quick overview
--------------

This pipeline is triggered on every push to the repository, but the second job is only executed for pushes
on the `main` branch.

- The first job, `build-and-test`, sets up the environment, installs dependencies, and runs linting and tests. 
  If linter or test fails, the job fails and the pipeline stops.
- The second job, `containerize-and-push`, starts only if the first job is successful. 
  It builds a Docker image and pushes it to the Docker Hub registry.
- Finally, the image is deployed on Render thanks to a webhook. This is not directly handled in this workflow, 
  but it is triggered by the latest image pushed to the registry.

Jobs details
------------

1. **build-and-test**

    This job runs on the latest version of Ubuntu. It has several environment variables set for debugging 
    and database configuration. It also sets up a PostgreSQL service.

    Steps:

    - *Checkout code*: This step checks out your repository using the `actions/checkout@v4` action.
    - *Install poetry*: This step installs poetry using pipx.
    - *Set up Python*: This step sets up Python using the `actions/setup-python@v5` action.
    - *Install dependencies*: This step installs the project dependencies using poetry.
    - *Run linting*: This step runs flake8 for linting the code.
    - | *Run tests*: This step runs pytest for testing the code.
      | It also checks the code coverage and fails if it is under 80%.

2. **containerize-and-push**

    This job also runs on the latest version of Ubuntu. It depends on the `build-and-test` job.
    It is skipped if the previous job fails or if the branch is not `main`.

    Steps:

    - *Checkout code*: This step checks out your repository using the actions/checkout@v4 action. 
    - *Set up Docker Buildx*: This step sets up Docker Buildx using the docker/setup-buildx-action@v3 action. 
    - *Login to Docker Hub*: This step logs into Docker Hub using the docker/login-action@v3 action.
      It uses the Docker Hub username and access token stored in the GitHub secrets.
    - *Extract metadata for web*: This step extracts metadata for the web image using 
      the docker/metadata-action@v5 action. The generated tags are used in the next step 
      to tag the Docker image.
    - *Build and push web image*: This step builds the Docker image and pushes it to Docker Hub using 
      the docker/build-push-action@v5 action.

    .. note::
      This job is crucial for continuous deployment, as it ensures that every successful build on the 
      main branch results in a new Docker image that can be deployed. 
      The image is built with the latest code, ensuring that the deployed application is always up-to-date. 
      The image is pushed to Docker Hub, making it available for any deployment service that pulls images from 
      Docker Hub.

3. **deploy-on-render**
    
    This job is not part of the pipeline, but it is triggered by the latest image pushed to the registry.
    Deployments are made on https://oc-lettings-prebuilt-image.onrender.com
    