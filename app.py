from time import sleep

from ctpbee import CtpBee

from action import ActionMe

from risk import RiskMe
from strategy import DataRecorder


def create_app():
    app = CtpBee("last", __name__, action_class=ActionMe)

    info = {
        "CONNECT_INFO": {
            "userid": "089131",
            "password": "350888",
            "brokerid": "9999",
            "md_address": "tcp://180.168.146.187:10131",
            "td_address": "tcp://180.168.146.187:10130",
            # "md_address": "tcp://218.202.237.33:10112",
            # "td_address": "tcp://218.202.237.33:10102",
            "product_info": "",
            "appid": "simnow_client_test",
            "auth_code": "0000000000000000",
        },
        "INTERFACE": "ctp",
        "TD_FUNC": True,
        "MD_FUNC": True,
    }
    app.config.from_mapping(info)
    app.add_risk_gateway(RiskMe)
    data_recorder = DataRecorder("data_recorder", app)

    app.start()
    return app


if __name__ == '__main__':
    app = create_app()
    while True:
        app.query_position()
        sleep(1)
        app.query_account()
        sleep(1)
