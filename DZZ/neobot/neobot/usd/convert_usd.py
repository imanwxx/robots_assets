#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pxr import Usd
import os

# 只转换机器人，不转换场景
def convert_robot_only(input_robot_file="neobot_robot.usd", output_file="neobot_robot.usda"):
    """
    只转换机器人USD文件，不包含场景元素
    """
    # 检查配置文件目录是否存在
    config_dir = "configuration"
    input_path = os.path.join(config_dir, input_robot_file)
    
    if not os.path.exists(input_path):
        print(f"错误: 找不到机器人USD文件 {input_path}")
        print("可用的机器人USD文件:")
        if os.path.exists(config_dir):
            for f in os.listdir(config_dir):
                if f.endswith('_robot.usd'):
                    print(f"  - {os.path.join(config_dir, f)}")
        return False
    
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"错误: 无法打开USD文件 {input_path}")
        return False
    
    stage.Export(output_file)
    print(f"已成功转换机器人: {input_path} -> {output_file}")
    print("注意: 此转换仅包含机器人模型，不包含场景元素")
    return True

# 如果需要转换完整的USD文件（包含场景），保留原函数
# def convert_complete_usd(input_file="neobot.usd", output_file="neobot_complete.usda"):
#     stage = Usd.Stage.Open(input_file)
#     stage.Export(output_file)
#     print(f"已转换完整文件: {input_file} to {output_file}")

if __name__ == "__main__":
    # 默认只转换机器人
    success = convert_robot_only()
    
    # 如果需要转换完整文件，取消下面的注释
    # convert_complete_usd()

