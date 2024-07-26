from enum import Enum
import time

TEMP_PATH = "/sys/devices/virtual/thermal/thermal_zone0/temp"
FAN_PATH = "/sys/class/thermal/cooling_device0/cur_state"


class FanSpeed(Enum):
    OFF = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    FULL = 4


def main():
    start = time.time()
    while True:
        temp = get_temp()
        if temp > 60:
            speed = FanSpeed.FULL
        elif temp > 55:
            speed = FanSpeed.HIGH
        elif temp > 45:
            speed = FanSpeed.MEDIUM
        elif temp > 40:
            speed = FanSpeed.LOW
        else:
            speed = FanSpeed.OFF
        set_fan_speed(speed)
        time.sleep(30)

        
def get_temp() -> int:
    with open(TEMP_PATH, "r") as f:
        data = f.read()
    return int(data) // 1000


def set_fan_speed(speed: FanSpeed):
    with open(FAN_PATH, "w") as f:
        f.write(str(speed.value))


if __name__ == "__main__":
    main()
