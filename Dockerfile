FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8001

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8001 & python manage.py process_tasks"]
