FROM python:latest

RUN apt-get update && \
    apt-get install -y libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY app app
WORKDIR /app
CMD ["python", "main.py"]


