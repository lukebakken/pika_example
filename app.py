import os

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from flask import Flask

app = Flask('Pika Example')


url = os.getenv('BROKER_URL')
# url = 'amqp://localhost'


broker = RabbitmqBroker(url=url)
dramatiq.set_broker(broker)


@dramatiq.actor
def do_this_thing():
    pass


@app.route('/')
def schedule():
    do_this_thing.send()
    return '1'
