FROM python:3.11-slim

# Устанавливаем рабочую папку
WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Собираем статические файлы Django (если нужно)
RUN python manage.py collectstatic --noinput

# Команда запуска
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]