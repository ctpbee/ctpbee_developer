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
class ActionMe(Action):
    def __init__(self, app):
        super().__init__(app)
        self.add_risk_check(self.short)
        self.add_risk_check(self.cancel)

# risk.py
class Risk(RiskLevel):
  
    def before_func(self,*args, **kwargs):
          print("事前")
          return True, *args, **kwargs
    
      def after_func(self, result):
          print("事后")

app.py create app by factory pattern, and create multiple account by calling it.
ext.py storing the ctpbee plug-in

At last, hopefully it will greatly reduce your workload and bring you financial freedom as soon as possible

