FROM python:3.7

WORKDIR /opt/app
ENV DEBIAN_FRONTEND=noninteractive

# TODO: remove git dependency. Right now needed for tinyAPI.
RUN apt-get update && \
    apt-get install -y supervisor netcat libmemcached-dev zlib1g-dev git mysql-server libsasl2-modules opendkim opendkim-tools && \
    pip install uwsgi && \
    mkdir /config && touch /config/.env

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["supervisord", "-n", "-c", "/opt/app/supervisor.conf"]
