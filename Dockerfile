# syntax=docker/dockerfile:1

# Стадия 1: сборка зависимостей
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /app

# Копируем только файлы зависимостей → отличный кэш слоёв
COPY pyproject.toml uv.lock* ./

# Устанавливаем зависимости (без проекта и без dev)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Стадия 2: финальный образ (лёгкий)
FROM python:3.12-slim-bookworm

WORKDIR /app

# ffmpeg + ffprobe (yt-dlp требует)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Копируем виртуальное окружение из builder
COPY --from=builder /app/.venv ./.venv

# Копируем весь код проекта
COPY . .

# Добавляем venv в PATH
ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Порт, на котором работает uvicorn / fastapi
EXPOSE 8000

# Запуск приложения
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]