from ctpbee import CtpBee

from action import ActionMe
from risk import RiskMe
from strategy import DataRecorder


def create_app():
    app = CtpBee("last", __name__, action_class=ActionMe, risk=RiskMe, refresh=True)

    app.config.from_pyfile("config.py")
    data_recorder = DataRecorder("data_recorder", app)
    return app


if __name__ == '__main__':
    from ctpbee import hickey
    hickey.start_all(app_func=create_app)
