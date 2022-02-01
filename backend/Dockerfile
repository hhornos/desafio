FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD uvicorn main:app --workers 4 --host 0.0.0.0 --port 5000
