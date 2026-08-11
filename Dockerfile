FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Render exposes $PORT automatically (defaults to 10000)
ENV PORT=8000
EXPOSE ${PORT}

# Use sh -c to expand $PORT dynamically at runtime
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT}"