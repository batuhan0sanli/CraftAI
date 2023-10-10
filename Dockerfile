FROM python:3.11.5-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

ADD Pipfile /.
ADD Pipfile.lock /.

RUN pip3 install pipenv
RUN pipenv install --system --deploy

COPY . /app
WORKDIR /app

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["pipenv", "run", "up"]
