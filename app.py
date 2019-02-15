import os

import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker
from flask import Flask

app = Flask('Pika Example')

broker = RabbitmqBroker(url='amqp://localhost:5672')
dramatiq.set_broker(broker)

@dramatiq.actor
def do_this_thing():
    pass

@app.route('/')
def schedule():
    do_this_thing.send()
    return '1'
