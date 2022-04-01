FROM python:3.8.3
LABEL maintainer 'Wellington Zambiazzi <wellington.zambiazzi@jqb.global>'

RUN apt-get update && apt-get install -y curl

WORKDIR /app

COPY . /app

RUN pip install Flask

EXPOSE 5000

CMD ["python3", "app.py"]