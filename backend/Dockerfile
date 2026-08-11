# Use official lightweight Python image
FROM python:3.11-slim

# Prevent Python from writing .pyc files & enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install dependencies first (leverages Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend application code
COPY . .

# Default fallback port (Render overrides this with $PORT automatically)
ENV PORT=8000
EXPOSE ${PORT}

# Run Uvicorn dynamically bound to $PORT for local and Render compatibility
CMD sh -c "uvicorn main:app --host 0.0.0.0 --port ${PORT}"