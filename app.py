from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('start.html', headline='have fun')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
