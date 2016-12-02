from datetime import datetime, timedelta
import threading
from easygui import msgbox

def job():
    msgbox("Time to close your work, buddy!")

now = datetime.now()

run_at = now + timedelta(hours=7, minutes=30)
delay = (run_at - now).total_seconds()

threading.Timer(delay, job).start()
