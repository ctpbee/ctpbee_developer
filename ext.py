"""
    在这里导入插件
        ext.py 创建插件实例

        strategy 在策略中导入实例进行使用
        app  在create_app函数中使用实例.init_app(app)
"""

from strategy import DataRecorder

data_recorder = DataRecorder("data_recorder")
