# Используем официальный образ Python
FROM python:3.13-slim

# Устанавливаем переменные окружения для Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=django_shorts.settings

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY django_shorts/ /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Открываем порт 8000
EXPOSE 8000

# Команда запуска Django сервера
CMD ["python", "django_shorts.manage.py", "runserver", "0.0.0.0:8000"]