import logging
from random import choice, random

from flask import Flask, redirect, request
import redis
from redis.exceptions import ConnectionError


app = Flask('Greetings service')
logging.basicConfig(level='INFO')


try:
    key_value_store = redis.StrictRedis(host='redis')
    key_value_store.get('hello')
except ConnectionError:
    key_value_store = {}  # default to in-memory key-value store if Redis not available


@app.route('/greeting/<name>')
def greeting(name):
    hello_likes = int(key_value_store.get('hello') or 0)
    howdy_likes = int(key_value_store.get('howdy') or 0)

    logging.info('Hello likes {}, howdy likes {}'.format(hello_likes, howdy_likes))

    if random() <= .1:
        # explore greeting performance
        logging.info('Exploring greetings ...')
        greeting_generator = choice([hello, howdy])
    else:
        # exploit best performing greeting
        logging.info('Exploiting best performing greeting ...')
        if hello_likes > howdy_likes:
            greeting_generator = hello
        else:
            greeting_generator = howdy

    return greeting_generator(name)


def hello(name):
    return 'Hello {}'.format(name)


def howdy(name):
    return 'Howdy {}'.format(name)


@app.route('/like_greeting', methods=['POST'])
def greeting_performance():
    greeting_type = 'hello' if 'hello' in request.form else 'howdy'

    try:
        key_value_store.incr(greeting_type, amount=1)
    except AttributeError:
        key_value_store[greeting_type] += 1

    return redirect(request.referrer)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
