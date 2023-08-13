from flask import Flask, render_template, request
from config import LocalConfig
from ds18b20 import DS18B20

conf = LocalConfig()
sensor = DS18B20()


app = Flask(__name__)


def get_data():
    conf.get_config_data()
    sensor_links = sensor.tempC(0)
    sensor_rechts = sensor.tempC(1)
    xs_temp = conf.settings['xs_temp']
    xs_hysterese = conf.settings['xs_hysterese']

    return sensor_links, sensor_rechts, xs_temp, xs_hysterese


@app.route('/')
def hello_world():
    sensor_links, sensor_rechts, xs_temp, xs_hysterese = get_data()
    return render_template('start.html', sensor_rechts=sensor_rechts, sensor_links=sensor_links, xs_temp=xs_temp,
                           xs_hysterese=xs_hysterese)


@app.route('/', methods=['POST'])  # post example
def post_hello():
    try:
        form_xs_temp = request.form.get('form_xs_temp')
        form_xs_hysterese = request.form.get('form_xs_hysterese')
        if not form_xs_temp == "":
            conf.set_config_data('SETTINGS', 'xs_temp', form_xs_temp)
        if not form_xs_hysterese == "":
            conf.set_config_data('SETTINGS', 'xs_hysterese', form_xs_hysterese)


        sensor_links, sensor_rechts, xs_temp, xs_hysterese = get_data()
        return render_template('start.html', sensor_rechts=sensor_rechts, sensor_links=sensor_links, xs_temp=xs_temp,
                               xs_hysterese=xs_hysterese)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

