from flask import Flask, render_template
from application.database import Database

app = Flask(__name__)

db = Database()


@app.route('/')
def hello_world():  # put application's code here
    return render_template('start.html', title='Your App')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
