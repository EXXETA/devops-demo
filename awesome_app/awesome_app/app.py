from flask import Flask, render_template
import requests


app = Flask('Awesome app')


@app.route('/<name>/<x>/<y>')
def index(name, x, y):
    greeting = requests.get('http://greetings:5000/greeting/{}'.format(name))
    greeting_type = 'hello' if 'hello' in greeting.text.lower() else 'howdy'
    sum_ = requests.get('http://maths:5000/add?x={x}&y={y}'.format(x=x, y=y))

    return render_template(
        'index.html',
        greeting=greeting.text,
        x=x,
        y=y,
        result=sum_.text,
        greeting_type=greeting_type
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
