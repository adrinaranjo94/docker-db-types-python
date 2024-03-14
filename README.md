# Database viewer

## Introduction

This project is designed to provide a simple environment for viewing and interacting with MySQL, Redis, MongoDB, and Cassandra databases using Python. It utilizes Docker Compose to orchestrate the necessary containers, making it easy to set up and run locally.

## Features

- View and interact with MySQL, Redis, MongoDB, and Cassandra databases.
- Python scripts provided for querying and modifying data in each database.
- Docker Compose configuration for easy setup and teardown of the database environment.

## Getting Started

These are the steps to set up and run the project.

### 1. Set up Virtual Environment

It is recommended to use a virtual environment to install the project dependencies and avoid conflicts with other projects.

```bash
# Install virtualenv if not installed
pip install virtualenv

# Create a new virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Linux/Mac
source venv/bin/activate
```

### 2. Install dependencies

Once the virtual environment is activated, install the project dependencies from the `requirements.txt` file.

```bash
# Install requirements txt dependencies
pip install -r requirements.txt
```

### 3. Run with docker-compose

The project uses Docker Compose to orchestrate Docker containers. Make sure you have Docker and Docker Compose installed on your system.

```bash
# Bring up the services using Docker Compose
docker-compose up -d
```
