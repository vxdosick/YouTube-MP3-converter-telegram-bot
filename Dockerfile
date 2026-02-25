# syntax=docker/dockerfile:1

# Step 1: install dependencies
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock* ./

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Step 2: build app
FROM python:3.12-slim-bookworm

WORKDIR /app

# ffmpeg + ffprobe (yt-dlp need it)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment
COPY --from=builder /app/.venv ./.venv

# Copy source code
COPY . .

# Add venv to PATH
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Port
EXPOSE 8000

# Run app
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "${PORT:-8000}"]