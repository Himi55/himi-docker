FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install \
    libgl1 \
    libgl1-mesa-glx \
    libglib2.0-0 -y

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update \
    && apt-get install -y kafkacat \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
