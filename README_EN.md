# ctpbee_developer
the open template recommended by ctpbee 

> A reasonable structure can greatly reduce your workload


Because of the characteristics of ctpbee, we were able to present this classic development case


### USAGE
git clone https://github.com/ctpbee/ctpbee_developer

Then use the vscode or pycharm to open ctpbee_developer folder， and write your strategy code in strategy folder

action.py，you can write some operation code, and call it by self.operation in strategy file
risk.py ，you can write risk code in here. Note that you need to manually bind the function to the risk control manually

``` risk example
# action.py
def func(self):
  print("I want to do risk control")
self.app.risk_gateway_class(func)


# risk.py
class Risk(RiskLevel):
  def before_func(self):
      print("before")
      return True
  def after_func(self, result):
      print("after")
```

app.py create app by factory pattern, and create multiple account by calling it.
ext.py storing the ctpbee plug-in

At last, hopefully it will greatly reduce your workload and bring you financial freedom as soon as possible

