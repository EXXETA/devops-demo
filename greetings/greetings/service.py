from flask import Flask


app = Flask('Greetings service')


@app.route('/hello/<name>')
def greeting(name):
    return 'Hello {}'.format(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
