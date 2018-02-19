from flask import Flask
import requests


app = Flask('Awesome app')


@app.route('/<name>/<x>/<y>')
def index(name, x, y):
    greeting = requests.get('http://greetings:5000/hello/{}'.format(name))
    sum_ = requests.get('http://maths:5000/add?x={x}&y={y}'.format(x=x, y=y))

    return '{greeting}, {x} + {y} = {sum_}'.format(
        greeting=greeting.text,
        x=x,
        y=y,
        sum_=sum_.text
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
