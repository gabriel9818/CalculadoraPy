# Calculadora Py

Calculadora Py is a simple web calculator application developed in Python with Flask. This repository contains the source code and the Dockerfile needed to run the application in a Docker container.

## Requirements

- Python 3.12 or higher
- Docker (optional, only if you want to run the application in a container)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/calculadora-py.git
    cd calculadora-py
    ```

2. Install the dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Running with Docker

You can also run the application in a Docker container.

1. Pull the image from Docker Hub:

    ```bash
    docker pull gabrielrv/hola-py
    ```

2. Run the image:

    ```bash
    docker run -p 5000:5000 gabrielrv/hola-py
    ```

## Dockerfile

This project includes a `Dockerfile` that performs the following actions:

- Uses a Python 3.12-slim base image.
- Copies and installs the dependencies from `requirements.txt`.

## Docker (for local builds)

If you cloned the repository and opened it in a code editor, follow these steps to build and run locally:

1. Build the image:

    ```bash
    docker build -t calculadorapy .
    ```

2. Run the container:

    ```bash
    docker run -p 5000:5000 calculadorapy
    ```




