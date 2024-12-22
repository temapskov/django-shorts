# Stage 1: Builder (для установки зависимостей с Poetry)
FROM python:3.13-slim AS builder

# Устанавливаем зависимость для Poetry
RUN pip install --no-cache-dir poetry

# Создаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей (poetry.lock и pyproject.toml)
COPY pyproject.toml poetry.lock /app/

# Устанавливаем зависимости через Poetry
RUN poetry install --no-dev --no-root

# Stage 2: Производственный образ
FROM python:3.13-slim AS production

# Создаем рабочую директорию
WORKDIR /app

# Копируем только необходимые файлы из сборки
COPY --from=builder /app /app

# Устанавливаем переменные окружения для Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=django_shorts.settings

# Копируем файлы проекта в контейнер
COPY . /app/

# Открываем порт 8000 для доступа
EXPOSE 8000

# Запускаем команду для старта сервера Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]