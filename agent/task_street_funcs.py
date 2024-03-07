from tqdm import tqdm 
import time 
import random

from agent.config import wait_time


task_street_prompt = """[底层程序消息]接下来你要引导盲人进入道路对面的教学楼。你要先穿过道路，注意行人和来车。你可以调用的方法有：[{"name": "get_surrounding_state", "description": "向底层程序获取周边的情况，会向你汇报距离1m以内的行人，距离5m以内的车辆，正前方距离1m以内的台阶。"}, {"name": "move_forward", "description": "向前移动。"}, {"name": "stop", "description": "停止移动。"}, {"name": "pass", "description": "不调用任何方法。"}, {"name": "climb_mode", "description": "普通行动模式下，切换为攀爬模式。"}, {"name": "common_mode", "description": "攀爬模式下，切换为普通行动模式。"}, {"name": "exit", "description": "结束任务。"}]"""


def get_surrounding_state(cli=True):
    if cli:
        print("[情景模拟]")
        print("InternDog正在探测周边环境状况。")
        print("现在，有您来充当底层程序。您可以将探测结果告诉InternDog。")
        print("\t输入0:表示周围安全；")
        print("\t输入1:表示周围1m内有人；")
        print("\t输入2:表示周围5m内有车；")
        print("\t输入3:表示前方有楼梯；")
        print("\t输入4:表示离开了楼梯；")
        print("\t输入5:表示已经进入了教学楼。")
        while True:
            inp = input("[你的输入] >>> ")
            if not inp.isdigit():
                print("!!!!警告：输入格式错误!!!")
                continue 
            inp = int(inp)
            if inp == 0:
                message = "[底层程序消息]周围安全。"
                break
            elif inp == 1:
                message = "[底层程序消息]左方距离{:.2f}m有行人。".format(random.random())
                break
            elif inp == 2:
                direct = random.choice(["左", "右"])
                message = "[底层程序消息]{}方距离{:.2f}m有车辆驶来。".format(direct, random.random() * 5)
                break
            elif inp == 3:
                message = "[底层程序消息]前方楼梯。"
                break
            elif inp == 4:
                message = "[底层程序消息]离开楼梯。"
                break 
            elif inp == 5:
                message = "[底层程序消息]已进入教学楼。"
                break
            else:
                print("!!!!警告：输入格式错误!!!")
                continue
        return message  


def move_forward(cli=True):
    if cli:
        print("[情景]导盲犬正在向前移动...")
        for i in tqdm(range(wait_time)):
            time.sleep(0.1)
        message = "[底层程序消息]开始向前移动。"
        return message


def stop(cli=True):
    if cli:
        print("[情景]导盲犬正在停止运动...")
        for i in tqdm(range(wait_time)):
            time.sleep(0.1)
        message = "[底层程序消息]已停止运动。"
        return message


def climb_mode(cli=True):
    if cli:
        print("[情景]导盲犬正在切换为攀爬模式...")
        for i in tqdm(range(wait_time)):
            time.sleep(0.1)
        message = "[底层程序消息]已切换为攀爬模式。"
        return message


def common_mode(cli=True):
    if cli:
        print("[情景]导盲犬正在切换为普通模式...")
        for i in tqdm(range(wait_time)):
            time.sleep(0.1)
        message = "[底层程序消息]已切换为普通模式。"
        return message
    