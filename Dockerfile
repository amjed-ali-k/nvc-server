FROM python:latest

ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python3", "main.py"]
