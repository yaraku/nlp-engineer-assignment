FROM python:3.10-slim-bullseye

# Install required system-level packages.
ARG DEBIAN_FRONTEND=noninteractive
ENV PIP_DEFAULT_TIMEOUT 500
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PIP_NO_CACHE_DIR 1
RUN pip install poetry

# Copy project directories and files over to image.
WORKDIR /root
COPY data               /root/data
COPY src                /root/src
COPY tests              /root/tests
COPY main.py            /root/main.py
COPY pyproject.toml     /root/pyproject.toml

# Create the virtual environment and install the required packages.
ENV POETRY_VIRTUALENVS_CREATE 0
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONHASHSEED random
RUN poetry install --no-interaction --no-ansi                                           \
    && rm -rf ~/.cache

# Expose the required ports.
EXPOSE 8000

# Execute the main script.
CMD ["sh", "-c", "python main.py"]
