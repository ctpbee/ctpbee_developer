# ctpbee_developer
ctpbee的推荐的开放模板


> 合理的架构会让你的工作量极大减少

因为ctpbee的特性，我们才得以推出这个经典的开发案例

### 用法/USAGE
git clone https://github.com/ctpbee/ctpbee_developer

然后用vscode或者pycharm打开ctpbee_developer， 开始在strategy文件夹中编写你的代码。

action.py，你可以编写一些你喜欢的操作,并在策略文件中通过self.action调用它
risk.py ，你可以在此处编写你想要的风控代码，值得注意的是你需要手动将函数手动绑定到风控上
``` 这里是个典型的风控示例
# action.py
def func(self):
  print("我想执行风控操作")
self.app.risk_gateway_class(func)即可


# risk.py
class Risk(RiskLevel):
  def before_func(self):
      print("事前")
      return True
  def after_func(self, result):
      print("事后")
```

app.py 工厂模式运行创建app，可以调用从create_app创建多个不同的账户


最后希望能极大减少你的工作量，早日实现财富自由
