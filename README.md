# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.12 or later

#### Install Python using MiniConda

1) Download and install Python 3.12
2) Create a new environment using the following command:
```bash
$ py -3.12 -m venv venv
```
3) Activate the environment:
```bash
$ venv\Scripts\Activate.ps1
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.
