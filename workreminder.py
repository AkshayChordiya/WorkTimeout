from datetime import datetime, timedelta
import threading
from easygui import msgbox

def job():
    msgbox("Time to close your work, buddy!")

now = datetime.now()

run_at = now + timedelta(hours=6, minutes=10)
delay = (run_at - now).total_seconds()

threading.Timer(delay, job).start()
