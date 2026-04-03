# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.12 or later

#### Install Python using MiniConda

1) Download and install Python 3.12
2) Create a new environment using the following command:
```bash
py -3.12 -m venv venv
```
3) Activate the environment:
```bash
venv\Scripts\Activate.ps1
```

## Installation

### Install the required packages

```bash
pip install -r requirements.txt
```

### Setup the environment variables

```bash
cp .env.example .env
```
### Run Alembic Migration
```bash
 alembic upgrade head
```
Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

### Run Docker Compose Services
```bash
cd docker
cp .env.example .env
```
### update .env with your credentials
```bash
cd docker
docker compose up -d
```
### Run the FastAPI server (Development Mode)

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 5000
```