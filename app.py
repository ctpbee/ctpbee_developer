from ctpbee import CtpBee

from action import ActionMe
from risk import RiskMe
from ext import data_recorder


def create_app():
    app = CtpBee("last", __name__, action_class=ActionMe, risk=RiskMe, refresh=True)

    app.config.from_pyfile("config.py")
    data_recorder.init_app(app)
    return app


if __name__ == '__main__':
    # 24 小时监管运行
    from ctpbee import hickey
    hickey.start_all(app_func=create_app)

    # 直接启动
    app = create_app()
    app.start()