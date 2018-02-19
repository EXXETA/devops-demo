from time import time

from flask import Flask, request
import statsd


client = statsd.StatsClient('graphite', 8125)
app = Flask('Maths service')


@app.route('/')
def index():
    return 'Maths service'


@app.route('/add')
def add():
    client.incr('add')

    x = request.args.get('x', 0.)
    y = request.args.get('y', 0.)

    x, y, = float(x), float(y)

    t0 = time()
    res = x + y
    dt = time() - t0

    client.timing('stats.timers.add', dt)

    return str(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
