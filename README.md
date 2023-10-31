# NLP Engineer Assignment

This repository contains the skeleton code for the coding assignment for the NLP Engineer position at Yaraku, Inc. You should use it alongside the provided instructions to complete the assignment.

## Requirements

- Python (created and tested with version `3.10.5`)
- Poetry (created and tested with version `1.6.1`)
- (Optional) Docker

## Setup

1. Start by cloning the repository into your local environment.
2. Install poetry in your local environment by running: `pip install poetry`
3. Create the virtual environment for the project by running: `poetry install`
4. Initialize the virtual environment by running: `poetry shell`
5. Run the entrypoint script with: `python main.py`

The code should initially print out an exception that says: 

```
You should implement `train_classifier` in transformer.py. 
```

Once you are done with your implementation, you should be able to run the script without the exception. Then navigate to http://localhost:8000/docs to access the Swagger UI and test your API.

## Docker

We have also included a Dockerfile in the repository to ensure that it works across different environments. Feel free to use the Dockerfile if it works better for you. You can consult how to work with Dockerfiles at the [Docker documentation](https://docs.docker.com).
