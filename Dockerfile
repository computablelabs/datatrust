FROM python:3.7-stretch

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP app.py
CMD ["python", "-m", "flask", "run"]
