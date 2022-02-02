from ctypes import Structure, windll, c_uint, sizeof, byref
import time
import datetime

class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    """Returns the idle duration in seconds"""
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0

while True:
    now = datetime.datetime.now()
    print("[" + now.strftime("%H:%M") + "] ", end="")

    # If the system was idle for more than 60 seconds
    # move the mouse to the top left corner
    # and click
    if get_idle_duration() > 60:
        print("Idle for more than 60 seconds. Clicking...")
        windll.user32.SetCursorPos(0,0)
        windll.user32.mouse_event(2, 0, 0, 0)
        windll.user32.mouse_event(4, 0, 0, 0)
    else:
        waitingTime = round(max(60 - get_idle_duration(), 1), 2)
        print("Nothing to do. Checking again in " + str(waitingTime) + " seconds...")
        time.sleep(waitingTime)
