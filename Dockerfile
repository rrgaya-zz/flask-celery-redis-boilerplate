# FROM python:3.8.0-alpine

# WORKDIR /usr/src/app

# COPY requirements.txt .

# RUN pip install -r requirements.txt

# COPY . .

# ENV FLASK_APP="app"

# EXPOSE 5000

# CMD ["flask", "run", "-h", "0.0.0.0"]


FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]