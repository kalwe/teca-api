# FROM python:3.9-slim

# WORKDIR /app

# COPY requirements.txt .
# COPY .env .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# EXPOSE 5000

# CMD ["uvicorn", "run:create_app", "--factory", "--host=0.0.0.0", "--port", "5000", "--reload", "--proxy-headers"]


# Staged
FROM ubuntu:22.04 as dependencies

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=nointeractive

# Install packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    python3.10 -m pip install --upgrade pip
    python3.10 \
    python3.10-dev \
    python3.10-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/**

# Python 3.10 as default
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# Install poetry
ENV POETRY_VERSION=0.4.2
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Configure poetry
RUN poetry config virtualenvs.create false

WORKDIR /app

# Copy only pyproject.toml to create cache deps
COPY pyproject.toml ./

# Gen poetry.lock and install deps
RUN poetry lock && poetry install --no-root

# STAGE:DEVELOPMENT
FROM dependencies as development

RUN apt-get update && apt-get install -y \
    vim \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY app /app

# Install the root package
RUN poetry install

EXPOSE 5001

CMD poetry run hypercorn app.asgi:app -b 0.0.0.0:5001 --reload

# STAGE:PRODUCTION
FROM dependencies as production

COPY app ./app

# Install the root package
RUN poetry install

EXPOSE 5001

CMD poetry run hypercorn app.asgi:app -b 0.0.0.0:5001
