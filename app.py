from time import sleep

from ctpbee import CtpBee

from action import ActionMe
from risk import RiskMe
from strategy import DataRecorder


def create_app():
    app = CtpBee("last", __name__, action_class=ActionMe, work_mode="forever", refresh=True)

    app.config.from_pyfile("config.py")
    app.add_risk_gateway(RiskMe)
    data_recorder = DataRecorder("data_recorder", app)
    app.start(log_output=False)
    return app


if __name__ == '__main__':
    app = create_app()
