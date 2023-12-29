# time-code
import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"倒计时: {seconds // 60} 分钟 {seconds % 60} 秒")
        time.sleep(1)
        seconds -= 1
    print("专注时间结束！")

focus_timer(25)  # 设置专注时间为25分钟
