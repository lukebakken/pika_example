# pika_example
Minimal example for reproducing FileNotFoundError bug in pika.

## Build
docker build -t app .

## Run
docker run --rm -d -e BROKER_URL="amqp://<rabbit-host>" -p 8080:8000 app

## Test
curl localhost:8080
