FROM python:latest

WORKDIR /app

ADD . .
RUN pip install -r requirements.txt

EXPOSE 8080

COPY ./app /app

CMD ["python3", "main.py"]
