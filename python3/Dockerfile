FROM docker.io/python:3.12.9-slim-bookworm AS base

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Copy and install runtime dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app

EXPOSE 8080

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080"]
