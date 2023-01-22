FROM python:latest

WORKDIR /app

ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py
COPY app app

EXPOSE 8080

CMD ["python3", "main.py"]
