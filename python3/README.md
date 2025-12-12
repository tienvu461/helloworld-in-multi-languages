# Python FastAPI Hello World

This is a minimal FastAPI example that serves the contents of `health.json` at the `/health` endpoint.

Quick commands:

Build the docker image:

```bash
docker build -t himl-python:latest .
```

Run the container (mapped to port 8080):

```bash
docker run --rm -p 8080:8080 himl-python:latest
```

Then visit http://localhost:8080/health

Run the tests locally (recommended inside a venv):

```bash
python -m pip install -r requirements.txt pytest
pytest -q
```
