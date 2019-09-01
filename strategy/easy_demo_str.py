from datetime import datetime

from ctpbee import CtpbeeApi
from ctpbee.constant import LogData, AccountData, PositionData


class DataRecorder(CtpbeeApi):
    def __init__(self, name, app=None):
        super().__init__(name, app)
        self.instrument_set = set(["ag1910.SHFE"])
        self.init_flag = False
        self.converter = None

    def on_trade(self, trade):
        pass

    def on_realtime(self, timed: datetime):
        pass

    def on_contract(self, contract):
        # 订阅所有
        if contract.symbol in self.instrument_set:
            self.app.subscribe(contract.symbol)

    def on_order(self, order):
        pass

    def on_position(self, position: PositionData) -> None:
        pass

    def on_account(self, account: AccountData) -> None:
        if not self.init_flag:
            print("111")
            return
        #
        # print(self.converter.account_df)

    def on_init(self, init):
        self.init_flag = True

        print("初始化完成")

    def on_tick(self, tick):
        """tick process function"""

    def on_bar(self, bar):
        """bar process function"""

    def on_log(self, log: LogData):
        """ 可以用于将log信息推送到外部 """
        pass
